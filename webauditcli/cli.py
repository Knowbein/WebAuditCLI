import typer

app = typer.Typer()

@app.callback()
def main():
    """
    Web Audit CLI
    """
    pass

@app.command()
def scan(url: str):
    typer.echo(f"Scanning {url}...")

if __name__ == "__main__":
    app()