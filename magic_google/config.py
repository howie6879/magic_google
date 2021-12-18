"""
    Created by howie.hu at 2021-12-18.
    Description: Magic Google's configuration
    Changelog: all notable changes to this file will be documented
"""

import os


class Config:
    """Global configuration"""

    BASE_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(BASE_DIR, "data")
    UA_PATH = os.path.join(DATA_DIR, "user_agents.txt")
    DOMAIN_PATH = os.path.join(DATA_DIR, "all_domain.txt")

    # google url configuration
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
    BLACK_DOMAIN = ["www.google.gf", "www.google.io", "www.google.com.lc"]
    # global uri
    DOMAIN = "www.google.com"
    URL_SEARCH = "https://{domain}/search?hl={language}&q={query}&btnG=Search&gbv=1"
    URL_NUM = URL_SEARCH + "&num={num}"
    URL_NEXT = URL_NUM + "&num={num}&start={start}"


import logging

# Define some constants

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
BLACK_DOMAIN = ["www.google.gf", "www.google.io", "www.google.com.lc"]

DOMAIN = "www.google.com"
URL_SEARCH = "https://{domain}/search?hl={language}&q={query}&btnG=Search&gbv=1"
URL_NUM = "https://{domain}/search?hl={language}&q={query}&btnG=Search&gbv=1&num={num}"
URL_NEXT = "https://{domain}/search?hl={language}&q={query}&btnG=Search&gbv=1&num={num}&start={start}"

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("chardet").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
LOGGER = logging.getLogger("magic_google")

if __name__ == "__main__":
    print(Config.DOMAIN_PATH)
