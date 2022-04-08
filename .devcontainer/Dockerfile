# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.224.2/containers/ubuntu/.devcontainer/base.Dockerfile

# [Choice] Ubuntu version (use hirsuite or bionic on local arm64/Apple Silicon): hirsute, focal, bionic
ARG VARIANT="hirsute"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends python3.9-venv

RUN curl -sSL https://install.python-poetry.org | python3.9 - --version=1.1.13
