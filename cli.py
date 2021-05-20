from dataclasses import dataclass
from pathlib import Path

import click
from mypy import api
from rich.console import Console
from rich.table import Table


@dataclass
class Result:
    result: str
    error: str
    exit_code: int

DIRS = ["koans/py"]


def run_mypy(path: str):
    result, error, exit_code = api.run(
        [
            path,
            "--strict",
            "--disallow-any-expr",
            "--disallow-any-explicit",
            "--disallow-untyped-calls",
            "--disallow-untyped-defs",
            "--disallow-incomplete-defs",
            "--disallow-any-expr",
            "--pretty",
        ]
    )
    return Result(result=result, error=error, exit_code=exit_code)


def run_one(path):
    console = Console()
    console.rule("")
    console.print(f"Running mypy on koan file {path}")
    res = run_mypy(path)
    display_result(console, path, res, display="all")
    console.rule()


def display_summary(console: Console, run_result: dict[str, Result]):
    total = len(run_result)
    passed = sum(1 for r in run_result.values() if r.exit_code == 0)
    failed = total - passed

    table = Table(title="Koans Summary")
    table.add_column("Status")
    table.add_column("Count")

    table.add_row("Passed", str(passed))
    table.add_row("Failed", str(failed))

    console.print(table)


def display_result(console: Console, file_name: str, result: Result, display="all"):
    if display in ("all", "error") and result.exit_code != 0:
        console.rule(f"[bold] mypy errors in koan file {file_name}")
        if result.result:
            console.print(result.result)

        if result.error:
            console.print(result.error)

        console.rule("End")

    if display in ("all",) and result.exit_code == 0:
        console.print(f"No errors in koan file {file_name} :thumbsup: ")


############# Commands ####################


@click.group()
def cli():
    pass


@cli.command(help="Display summary of all koans")
@click.option("--display-error", default=False, is_flag=True)
def summary(display_error):
    console = Console()
    console.rule()
    dirs = DIRS
    run_result: dict[str, Result] = {}
    with console.status("Running mypy against all koan files ...", spinner="moon"):
        for directory in dirs:
            for py_file in sorted(Path(directory).rglob("*.py")):
                name = str(py_file)
                res = run_mypy(name)
                if res.exit_code == 0:
                    emoji_text = ":thumbsup:"
                else:
                    emoji_text = ":thumbsdown:"

                console.print(f"[bold] Ran mypy in koan file: {name} {emoji_text}")
                run_result[name] = res

    display_summary(console, run_result)
    if display_error:
        for file_name, result in run_result.items():
            display_result(console, file_name, result, display="error")

    console.rule()


@cli.command(help="Run one koan file")
@click.argument("path", required=True, type=click.Path())
def one(path):
    run_one(path)


@cli.command(help="List all the koans")
def list():
    console = Console()
    console.rule('Koan files')
    for directory in DIRS:
        for py_file in sorted(Path(directory).rglob("*.py")):
            console.print(py_file)
    console.rule('End')


if __name__ == "__main__":
    cli()
