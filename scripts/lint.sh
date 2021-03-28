#!/usr/bin/env bash

set -e
set -x

mypy covid_vaccine_stat
flake8 covid_vaccine_stat
black covid_vaccine_stat --check
isort covid_vaccine_stat --check-only