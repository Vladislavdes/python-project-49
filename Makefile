install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user python3 -m pip install --user /usr/bin/python3

make lint:
	poetry run flake8 brain_games
