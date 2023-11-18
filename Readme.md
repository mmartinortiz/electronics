# Electronic projects

Multiple electronic projects with (or without) MicroControllers

## Development

For managing the different programs and libraries used for my electronic projects, I use [DevBox](https://www.jetpack.io/devbox). For [installing DevBox](https://www.jetpack.io/devbox/docs/quickstart/#install-devbox) run:

```bash
curl -fsSL https://get.jetpack.io/devbox | bash
```

Once installed, just execute `devbox shell` to get into a Shell with all the programs a libraries you need. Within this DevBox Shell, you can still use your favourite IDEs.

## How to

- Upload a file to the Pico, and make it be run on boot

```shell
rshell cp program.py /pyboard/main.py
```
