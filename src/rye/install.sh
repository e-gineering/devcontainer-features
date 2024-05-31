#!/bin/sh

# Exit immediately on error
set -o errexit

echo "Activating feature 'rye'"

# https://rye.astral.sh/guide/installation/#customized-installation
curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash

if [ "$BASHCOMPLETION" == "true" ]; then
  echo "Activating bash completion for 'rye'"
  # https://rye.astral.sh/guide/installation/#shell-completion
  rye self completion > /etc/bash_completion.d/rye
fi
