import typer
from modules.headers import check_headers

app = typer.Typer()


@app.command()
def scan(url: str):
    typer.echo(f"Scanning {url}...\n")

    findings = check_headers(url)

    if findings:
        for finding in findings:
            typer.echo(f"[!] {finding}")
    else:
        typer.echo("[+] All security headers are present")


if __name__ == "__main__":
    app()