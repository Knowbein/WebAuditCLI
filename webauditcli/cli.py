import typer

from rich.console import Console
from rich.table import Table

from modules.headers import check_headers
from risk.severity import get_severity
from risk.scoring import calculate_risk
from modules.xss import check_xss
from utils.logger import logger
from reporting.html_report import generate_html_report

app = typer.Typer()
console = Console()


@app.command()
def scan(url: str):

    console.print(f"\n[bold cyan]Scanning[/bold cyan] {url}\n")

    findings = []

    logger.info(f"Starting scan for {url}")

    findings.extend(check_headers(url))
    logger.info("Headers scan completed")

    findings.extend(check_xss(url))
    logger.info("XSS scan completed")

    logger.info("Scan finished")

    report_data = []

    if findings:

        table = Table(title="Security Findings")

        table.add_column("Finding", style="red")
        table.add_column("Severity", style="yellow")
        table.add_column("Likelihood")
        table.add_column("Impact")
        table.add_column("Risk Score")

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

            table.add_row(
                finding,
                severity,
                str(risk["likelihood"]),
                str(risk["impact"]),
                str(risk["score"])
            )

        console.print(table)
        generate_html_report(url, report_data)

        logger.info("HTML report generated")

    else:
        console.print(
            "[bold green][+] All security headers are present[/bold green]"
        )


if __name__ == "__main__":
    app()