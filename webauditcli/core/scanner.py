from modules.headers import check_headers
from modules.xss import check_xss

from risk.severity import get_severity
from risk.scoring import calculate_risk


def run_scan(url):

    findings = []

    findings.extend(check_headers(url))
    findings.extend(check_xss(url))

    report_data = []

    for finding in findings:

        severity = get_severity(finding)

        risk = calculate_risk(finding)

        report_data.append({

            "finding": finding,

            "severity": severity,

            "likelihood": risk["likelihood"],

            "impact": risk["impact"],

            "score": risk["score"]
        })

    return report_data