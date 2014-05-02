# Rucksack

Rucksack is a repository of [web components](http://www.w3.org/TR/components-intro/) and a tool to create and collect them.  This is the API.

## API Resources

### users
---------

Available at */users*.

#### GET

Return a list of all users.

Example:
```json
[
  {
    "created": 1398900632,
    "email": "user@email.com",
    "id": 1,
    "username": "user"
  },
  ...
]
```

#### POST

Create a new user.

Request body:

```json
{
  "username": <username>,
  "email": <email address>
}
```

### web_components
------------------

Available at */web_components*

#### GET

Return a list of all web components.

Example:
```json
[
  {
    "created": 1398901345,
    "description": "This is a test component.",
    "id": 1,
    "name": "Test Component",
    "owner": {
      "created": 1398900632,
      "email": "user@email.com",
      "id": 1,
      "username": "user"
    },
    "repository_url": "https://github.com/username/test_component",
    "tags": []
  },
  ...
]
```

#### POST

Create a new web component.

Request body:
```json
{
  "name": <name>,
  "description": <description>,
  "owner": <username of existant user>,
  "repository_url": <relevant url>
}
```

### tags
--------

Available at */web_components/:id/tags*.

#### GET

Returns a list of all tags for the web component.

Example:
```json
[
  {
    "created": 1398901909,
    "id": 1,
    "name": "Test Tag"
  },
  ...
]
```

#### POST

Add a tag to the web component.

Request body:
```json
{
  "name": "Test Tag"
}
```

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

### 4. Run the Webserver:

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
