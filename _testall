pushd $POET_POEM
rm -rf .venv
poetry install
poetry run pytest
popd
poet bats $POET_BIN/tests
