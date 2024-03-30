# Electronic projects

Multiple electronic projects with (or without) MicroControllers

## Development

For managing the different programs and libraries used for my electronic projects, I use [DevBox](https://www.jetpack.io/devbox). For [installing DevBox](https://www.jetpack.io/devbox/docs/quickstart/#install-devbox) run:

```bash
curl -fsSL https://get.jetpack.io/devbox | bash
```

Once installed, just execute `devbox shell` to get into a Shell with all the programs a libraries you need. Within this DevBox Shell, you can still use your favourite IDEs.

The following programs are available in your DevBox shell:

- [Thonny](https://thonny.org/)
- [ESPTool](https://github.com/espressif/esptool)
- Python 3.11.
- [Ruff](https://www.ruff.io/), for code formatting.
- [rshell](https://github.com/dhylands/rshell), for remote execution of Python files.
- [pre-commit](https://pre-commit.com/), for making sure that committed files look nice.
- poetry, for managing a Python Virtual environment with the project libraries.
- [Poetry](https://python-poetry.org/), for managing a Python Virtual environment with the project libraries.

## How to

- Upload a file to the Pico, and make it be run on boot

```shell
rshell cp program.py /pyboard/main.py
```
