import requests

from utils.logger import logger


DEFAULT_TIMEOUT = 5


def safe_request(url):

    try:

        response = requests.get(
            url,
            timeout=DEFAULT_TIMEOUT
        )

        return response

    except requests.exceptions.Timeout:

        logger.error(f"Timeout while connecting to {url}")

        return None

    except requests.exceptions.SSLError:

        logger.error(f"SSL error for {url}")

        return None

    except requests.exceptions.RequestException as error:

        logger.error(f"Request failed for {url}: {error}")

        return None