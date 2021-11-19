# coding=utf-8
""" Utilities for the parac_ext_cli module """
import os
import shutil
from os import PathLike
from pathlib import Path
from typing import Union, Tuple

try:
    import parac
except ImportError as e:
    raise ImportError("Failed to locate parent module 'parac'") from e
else:
    from parac import UserInputError
    from parac.util import abortable, decode_if_bytes
    from parac.logging import get_rich_console as console

__all__ = [
    "cli_err_dir_already_exists",
    "cli_setup_output_dirs",
    "cli_setup_destination",
    "cli_resolve_path"
]


def cli_resolve_path(path: Union[bytes, str, Path, PathLike]) -> str:
    """
    If the path is a pathlib.Path it will resolve it, including all symlinks
    and return it as a string, else it will be passed through decode_if_bytes,
    made to a pathlib.Path to resolve all symlinks and then returned as a
    string

    :raise UserInputError: If the inserted path can not be resolved due to an
    invalid format
    """
    if str(path).strip() == "":
        raise UserInputError("Path can not be empty")
    if type(path) in (bytes, str, PathLike):
        try:
            path = Path(decode_if_bytes(path))
        # pathlib.Path raised error -> Invalid path
        except Exception as e:
            raise UserInputError("Path is in an invalid format") from e
    return str(path.resolve())


@abortable(step="Validating Output", reraise=True)
def cli_err_dir_already_exists(folder: Union[str, PathLike]) -> bool:
    """
    Asks the user whether the build folder should be overwritten

    :returns: True if "yes" and False if "no"
    """
    _input = console().input(
        f"[bright_yellow] > [bright_white]The {folder} "
        "folder already exists. Overwrite data? If no, a new directory will "
        "be created (y\\N): "
    ).lower() in ('y', 'yes')
    return _input


def cli_setup_destination(
        dir_name: str,
        default_path: Union[str, PathLike],
        prompt_user: bool,
        overwrite: bool,
        work_dir: Path = Path(os.getcwd())
) -> Path:
    """
    Validates the destination and checks whether the specified output
    folder is available. If the folder already exists and prompt_user was
    set to true it will show a prompt to the user what should be done
    about the existing folder.

    It will not overwrite the data per default

    :param dir_name: The name of the directory
    :param default_path: The default path/destination where the directory
     should exist
    :param prompt_user: If set to True, it will prompt the user in case the
     folder already exists
    :param overwrite: If set to True, it will always overwrite the data, even
     if prompt_user is set to True
    :param work_dir: The working directory where the folder should be created.
    :returns: The path to the folder
    """
    output = default_path
    if not os.path.exists(output):
        # create and done!
        os.mkdir(output)
    elif len(os.listdir(output)) > 0:
        # If the overwrite is set to False then a prompt will appear
        if prompt_user and not overwrite:
            ret: bool = cli_err_dir_already_exists(dir_name)
        else:
            ret: bool = False

        # if the user said yes it should be overwritten
        # if no prompt was asked default to
        if overwrite or ret or not prompt_user:
            # removing everything and creating it again
            shutil.rmtree(output)
            os.mkdir(output)
        else:
            # create a directory that does not match this name by creating a
            # unique number identifier for it
            counter = 2
            while os.path.exists(work_dir / f"{dir_name}_{counter}"):
                counter += 1
            output = work_dir / f"{dir_name}_{counter}"
            os.mkdir(output)

    return Path(output).resolve()


def cli_setup_output_dirs(
        overwrite_build: bool,
        overwrite_dist: bool,
        work_dir: Union[str, PathLike, Path] = os.getcwd()
) -> Tuple[Path, Path]:
    """
    Sets up the output directories, by validating whether the output folder
    /build/ and /dist/ can be used and creates a prompt if one of the folder
    already exists

    :param overwrite_build: If set to True if a build folder already exists
     it will be deleted and overwritten
    :param overwrite_dist: If set to True if a dist folder already exists
     it will be deleted and overwritten
    :param work_dir: Work Directory that should be used for the check
    """
    from parac import const

    build_path = cli_setup_destination(
        "build",
        default_path=const.DEFAULT_BUILD_PATH,
        prompt_user=True,
        overwrite=overwrite_build,
        work_dir=work_dir
    )
    dist_path = cli_setup_destination(
        "dist",
        default_path=const.DEFAULT_DIST_PATH,
        prompt_user=True,
        overwrite=overwrite_dist,
        work_dir=work_dir
    )
    return build_path, dist_path
