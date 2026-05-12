import typer

from rich.console import Console
from rich.table import Table

from core.scanner import run_scan

from reporting.html_report import generate_html_report
from reporting.json_report import generate_json_report

from utils.logger import logger


app = typer.Typer()
console = Console()


@app.command()
def scan(

    url: str,

    html: bool = typer.Option(
        False,
        "--html",
        help="Generate HTML report"
    ),

    json_output: bool = typer.Option(
        False,
        "--json",
        help="Generate JSON report"
    )
):

    console.print(f"\n[bold cyan]Scanning[/bold cyan] {url}\n")

    logger.info(f"Starting scan for {url}")

    report_data = run_scan(url)

    table = Table(title="Security Findings")

    table.add_column("Finding", style="red")
    table.add_column("Severity", style="yellow")
    table.add_column("Likelihood")
    table.add_column("Impact")
    table.add_column("Risk Score")

    for item in report_data:

        table.add_row(
            item["finding"],
            item["severity"],
            str(item["likelihood"]),
            str(item["impact"]),
            str(item["score"])
        )

    console.print(table)

    if html:

        generate_html_report(url, report_data)

        logger.info("HTML report generated")

    if json_output:

        generate_json_report(url, report_data)

        logger.info("JSON report generated")

    logger.info("Scan finished")


if __name__ == "__main__":
    app()