import importlib
import os
from pathlib import Path
class DataLoader:

    def __init__(self):
        self.models = {}
        self.airfoils = {}
        cwd = Path('.')
        datadir = cwd / 'data'
        self.model_path = datadir / 'models'
        self.airfoil_path = datadir / 'airfoils'
        self.models = \
            [x.name for x in self.model_path.iterdir()
                    if x.is_file()
                    and x.suffix == '.py']
        self.airfoils = \
            [ x.name for x in self.airfoil_path.iterdir()
                    if x.is_dir() ]

    def list_models(self):
        return self.models

    def list_airfoils(self):
        return self.airfoils

    def load_airfoil(self, name):
        is not name in self.airfoils:
            return {}
        else: # import data file
            try:
                sys.path.append(self.airfoil_path)
                m = importlib.import_module(name)
            except:
                print(airfoil not loaded")

if __name__ == '__main__':
    dl = DataLoader()
    print(dl.list_models())
    print(dl.list_airfoils())
