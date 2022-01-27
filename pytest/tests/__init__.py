# coding=utf-8
""" Init file for the core tests """
import os
import logging
import shutil
from pathlib import Path
from rich import get_console

from paralang_cli import cli_get_rich_console
from paralang_cli.logging import (cli_init_rich_console, cli_get_rich_console,
                                  cli_set_avoid_print_banner_overwrite)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('paralang_base')
logger.setLevel(logging.DEBUG)

cli_init_rich_console()
cli_set_avoid_print_banner_overwrite(True)

# prev default input function
prev_input = cli_get_rich_console().input


def resolve_test_path() -> Path:
    """
    Resolves the test path and tries to find the directory that contains the
    test files
    """
    p: Path = Path(os.getcwd()).resolve()
    if p.name == "pytest":
        return p
    elif os.path.exists(_ := p.joinpath("pytest")):
        p = _
    elif os.path.exists(_ := p.parent.joinpath("pytest")):
        p = _
    elif os.path.exists(_ := p.joinpath("src").joinpath("pytest")):
        p = _
    else:
        raise RuntimeError("Failed to resolve test path")

    return Path(str(p)).resolve()


BASE_TEST_PATH = resolve_test_path()


def overwrite_builtin_func_input(overwrite: str) -> None:
    """ Overwrites the input with a lambda that returns the specified value """
    cli_get_rich_console().input =\
        lambda *args, **kwargs: overwrite


def reset_input() -> None:
    """ Resets the output method of the console object """
    cli_get_rich_console().input = prev_input


def add_folder(folder_name: str) -> Path:
    """
    Removes any pre-existing data if it exists and adds the folder

    :returns: The path of the folder
    """
    remove_folder(folder_name)
    os.mkdir(p := BASE_TEST_PATH / folder_name)
    return Path(str(p)).resolve()


def remove_folder(folder_name: str) -> None:
    """ Removes the build and dist folder if they exist """
    path: Path = BASE_TEST_PATH / folder_name
    if os.path.exists(path):
        shutil.rmtree(str(path.resolve()))

    counter = 2
    while os.path.exists(path := BASE_TEST_PATH / f"{folder_name}_{counter}"):
        shutil.rmtree(str(path.resolve()))
        counter += 1


def create_test_file(folder_name: str, file_name: str) -> None:
    """ Creates a test file in the specified path with the specified name """
    with open(BASE_TEST_PATH / folder_name / file_name, 'w+') as file:
        file.write("x")
    assert os.path.exists(BASE_TEST_PATH / folder_name / file_name)


def overwrite_builtin_input(overwrite: str) -> None:
    """ Overwrites the input with a lambda that returns the specified value """
    cli_get_rich_console().input = lambda *args, **kwargs: overwrite
