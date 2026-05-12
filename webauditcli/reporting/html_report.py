from jinja2 import Template


HTML_TEMPLATE = """
<html>
<head>
    <title>WebAuditCLI Report</title>

    <style>
        body {
            font-family: Arial;
            margin: 40px;
        }

        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            border: 1px solid black;
            padding: 10px;
        }

        th {
            background-color: #eeeeee;
        }
    </style>
</head>

<body>

    <h1>WebAuditCLI Report</h1>

    <p><strong>Target:</strong> {{ url }}</p>

    <table>

        <tr>
            <th>Finding</th>
            <th>Severity</th>
            <th>Likelihood</th>
            <th>Impact</th>
            <th>Risk Score</th>
        </tr>

        {% for item in findings %}

        <tr>
            <td>{{ item.finding }}</td>
            <td>{{ item.severity }}</td>
            <td>{{ item.likelihood }}</td>
            <td>{{ item.impact }}</td>
            <td>{{ item.score }}</td>
        </tr>

        {% endfor %}

    </table>

</body>
</html>
"""


def generate_html_report(url, findings_data):

    template = Template(HTML_TEMPLATE)

    html_content = template.render(
        url=url,
        findings=findings_data
    )

    with open("report.html", "w", encoding="utf-8") as report_file:

        report_file.write(html_content)