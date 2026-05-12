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

        from utils.network import safe_request
        response = safe_request(url)
        if response is None:
            findings.append("Failed to retrieve headers")
            return findings

        headers = response.headers

        for header in SECURITY_HEADERS:

            if header not in headers:

                findings.append(f"Missing {header}")

    except requests.RequestException as error:

        logger.error(f"Headers scan failed: {error}")

        findings.append(f"Connection error: {error}")

    return findings