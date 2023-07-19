import requests
import os
from dotenv import load_dotenv

load_dotenv()

SITE_URL = os.getenv('SITE_URL')
API_KEY = os.getenv('API_KEY')


def score():
    """
    The function retrieves the First Interactive score from the Google PageSpeed Insights API for a
    given URL.
    :return: a dictionary with a key 'response' and a value that depends on the execution of the code.
    If there is a NameError, the value will be "error". Otherwise, the value will be the value of the
    'urlfi' variable, which represents the 'First Interactive' metric.
    """
    try:
        url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&key={}'.format(SITE_URL, API_KEY)
        response = requests.get(url)
        requestJson = response.json()
        urlid = requestJson['id']
        split = urlid.split('?')
        urlid = split[0]
        ID = f'URL ~ {urlid}'
        ID2 = str(urlid)
        urlfcp = requestJson['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
        FCP = f'First Contentful Paint ~ {str(urlfcp)}'
        FCP2 = str(urlfcp)
        urlfi = requestJson['lighthouseResult']['audits']['interactive']['displayValue']
        FI = f'First Interactive ~ {str(urlfi)}'
        FI2 = str(urlfi)
        return {'response': FI2}
    except NameError:
        return  {'response': "error"}