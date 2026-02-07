.DEFAULT_GOAL := all

.PHONY: install
install: ## Install dependencies
	uv sync --all-extras

.PHONY: format
format: ## Format code
	uv run ruff format
	uv run ruff check --fix

.PHONY: lint
lint: ## Lint code
	uv run ruff check
	uv run pyright
	uv run mypy app

.PHONY: test
test: ## Run tests
	uv run pytest

.PHONY: run
run: ## Run local server
	uv run uvicorn app.main:app --reload

.PHONY: all
all: format lint test