# Changelog

All notable changes to the Compiler will be documented in this file.
Note that these changes in this file are specifically for the Compiler.
The full summary will be in the CHANGELOG.md file the main folder 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

*Note that Documentation changes should not appear here!*

## Unreleased

### Added
- Automatic CLI installation on setup and addition to the path, so that the
  script can be easily run right after installing `parac_ext_cli`.

### Changed
- Renamed `cli_run_output_dir_validation()` to `cli_setup_output_dirs()`
- Renamed `cli_check_destination()` to `cli_setup_destination()`
- Updated `cli_setup_destination()` to have a more clear parameter and 
  instruction set for overwriting the default and prompting to the user.

### Removed

## [v0.1.dev7] - 2022-01-27

### Added
- New file `logging.py` responsible for graphical logging onto the console
- New additional helper command `paraproj` for setting up and configuring a 
  Para project, where unique commands may be run for compilation.
- New submodule `paralang_cli.scripts` for containing the main CLI and side
  CLI tools
- Banner Print function `utils.cli_print_paraproj_banner()` for printing the
  banner for the command `paraproj`

### Changed
- Renamed module `para_ext_cli` to `paralang_cli` and renamed all prefixes 
  to `para`
- Moved the graphical functions and classes from `parabase_cli.logging` to 
  `paralang_cli.logging` to allow the usage of graphical logging only in 
  combination with the CLI module. This also allows the usage of regular
  logging in the main module `paralang_base`

### Removed
- Unneeded command `para c-init`, as the configuration of the C compiler will
  be done from now on using the tool `paraproj`, which will allow project-wide
  configuration.

## [v0.1.dev6] - 2021-11-10

### Changed
- Deleted the file `entry_cli.py` in the main repo, and moved the function
  here. This function can now be called using `cli_run()`; This means that
  the main repo and module can only be run as module, and the CLI is a
  fully separate entity.
  
## [v0.1.dev5] - 2021-11-09

### Added
- Moved CLI from the main repo to its independent repo. Changes will appear
  from this version on here, as well as on the main repo.

[unreleased]: https://github.com/Para-Lang/Para-CLI/compare/v0.1.dev7...dev
[v0.1.dev7]: https://github.com/Para-Lang/Para-CLI/compare/v0.1.dev6...v0.1.dev7
[v0.1.dev6]: https://github.com/Para-Lang/Para-CLI/compare/v0.1.dev5...v0.1.dev6
[v0.1.dev5]: https://github.com/Para-Lang/Para-CLI/tag/v0.1.dev5
