from sauce_storage_api import SauceStorageApi
from os import getenv
import argparse

parser = argparse.ArgumentParser(description='Upload apps to Sauce Labs cloud to run automatic test')
parser.add_argument('app_path', metavar='APP_PATH', type=str,
                    help='Path to app file')
args = parser.parse_args()

sauce_api = SauceStorageApi(
    username=getenv("SAUCELABS_USERNAME"),
    access_key=getenv("SAUCELABS_ACCESS_KEY")
)
sauce_api.upload(args.app_path)