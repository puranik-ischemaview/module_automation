import os
from datetime import datetime
from configparser import ConfigParser
import yaml
import behave

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
os.environ["ROOT_DIR"] = ROOT_DIR

CONFIG_PATH = os.path.join(ROOT_DIR, 'test_env_config.yml')

with open(CONFIG_PATH) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    # print(data)

    sorted = yaml.dump(data, sort_keys=True)
    # print(sorted)

