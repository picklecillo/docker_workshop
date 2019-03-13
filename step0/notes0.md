# Step 0

Ej app flask.
Para esta primera etapa vamos a levantar la app en local usando un virtualenv.

## Virtualenv

### CMDs

```bash
brew update
brew install pyenv pyenv-virtualenv

pyenv install 3.6.8
pyenv global 3.6.8
python -V
```

### Profile

```bash
...
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PATH="$PYENV_ROOT/shims:$PATH"
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi

if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

#Virtualenv
VIRTUALENVWRAPPER_PYTHON=/Users/lagaelespinosa/.pyenv/versions/3.6.8/bin/python
export PIP_REQUIRE_VIRTUALENV=true
gpip(){
  PIP_REQUIRE_VIRTUALENV="" pip "$@"
}

export WORKON_HOME=$HOME/.virtualenvs
pyenv virtualenvwrapper_lazy
```

## Run app

```bash
FLASK_APP=app/app.py flask run
```
