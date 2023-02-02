import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.append(BASE_DIR)

LOG_PATH = os.path.join(BASE_DIR,'log/user.log')