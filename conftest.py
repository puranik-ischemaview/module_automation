import os
import pytest
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


# ---------------------------------------------------------------------------
# PYTEST FIXTURES:
# ---------------------------------------------------------------------------
@pytest.fixture(autouse=True)
def _annotate_environment(request):
    """Add project-specific information to test-run environment:
    * behave.version
    NOTE: autouse: Fixture is automatically used when test-module is imported.
    """
    # -- USEFUL FOR: pytest --html=report.html ...
    environment = getattr(request.config, "_environment", None)
    if environment:
        # -- PROVIDED-BY: pytest-html
        behave_version = behave.__version__
        environment.append(("behave", behave_version))


_pytest_version = pytest.__version__
if _pytest_version >= "5.0":
    # -- SUPPORTED SINCE: pytest 5.0
    @pytest.fixture(scope="session", autouse=True)
    def log_global_env_facts(record_testsuite_property):
        # SEE: https://docs.pytest.org/en/latest/usage.html
        behave_version = behave.__version__
        record_testsuite_property("BEHAVE_VERSION", behave_version)

# @pytest.fixture()
# def datatable():
#     return DataTable()
#
# class DataTable(object):
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         dt_str = ''
#         for field, value in self.__dict__.items():
#             dt_str = f'{dt_str}\n{field} = {value}'
#         return dt_str
#
#     def __repr__(self) -> str:
#         return self.__str__()


# test_config = ConfigParser()
# test_config.read("test_config.ini")
# with open("test_env_config.yml", "r") as ymlfile:
#     test_env_cfg = yaml.load(ymlfile)

# test_env_cfg = yaml.load("test_env_config.yml", Loader=yaml.FullLoader)
# print(test_env_cfg)

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     # to remove environment section
#     config._metadata = None
#
#     if not os.path.exists('reports'):
#         os.makedirs('reports')
#
#     config.option.htmlpath = 'reports/' + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
