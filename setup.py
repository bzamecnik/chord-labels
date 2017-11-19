import distutils.cmd
import distutils.log
import glob
import os
from setuptools import setup
import subprocess

# Regenerating the lexer/parser code needs antlr4 installed.
# Ubuntu: $ sudo apt install antlr4
# OS X: $ brew install antlr
class AntlrGeneratorCommand(distutils.cmd.Command):
    """Runs ANTLR4 to generate lexer/parser source files."""

    description = 'run ANTLR4 to generate Python source files'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print('Regenerating parser code using ANTLR...')
        target_dir = 'chord_labels/parser'
        for f in glob.glob(os.path.join(target_dir, 'ChordLabel*')):
            print('rm', f)
            os.remove(f)
        command = ['antlr4', '-Dlanguage=Python3', '-o', target_dir, 'ChordLabel.g4']
        self.announce('Running command: %s' % ' '.join(command), level=distutils.log.INFO)
        subprocess.check_call(command)

setup(name='chord_labels',
      version='0.1',
      description='MIREX-style chord label parser',
      url='https://github.com/bzamecnik/chord_labels',
      author='Bohumir Zamecnik',
      author_email='bohumir.zamecnik@gmail.com',
      license='MIT',
      packages=['chord_labels', 'chord_labels.parser'],
      include_package_data=True,
      zip_safe=False,
      cmdclass={'antlr': AntlrGeneratorCommand},
      install_requires=[
        'antlr4-python3-runtime',
        'typing'
      ],
      # brew install pandoc
      # setup_requires=['setuptools-markdown'],
      # long_description_markdown_filename='README.md',
      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',

          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 3',

          'Operating System :: POSIX :: Linux'
      ],
      # entry_points={
          # 'console_scripts': [
          #     'chord_labels = chord_labels.__main__:main'
          # ]
      # }
)
