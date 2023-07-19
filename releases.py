import requests
from scrapy import Selector
from lxml.html import fromstring
import os
from dotenv import load_dotenv

load_dotenv()

WORPRESS_RELEASES = os.getenv('WORPRESS_RELEASES')

def releases():
    """
    The function `releases` retrieves the latest WordPress core version from a website and returns it as
    a list of strings.
    :return: the core version of the WordPress releases. If there are no releases yet, it will return
    "No release yet". If there is an error, it will return "error".
    """
    try:
        url = WORPRESS_RELEASES

        response = requests.get(url)

        html = Selector(text=response.text)

        quotes_html = html.css(".wp-block-wporg-release-version").extract()

        core_version = ''

        if not quotes_html:
            core_version = 'No release yet'
        else:
            core_version = []
            for x in quotes_html:
                core_version.append(fromstring(x).text_content().strip())

        return (core_version)
    except NameError:
        return ("error")
    