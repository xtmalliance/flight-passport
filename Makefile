# Linting commands
lint:
	ruff check . --fix

black:
	black .

cleanimports:
	isort .

# Run tests
testprep:
	docker exec -it flight_passport-web-1 python -m pip install --upgrade -r requirements_dev.txt

test: testprep
	docker exec -it flight_passport-web-1 pytest
