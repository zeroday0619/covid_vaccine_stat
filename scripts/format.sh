#!/bin/sh -e
set -x

isort covid_vaccine_stat tests --force-single-line-imports
autoflake --remove-all-unused-imports --recursive --remove-unused-variables covid_vaccine_stat tests --exclude=__init__.py
black covid_vaccine_stat tests
isort covid_vaccine_stat tests
