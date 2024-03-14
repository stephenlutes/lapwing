import subprocess
from pathlib import Path


def run() -> None:
    """Run the command line script to collect information and start the project."""
    project_name: str = input("Project name: ")

    template_path: Path = Path(__file__).parent / "project_template"

    subprocess.run(
        ["wagtail", "start", "--template=" + str(template_path), project_name]
    )
