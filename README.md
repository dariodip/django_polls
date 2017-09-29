# django_pools
Just a useless try. I just wanted to try Python's channel and Django.

PS: This was my first project in Django and I know it's not perfect. When I'll have more time, I'll correct some bugs.
PPS: If you want to work on it, correct bugs, fork it, or something else, feel free :)

## Setup

## Requirements

1. [Python 3.5 (or higher)](https://www.python.org/);
2. [pip 7.0 (or higher)](https://pip.pypa.io/en/stable/);
3. [virtualenvironment 15.1.0 (or higher)](https://docs.python.org/3/library/venv.html).
4. [npm 3.10.9 (or higher)](https://www.npmjs.com/)

## Setup
In order to install django_polls and all his requirements you have to create a virtual environment using [venv](https://virtualenv.pypa.io/en/stable/) on Python 3.5.
To install *venv*, run the following:

`[sudo] pip3 install virtualenv` on Linux/MacOS
or
`pip install virtualenv` using prompt as administrator on Windows.

To create a virtual environment, in the main directory of the project run:

`virtualenv venv`.

To activate the virtual environment, in the main directory on the project run:

`source venv/bin/activate` on Linux/MacOS
or
`venv\Scripts\activate` on Windows.

You can check if the virtual environmnent is activate, checking if the command prompt has the prefix `(venv)`.

To install all the requirements, run the following:

`pip install -r requirements.txt`

This should install, using [pip](https://pypi.python.org/pypi/pip), all the [requirements](#requirements).

To setup front end, run

`npm install`.

## Run

Run

`source venv/bin/activate` on Linux/MacOS

or

`venv\Scripts\activate` on Windows.

Then

`python manage.py runserver`
