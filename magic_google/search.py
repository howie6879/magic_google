"""
    Created by howie.hu at 2021-12-18.
    Description: Magic google search.
    Changelog: all notable changes to this file will be documented
"""

import random
import sys
import time

import cchardet
import requests

from pyquery import PyQuery as pq

from magic_google.config import Config
from magic_google.utils import get_data, get_logger

if sys.version_info[0] > 2:
    from urllib.parse import parse_qs, quote_plus, urlparse
else:
    from urllib import quote_plus

    from urlparse import parse_qs, urlparse


requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning
)


class MagicGoogle:
    """
    Magic google search.
    """

    def __init__(self, proxies=None):
        self.config = Config
        self.logger = get_logger()
        self.domain_list = get_data(file_path=self.config.DOMAIN_PATH)
        self.ua_list = get_data(file_path=self.config.UA_PATH)
        self.proxies = random.choice(proxies) if proxies else None

    def search(self, query, language=None, num=None, start=0, pause=2):
        """Get the results you want, such as title,description,url

        Args:
            query (str): query content
            language (str, optional): query language. Defaults to None.
            num ([type], optional): Number of results per page. Defaults to None.
            start (int, optional): start result. Defaults to 0.
            pause (int, optional): pause time(s). Defaults to 2.]

        Yields:
            [type]: {}
        """
        content = self.search_page(query, language, num, start, pause)
        pq_content = pq(content)
        for p in pq_content.items("a"):
            if p.attr("href").startswith("/url?q="):
                pa = p.parent()
                if pa.is_("div"):
                    ppa = pa.parent()
                    if ppa.attr("class") is not None:
                        result = {}
                        result["title"] = p("h3").eq(0).text()
                        result["url_path"] = p("div").eq(1).text()
                        href = p.attr("href")
                        if href:
                            url = self.filter_link(href)
                            result["url"] = url
                        text = ppa("div").eq(0).text()
                        result["text"] = text
                        yield result

    def search_url(self, query, language=None, num=None, start=0, pause=2):
        """search url from page

        Args:
            query (str): query content
            language (str, optional): query language. Defaults to None.
            num ([type], optional): Number of results per page. Defaults to None.
            start (int, optional): start result. Defaults to 0.
            pause (int, optional): pause time(s). Defaults to 2.

        Yields:
            [type]: [url]
        """
        content = self.search_page(query, language, num, start, pause)
        pq_content = pq(content)

        for p in pq_content.items("a"):
            if p.attr("href").startswith("/url?q="):
                pa = p.parent()
                if pa.is_("div"):
                    ppa = pa.parent()
                    if ppa.attr("class") is not None:
                        href = p.attr("href")
                        if href:
                            url = self.filter_link(href)
                            yield url

    def search_page(self, query, language=None, num=None, start=0, pause=2):
        """Google search

        Args:
            query (str): query content
            language (str, optional): query language. Defaults to None.
            num ([type], optional): Number of results per page. Defaults to None.
            start (int, optional): start result. Defaults to 0.
            pause (int, optional): pause time(s). Defaults to 2.

        Returns:
            [str]: Content
        """
        query, domain = quote_plus(query), self.get_random_domain()
        if start > 0:
            url = self.config.URL_NEXT
            url = url.format(
                domain=domain,
                language=language,
                query=query,
                num=num,
                start=start,
            )
        else:
            if num is None:
                url = self.config.URL_SEARCH
                url = url.format(domain=domain, language=language, query=query)
            else:
                url = self.config.URL_NUM
                url = url.format(domain=domain, language=language, query=query, num=num)
        url = url.replace("hl=None&", "") if language is None else url
        # Add headers
        headers = {"user-agent": self.get_random_user_agent()}
        try:
            time.sleep(pause)
            r = requests.get(
                url=url,
                proxies=self.proxies,
                headers=headers,
                allow_redirects=False,
                verify=False,
                timeout=30,
            )
            content = r.content
            charset = cchardet.detect(content)
            text = content.decode(charset["encoding"])
            self.logger.info(url)
            return text
        except Exception as e:
            self.logger.exception(e)
            return None

    def get_random_user_agent(self):
        """Get a random user agent string.

        Returns:
            str: Random user agent string.
        """
        return random.choice(self.ua_list)

    def get_random_domain(self):
        """Get a random user agent string.

        Returns:
            str: Random domain string.
        """
        domain = random.choice(self.domain_list)
        if domain in self.config.BLACK_DOMAIN:
            self.get_random_domain()
        else:
            return domain

    def filter_link(self, link):
        """
        Returns None if the link doesn't yield a valid result.
        Token from https://github.com/MarioVilas/google

        Args:
            link ([str]): search href

        Returns:
            [str]: valid result
        """
        try:
            # Valid results are absolute URLs not pointing to a Google domain
            # like images.google.com or googleusercontent.com
            o = urlparse(link, "http")
            if o.netloc:
                return link
            # Decode hidden URLs.
            if link.startswith("/url?"):
                link = parse_qs(o.query)["q"][0]
                # Valid results are absolute URLs not pointing to a Google domain
                # like images.google.com or googleusercontent.com
                o = urlparse(link, "http")
                if o.netloc:
                    return link
        # Otherwise, or on error, return None.
        except Exception as e:
            self.logger.exception(e)
            return None
