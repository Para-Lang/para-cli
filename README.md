![](img/parac-banner.png)

# Para-C CLI
[![Build](https://img.shields.io/github/workflow/status/Para-C/Para-C/CodeQL?logo=github)](https://github.com/Para-C/Para-C-CLI/actions/workflows/codeql-analysis.yml)
[![Open Para-C issues](https://img.shields.io/github/issues/Para-C/Para-C)](https://github.com/Para-C/Para-C/issues)
[![PyPI version](https://badge.fury.io/py/parac-ext-cli.svg)](https://badge.fury.io/py/parac-ext-cli)
[![Documentation Status](https://readthedocs.org/projects/para-c/badge/?version=latest)](https://para-c.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/github/license/Para-C/Para-C-CLI?color=cyan)](https://github.com/Para-C/Para-C-CLI/blob/main/LICENSE)

[![Windows Test workflow](https://github.com/Para-C/Para-C-CLI/actions/workflows/pytest-win.yml/badge.svg)](https://github.com/Para-C/Para-C-CLI/actions/workflows/pytest-win.yml)
[![MacOS Test workflow](https://github.com/Para-C/Para-C-CLI/actions/workflows/pytest-macos.yml/badge.svg)](https://github.com/Para-C/Para-C-CLI/actions/workflows/pytest-macos.yml)
[![Linux Test & Coverage workflow](https://github.com/Para-C/Para-C-CLI/actions/workflows/cov-pytest.yml/badge.svg)](https://github.com/Para-C/Para-C-CLI/actions/workflows/pytest-linux.yml)
[![codecov](https://codecov.io/gh/Para-C/Para-C-CLI/branch/main/graph/badge.svg?token=8I9XL1E7QR)](https://codecov.io/gh/Para-C/Para-C)

Command Line Interface Implementation for the Para-C programming language

*For proper documentation and info on Para-C visit the main repo [here](https://github.com/Para-C/Para-C). 
This also includes issues or requesting changes. These should be done on the main branch, while the issues
here will be maintainers-only*

## Commands
*Commands displayed are mostly only partly implemented*

| Name                   | Description                                                                                      |
|------------------------|--------------------------------------------------------------------------------------------------|
| ``parac compile``      | Compiles a Para-C program to C or an executable.                                                 |
| ``parac run``          | Compiles a Para-C program and runs it.                                                           |
| ``parac c-init``       | Starts the CLI for the configuration of the C-compiler, which is required for running a program. |
| ``parac syntax-check`` | Validates the syntax of a Para-C program and logs errors if needed. (Pre-Processor ignored)      |
| ``parac analyse``      | Analyses a program and validates the syntax (Pre-Processor included - macros required)           |


## Installation

```bash
python3 -m pip install -U parac-ext-cli
```

*With specific version*:
```bash
python3 -m pip install -U parac-ext-cli==version
```

## Copyright and License

![License](https://img.shields.io/github/license/Para-C/Para-C?color=cyan)

Copyright (C) 2021 [Nicolas Klatzer*](#legal-name-which-does-not-match-the-preferred-and-commonly-used-name-luna-klatzer).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

See the [LICENSE](./LICENSE) for information on terms & conditions for usage.

###### *Legal name, which does not match the preferred and commonly used name Luna Klatzer
