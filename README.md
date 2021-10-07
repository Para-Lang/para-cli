![para-c](img/parac-banner.png)

![Build](https://img.shields.io/github/workflow/status/Para-C/Para-C/CodeQL?logo=github)
[![PyPI version](https://badge.fury.io/py/parac_cli.svg)](https://badge.fury.io/py/parac_cli)
[![Documentation Status](https://readthedocs.org/projects/para-c/badge/?version=latest)](https://para-c.readthedocs.io/en/latest/?badge=latest)
![License](https://img.shields.io/github/license/Para-C/Para-C-CLI?color=cyan)
![Test workflow](https://github.com/Luna-Klatzer/Para-C-CLI/actions/workflows/python-test.yml/badge.svg)
[![codecov](https://codecov.io/gh/Para-C/Para-C-CLI/branch/main/graph/badge.svg?token=8I9XL1E7QR)](https://codecov.io/gh/Para-C/Para-C)

# Para-C CLI
Command Line Interface Implementation for the Para-C programming language

*For proper documentation and info on Para-C visit the main repo [here](https://github.com/Para-C/Para-C)*

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
python3 -m pip install -U parac_cli
```

*With specific version*:
```bash
python3 -m pip install -U parac_cli==version
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
