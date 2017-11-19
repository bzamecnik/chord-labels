import os

import numpy as np
import pandas as pd

from chord_labels.convert_chordlab import (
    convert_chordlab_df, convert_labels_to_matrix,
    read_chordlab_tsv)

data_dir = os.path.dirname(__file__)

def test_convert_chordlab_df():
    df = read_chordlab_tsv(os.path.join(data_dir, 'yesterday-orig.lab'))
    df_actual = convert_chordlab_df(df)
    df_expected = pd.read_csv(os.path.join(data_dir, 'yesterday-expected.tsv'), sep='\t')
    assert all(df_actual == df_expected)

def test_convert_labels_to_matrix():
    df = read_chordlab_tsv(os.path.join(data_dir, 'yesterday-orig.lab'))
    pc_matrix = convert_labels_to_matrix(df['label'])
    assert pc_matrix.shape == (len(df), 12)
    assert pc_matrix.dtype == np.uint8
    expected = np.load(os.path.join(data_dir, 'yesterday-expected.npz'))
    assert np.allclose(pc_matrix, expected['arr_0'])
