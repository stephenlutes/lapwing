import subprocess


def run() -> None:
    """Run the command line script to collect information and start the project."""
    project_name: str = input("Project name: ")

    subprocess.run(["wagtail", "start", project_name])
