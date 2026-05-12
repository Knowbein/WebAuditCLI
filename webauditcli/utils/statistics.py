def calculate_statistics(report_data):

    stats = {

        "total": len(report_data),

        "high": 0,
        "medium": 0,
        "low": 0
    }

    for item in report_data:

        severity = item["severity"]

        if severity == "HIGH":
            stats["high"] += 1

        elif severity == "MEDIUM":
            stats["medium"] += 1

        else:
            stats["low"] += 1

    return stats