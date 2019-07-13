#!/usr/bin/env bash

set -e

export PATH=env/bin:${PATH}

mdcal example/ output/ $@
