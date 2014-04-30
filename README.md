# Rucksack
----------

Rucksack is a repository of [web components](http://www.w3.org/TR/components-intro/) and a tool to create and collect them.

## Environment Set Up (OS X)

### 1. Install Postgres

Head over to [http://postgresapp.com/](http://postgresapp.com/) and install the application then run it.

### 2. Set up your Python environment

Install the latest version of Python using [Homebrew](http://brew.sh/).

`brew update && brew install python`

Ensure you are using Homebrew's latest Python and not the OS X version.

`echo 'export PATH=/usr/local/bin:/usr/local/sbin:~/bin:$PATH' >> ~/.bash_profile`
`source ~/.bash_profile`

Update Setuptools and Pip:

`pip install --upgrade setuptools`
`pip install --upgrade pip`

Install and set up [virtualenv](https://pypi.python.org/pypi/virtualenv):

`pip install virtualenv virtualenvwrapper`
`echo 'export WORKON_HOME=~/.virtualenvs/' >> ~/.bash_profile`
`echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile`
`source ~/.bash_profile`
`mkdir -p $WORKON_HOME`
`mkvirtualenv rucksack-api`

Now, to switch to your new environment you can do `workon rucksack-api`.

3. Clone and run the project:

`git clone git@github.com:nrempel/rucksack-api.git`
