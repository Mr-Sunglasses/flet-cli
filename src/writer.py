import os
from typing import Optional


def create_new_file_folder(appName: str):
    """
    :param appName: Name of Your app that you want to create
    :return: Project file
    """
    os.mkdir("src")
    with open(
        "/Users/anton/Desktop/Development/Python/fleet-create-app/templates/main.template",
        "r",
    ) as f, open("src/main.py", "w") as fw:
        for line in f:

            fw.write(line)


def create_git_ignore():

    with open(
        "/Users/anton/Desktop/Development/Python/fleet-create-app/templates/gitignore.template",
        "r",
    ) as f, open(".gitignore", "w") as fw:
        for line in f:

            fw.write(line)


def create_requirements():

    with open(
        "/Users/anton/Desktop/Development/Python/fleet-create-app/templates/requirements.template",
        "r",
    ) as f, open("requirements.txt", "w") as fw:
        for line in f:

            fw.write(line)


def create_license():
    with open(
        "/Users/anton/Desktop/Development/Python/fleet-create-app/templates/LICENSE.template",
        "r",
    ) as f, open("LICENSE", "w") as fw:
        for line in f:
            fw.write(line)


def create_readme(appName: str):
    with open(
        "/Users/anton/Desktop/Development/Python/fleet-create-app/templates/README.template",
        "r",
    ) as f, open("README.md", "w") as fw:
        fw.write(f"# {appName}")
        fw.write("\n")

        for line in f:
            fw.write(line)


def project_creator(Project_name: str):

    os.mkdir(f"{Project_name}")
    os.chdir(f"{Project_name}")
    create_new_file_folder(appName=Project_name)
    create_git_ignore()
    create_requirements()
    create_readme(appName=Project_name)
    create_license()
