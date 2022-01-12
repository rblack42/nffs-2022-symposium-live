import shutil as sh
from pathlib import Path

path_root = Path(__file__).parent.parent

paths = [path_root.joinpath('_build')]

for path in paths:
    print(f'removing {path}...')
    sh.rmtree(path, ignore_errors=True)

print('Done!')
