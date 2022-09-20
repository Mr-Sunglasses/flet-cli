#! /usr/bin/env python3
import os
import time
from typing import Optional
import typer


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


def runner():
    if os.path.isdir("src"):
        try:
            os.system("pip3 install -r requirements.txt")
            os.chdir("src")
            os.system("python3 main.py")
        except:
            print("ERROR")
    else:
        print("No src folder found")


# CLI EXECUTION

app = typer.Typer()


@app.command()
def create(name: str):
    start_time = time.time()
    project_creator(Project_name=name)
    end_time = time.time()
    print("\n")
    print(f"All done! in {end_time - start_time}ms")
    print("In order to run your application, type:")
    print("\n")
    print(f"$ cd {name}")
    print("\n")
    print("$ flet run")
    print("\n")
    print(f"Your application code is in {name}/src/main.py")


@app.command()
def run():
    runner()


if __name__ == "__main__":
    app()
