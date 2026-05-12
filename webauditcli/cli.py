import typer

from rich.console import Console
from rich.table import Table

from modules.headers import check_headers
from risk.severity import get_severity
from risk.scoring import calculate_risk

app = typer.Typer()
console = Console()


@app.command()
def scan(url: str):

    console.print(f"\n[bold cyan]Scanning[/bold cyan] {url}\n")

    findings = check_headers(url)

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

            table.add_row(
                finding,
                severity,
                str(risk["likelihood"]),
                str(risk["impact"]),
                str(risk["score"])
            )

        console.print(table)

    else:
        console.print(
            "[bold green][+] All security headers are present[/bold green]"
        )


if __name__ == "__main__":
    app()