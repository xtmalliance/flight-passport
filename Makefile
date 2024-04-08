# Linting commands
lint:
	ruff check . --fix

black:
	black .

cleanimports:
	isort .
