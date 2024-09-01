#NEXUS_URL=http://
PYTHON_VERSION ?= 3.12
PY_DIRECTORIES=src/ tests/

.PHONY: install-editable
install-requirements:
	uv sync --no-dev

.PHONY: install-dev-requirements
install-dev-requirements:
	uv sync

.PHONY: update-lock-requirements
update-lock-requirements:
	uv sync --upgrade

.PHONY: format
format: install-dev-requirements
	uv run ruff check --fix ${PY_DIRECTORIES}
	uv run ruff format ${PY_DIRECTORIES}	

.PHONY: check-tests
check-tests: install-dev-requirements
	uv run pytest -v -s

.PHONY: check-format
check-format: install-dev-requirements
	uv run ruff check ${PY_DIRECTORIES}
	uv run ruff format --check ${PY_DIRECTORIES}

.PHONY: check-typing
check-typing: install-dev-requirements
	.venv/bin/mypy ${PY_DIRECTORIES}

.PHONY: checks
checks: check-format check-typing check-tests

.PHONY: clean
clean:
	rm -rf ./.venv/
	rm -rf ./dist/

.PHONY: build
build:
	rm -rf ./dist/
	uvx --from build pyproject-build --installer uv

.PHONY: publish
publish:
	echo "package publishing not enabled"
#	uvx twine upload --repository-url ${NEXUS_URL} \
#				 -u ${NEXUS_USER} \
#				 -p "${NEXUS_PASS}" \
#				 dist/*
