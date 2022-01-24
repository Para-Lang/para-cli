# Changelog

All notable changes to the Compiler will be documented in this file.
Note that these changes in this file are specifically for the Compiler.
The full summary will be in the CHANGELOG.md file the main folder 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

*Note that Documentation changes should not appear here!*

## [Unreleased]

### Added
- New file `logging.py` responsible for graphical logging onto the console

### Changed
- Renamed module `parac_ext_cli` to `paralang_cli` and renamed all prefixes 
  to `para`
- Moved most of the graphical functionality from `para.logging` to 
  `para_ext_cli.logging` to allow both graphical and default logging.

### Removed
- Unneeded command `para c-init`, as 

## [v0.1.dev6]

### Changed
- Deleted the file `entry_cli.py` in the main repo, and moved the function
  here. This function can now be called using `cli_run()`; This means that
  the main repo and module can only be run as module, and the CLI is a
  fully separate entity.
  
## [v0.1.dev5]

### Added
- Moved CLI from the main repo to its independent repo. Changes will appear
  from this version on here, as well as on the main repo.

[unreleased]: https://github.com/Para-Lang/Para/compare/v0.1.dev6...dev
[v0.1.dev6]: https://github.com/Para-Lang/Para/compare/v0.1.dev5...v0.1.dev6
[v0.1.dev5]: https://github.com/Para-Lang/Para-CLI/tag/v0.1.dev5
