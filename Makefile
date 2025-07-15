#NEXUS_URL=http://
PY_DIRECTORIES=src/ tests/

.PHONY: install-editable
install-editable:
	uv sync --no-dev

.PHONY: install-dev-requirements
install-dev-requirements:
	uv sync

.PHONY: upgrade-lock-requirements
upgrade-lock-requirements:
	uv sync --upgrade

.PHONY: format
format:
	uv run ruff format ${PY_DIRECTORIES}
	uv run ruff check --fix ${PY_DIRECTORIES}

.PHONY: check-format
check-format:
	uv run ruff check ${PY_DIRECTORIES}
	uv run ruff format --check ${PY_DIRECTORIES}

.PHONY: check-typing
check-typing:
	uv run mypy ${PY_DIRECTORIES}

.PHONY: check-tests
check-tests:
	uv run pytest -v tests/unit/

.PHONY: check-it-tests
check-it-tests:
	uv run pytest -v tests/integration/

.PHONY: checks
checks: check-format check-typing check-tests check-it-tests

.PHONY: clean
clean:
	rm -rf ./.venv/
	rm -rf ./dist/

.PHONY: build
build:
	rm -rf ./dist/
	uv build

.PHONY: publish
publish:
	echo "package publishing not enabled"
	# uv publish --publish-url ${NEXUS_URL} \
	# 			--username ${NEXUS_USER} \
	# 			--password "${NEXUS_PASS}" \
	# 			./dist/
