#!/bin/sh

# Exit immediately on error
set -o errexit

echo "Activating feature 'rye'"

# https://rye.astral.sh/guide/installation/#customized-installation
curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash
