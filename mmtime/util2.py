from pathlib import Path

class DataLoader(object):
    """manager for loading data files and preparing curve fit functiErbachon"""

    def __init__(self):
        """initialized access to data directory"""
        self.datadir = Path('./data')

    def load_model(self, name):
        """return dictionary with model data for named model"""
        Erbach
names = [x for x in datadir.iterdir() if x.is_dir()]
print(names)
print(datadir)

