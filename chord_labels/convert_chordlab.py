import argparse
import os

import numpy as np
import pandas as pd

from .chord_labels import parse_chord, PITCH_CLASS_NAMES

def convert_chordlab_file(input_path, output_path):
    df = read_chordlab_tsv(input_path)
    _, ext = os.path.splitext(output_path)
    ext = ext[1:]
    if ext == 'tsv':
        df = convert_chordlab_df(df)
        df.to_csv(output_path, sep='\t', index=None)
    elif ext == 'npy' or ext == 'npz':
        pc_matrix = convert_labels_to_matrix(df['label'])
        if ext == 'npy':
            np.save(output_path, pc_matrix)
        elif ext == 'npz':
            np.savez_compressed(output_path, pc_matrix)

def read_chordlab_tsv(path):
    # try to guest the separator (in Isophonics it can be a space: ' ')
    return pd.read_csv(path, delim_whitespace=True,
         header=None, names=['start', 'end', 'label'], dtype=str)

def convert_chordlab_df(df, label_col='label'):
    """
    Converts a DataFrame with chord segment annotations - add columns with
    binary pitch classes and with root and bass pitch classes.

    Input: a DataFrame with columns including `label_col`, typically
           ('start', 'end', 'label')
    Output: a DataFrame with added columns
           ('root', 'bass', 'C', 'Db', ..., 'Bb', 'B')
    """
    # Series of ChordLabel
    parsed_labels = df[label_col].apply(lambda label: parse_chord(label))
    df['root'] = parsed_labels.apply(lambda l: l.root)
    df['bass'] = parsed_labels.apply(lambda l: l.bass)
    # TODO: Better just use columns 'pc_0', 'pc_1', ..., 'pc_12' that can be
    # later selected more easily.
    for pc, name in enumerate(PITCH_CLASS_NAMES):
        df[name] = parsed_labels.apply(lambda l: l.tones_binary[pc])
    return df

def convert_labels_to_matrix(labels):
    """
    Converts a list of string chord labels to a numpy matrix of pitch classes
    in one-hot encoding.

    Output: numpy array of shape: (chord_count, 12)
    """
    return np.vstack([parse_chord(l).tones_binary for l in labels]).astype(np.uint8)

def parse_args():
    parser = argparse.ArgumentParser('Convert symbolic chord labels to binary pitch classes')
    parser.add_argument('labels_file', help='TSV file with chord labels')
    parser.add_argument('pc_file', help='output file with pitch classes (tsv, npy, npz)')
    return parser.parse_args()

def main():
    args = parse_args()
    convert_chordlab_file(args.labels_file, args.pc_file)

if __name__ == '__main__':
    main()
