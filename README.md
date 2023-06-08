# FlaskProj


## Technical Requirements
- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtual environment](https://docs.python.org/3/library/venv.html)
- [MongoDB](https://www.mongodb.com/try/download/community).


## Installation
Write these commands in terminal

1. create virtual environment

For Windows run:
```sh
py -m pip install --upgrade pip

py -m pip --version

py -m pip install --user virtualenv

py -m venv flask_env

.\flask_env\Scripts\activate
```


For Unix/macOS run:
```sh
python3 -m pip install --user --upgrade pip

python3 -m pip --version

python3 -m pip install --user virtualenv

python3 -m venv flask_env

source flask_env/bin/activate

```
2. Install requirements:
```sh
pip install -r requirements.py

```

3. Run command in terminal:
```sh
flask --app run.py run

```

