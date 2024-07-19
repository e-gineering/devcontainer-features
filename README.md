<h1 align="center">Dev Container Features</h1>

## Features

<!-- START_FEATURES -->

### Rye (rye)

A Hassle-Free Python Experience

#### Example Usage

```json
"features": {
    "ghcr.io/e-gineering/devcontainer-features/rye:1": {}
}
```

#### Options

| Options Id     | Description                    | Type    | Default Value |
| -------------- | ------------------------------ | ------- | ------------- |
| bashCompletion | Enable bash completion for Rye | boolean | true          |

#### Customizations

##### VS Code Extensions

- `ms-python.python`
- `tamasfe.even-better-toml`


<!-- END_FEATURES -->


## Contributing

Bugfixes and features are welcome! If you have any questions feel free to open an issue as well.

## Local testing

To do local testing, I've been going to a project that consumes this feature, and making a soft link to make `.devcontainer/devcontainer-features` in the consuming project link to my local `devcontainer-features` repo where I've made changes that I need to now test.

```
ln -s ~/dev/devcontainer-features .devcontainer/
```

Then in your consuming project's `.devcontainer/devcontainer.json`, you can then refer to it like:

```json
{
    "name": "Python",
    "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bookworm",
    "features": {
        // "ghcr.io/e-gineering/devcontainer-features/rye:1": {}
        "./devcontainer-features/src/rye": {}
    }
}
```

## Releasing

The version numbers are set by manually changing the `version` option in each `devcontainer-feature.json` file. Please feel free to bump the version number when making a change, and try to follow [semver](https://semver.org) (`major.minor.bugfix`) to not unexpectedly break the feature for people using it.

On any push to the `main` branch, several Github Actions will auto-generate the readme files, build, and then publish the container images to Github Container Registry.
