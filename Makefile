install:
	uv sync

gendiff:
	uv run gendiff

lint:
	uv run ruff check

build:
	uv build
	
package-install:
	uv tool install dist/*.whl
