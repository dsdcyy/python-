import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.append(BASE_DIR)

from core.core import main
if __name__ == '__main__':
    main()