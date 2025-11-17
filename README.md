<h1 align="center">Dev Container Features</h1>

<p align="center">
  <a href="https://github.com/e-gineering/devcontainer-features/blob/main/LICENSE"><img src="https://img.shields.io/github/license/e-gineering/devcontainer-features" alt="License"></a>
  <a href="https://github.com/e-gineering/devcontainer-features/actions"><img src="https://img.shields.io/github/actions/workflow/status/e-gineering/devcontainer-features/publish.yml" alt="Build Status"></a>
</p>

## Overview

This repository contains [Dev Container Features](https://containers.dev/implementors/features/) for use with Visual Studio Code Dev Containers, GitHub Codespaces, and other tools that support the Dev Container specification.

Dev Container Features are self-contained units of installation code and development container configuration. They are designed to be easily shared and reused across different projects.

## Quick Start

To use a feature from this collection, add it to your `.devcontainer/devcontainer.json` file:

```json
{
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
  "features": {
    "ghcr.io/e-gineering/devcontainer-features/rye:1": {}
  }
}
```

## Available Features

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

| Options Id | Description | Type | Default Value |
|-----|-----|-----|-----|
| bashCompletion | Enable bash completion for Rye | boolean | true |

#### Customizations

##### VS Code Extensions

- `ms-python.python`
- `tamasfe.even-better-toml`


<!-- END_FEATURES -->


## Contributing

Contributions are welcome! Whether you want to fix bugs, add new features, or improve documentation, we appreciate your help.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Test your changes locally (see Local Testing below)
5. Commit your changes with a clear commit message
6. Push to your branch (`git push origin feature/your-feature`)
7. Open a Pull Request

If you have any questions or need help, feel free to open an issue.

### Local Testing

To test features locally before publishing:

1. Create a symbolic link from your test project to your local repository:
   ```bash
   ln -s ~/dev/devcontainer-features .devcontainer/
   ```

2. Update your test project's `.devcontainer/devcontainer.json` to reference the local feature:
   ```json
   {
       "name": "Python",
       "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bookworm",
       "features": {
           // Comment out the published version:
           // "ghcr.io/e-gineering/devcontainer-features/rye:1": {}

           // Use the local version:
           "./devcontainer-features/src/rye": {}
       }
   }
   ```

3. Rebuild your dev container to test the changes

### Releasing

Version management and publishing are handled automatically:

1. **Version Numbering**: Update the `version` field in the feature's `devcontainer-feature.json` file
   - Follow [Semantic Versioning](https://semver.org): `MAJOR.MINOR.PATCH`
   - `MAJOR`: Breaking changes
   - `MINOR`: New features (backwards compatible)
   - `PATCH`: Bug fixes (backwards compatible)

2. **Automated Publishing**: On push to the `main` branch, GitHub Actions will:
   - Auto-generate README files
   - Build container images
   - Publish to GitHub Container Registry (GHCR)

## Resources

- [Dev Container Features Specification](https://containers.dev/implementors/features/)
- [Dev Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
