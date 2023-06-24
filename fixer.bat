pipreqs --force

pip install -r requirements.txt

python -m black .

python -m isort .

ruff check . --fix
