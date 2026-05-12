import typer

from rich.console import Console
from rich.table import Table

from modules.headers import check_headers
from risk.severity import get_severity

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

        for finding in findings:
            severity = get_severity(finding)
            table.add_row(finding, severity)

        console.print(table)

    else:
        console.print("[bold green][+] All security headers are present[/bold green]")


if __name__ == "__main__":
    app()