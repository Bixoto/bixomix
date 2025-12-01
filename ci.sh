#! /bin/bash -ex
[ ! -f pyproject.toml ] && exit 0

COV_ARG=""

if [ -n "$HTMLCOV" ]; then
  COV_ARG="$COV_ARG --cov-report=html"
fi
if [ -n "$BRANCHCOV" ]; then
  COV_ARG="$COV_ARG --cov-branch"
fi

shopt -s globstar
poetry run mypy --strict --check-untyped-defs bixomix/**/*.py
#poetry run pytest --cov=app $COV_ARG tests/
