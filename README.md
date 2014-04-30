# Rucksack
----------

Rucksack is a repository of [web components](http://www.w3.org/TR/components-intro/) and a tool to create and collect them.

## How to Setup the Server Locally (OS X)

### 1. Install Postgres

Download Postgres.app and run it from https://github.com/PostgresApp/PostgresApp/releases.

Add the Postgres.app utilities to your path:

```sh
echo 'export PATH="/Applications/Postgres.app/Contents/Versions/9.3/bin:$PATH"' >> ~/.bash_profile
```

### 2. Set up your Python environment

Install the latest version of Python using [Homebrew](http://brew.sh/).

```sh
brew update && brew install python
```

Ensure you are using Homebrew's latest Python and not the OS X version.

```sh
echo 'export PATH=/usr/local/bin:/usr/local/sbin:~/bin:$PATH' >> ~/.bash_profile
source ~/.bash_profile
```

Update Setuptools and Pip:

```sh
pip install --upgrade setuptools
pip install --upgrade pip
```

Install and set up [virtualenv](https://pypi.python.org/pypi/virtualenv):

```sh
pip install virtualenv virtualenvwrapper
echo 'export WORKON_HOME=~/.virtualenvs/' >> ~/.bash_profile
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile
source ~/.bash_profile
mkdir -p $WORKON_HOME
mkvirtualenv rucksack-api
```

**Now, to switch to your new environment you can do `workon rucksack-api`.**

### 3. Clone and Setup Project:

Clone the repository:

```sh
git clone git@github.com:nrempel/rucksack-api.git && cd rucksack-api
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

Initalize the database:

```sh
fab shell
```
```python
>>> db.create_all()
```

### 3. Run the Webserver:

```sh
fab run
```

## Available Fabric Commands

### run

*e.g., `fab run`*

Runs the webserver.

### shell

*e.g., `fab shell:local`* 

Runs a Python interactive shell in the given context.
