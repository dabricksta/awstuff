from setuptools import setup
from awstuff import version
from configparser import ConfigParser

# get details from the config.cfg
cfgp = ConfigParser()
cfgp.read('setup.cfg')

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

if __name__ == "__main__":
  setup(name='awstuff',
      version= version.__version__,
      description='Helper functions for interacting with AWS and other misc tasks',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['awstuff'],
      author_email=cfgp['metadata']['author_email'],
      zip_safe=False)
  