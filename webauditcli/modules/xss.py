from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

import requests


TEST_PAYLOAD = "webaudit_test_payload"


def check_xss(url):

    findings = []

    parsed = urlparse(url)

    query_params = parse_qs(parsed.query)

    if not query_params:
        return findings

    for param in query_params:

        modified_params = query_params.copy()

        modified_params[param] = TEST_PAYLOAD

        new_query = urlencode(modified_params, doseq=True)

        test_url = urlunparse(
            (
                parsed.scheme,
                parsed.netloc,
                parsed.path,
                parsed.params,
                new_query,
                parsed.fragment
            )
        )

        try:

            response = requests.get(test_url, timeout=5)

            if TEST_PAYLOAD in response.text:

                findings.append(
                    f"Possible reflected XSS in parameter: {param}"
                )

        except requests.RequestException:
            continue

    return findings