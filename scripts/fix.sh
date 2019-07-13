#!/usr/bin/env bash

set -e

export PATH=env/bin:${PATH}

black setup.py mdcal
isort -rc setup.py mdcal
