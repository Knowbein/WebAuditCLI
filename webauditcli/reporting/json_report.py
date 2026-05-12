import json


def generate_json_report(url, findings_data):

    high_count = 0
    medium_count = 0
    low_count = 0

    for item in findings_data:

        severity = item["severity"]

        if severity == "HIGH":
            high_count += 1

        elif severity == "MEDIUM":
            medium_count += 1

        else:
            low_count += 1

    report = {

        "target": url,

        "findings_count": len(findings_data),

        "high_severity": high_count,
        "medium_severity": medium_count,
        "low_severity": low_count,

        "findings": findings_data
    }

    with open("report.json", "w", encoding="utf-8") as report_file:

        json.dump(
            report,
            report_file,
            indent=4
        )