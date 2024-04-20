import sys
from os.path import dirname, abspath, join

root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(join(root_dir, 'app'))
