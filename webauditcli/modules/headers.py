import requests

from utils.logger import logger


SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options"
]


def check_headers(url):

    findings = []

    try:

        response = requests.get(url, timeout=5)

        headers = response.headers

        for header in SECURITY_HEADERS:

            if header not in headers:

                findings.append(f"Missing {header}")

    except requests.RequestException as error:

        logger.error(f"Headers scan failed: {error}")

        findings.append(f"Connection error: {error}")

    return findings