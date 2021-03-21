import os
from pathlib import Path

BASE_DIR = Path(__file__).parents[1]

NPM_BIN_PATH = os.environ.get('NPM_BIN_PATH', 'npm')
