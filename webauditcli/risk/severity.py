SEVERITY_MAP = {
    "Content-Security-Policy": "HIGH",
    "Strict-Transport-Security": "MEDIUM",
    "X-Frame-Options": "MEDIUM",
    "Possible reflected XSS": "HIGH",
}


def get_severity(finding):
    for key in SEVERITY_MAP:
        if key in finding:
            return SEVERITY_MAP[key]

    return "LOW"