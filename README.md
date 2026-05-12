# WebAuditCLI

WebAuditCLI is a modular web security auditing CLI tool built with Python.

It performs lightweight security analysis against web targets and generates structured findings, risk scores, and reports.

---

# Features

- Security Headers Analysis
- Basic Reflected XSS Detection
- Risk Scoring System
- Severity Classification
- Rich CLI Output
- HTML Report Generation
- JSON Report Export
- Centralized Logging
- Graceful Error Handling

---

# Technologies Used

- Python
- Typer
- Rich
- Requests
- Jinja2

---

# Screenshots

## CLI Output

![CLI Output](screenshots/cli-output.png)

## HTML Report

![HTML Report](screenshots/html-report.png)

---

# Installation

Clone repository:

```bash
git clone https://github.com/Knowbein/WebAuditCLI.git
cd WebAuditCLI
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Usage

python cli.py https://example.com
python cli.py https://example.com/?q=test # XSS
python cli.py https://example.com --html
python cli.py https://example.com --json
python cli.py https://example.com --html --json
python cli.py https://example.com --help

# Example Output

Security Findings

Finding                           Severity
------------------------------------------------
Missing CSP                       HIGH
Missing X-Frame-Options           MEDIUM
