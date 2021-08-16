[![Build Status](https://travis-ci.com/MaewenPell/trailing-planner.svg?branch=master)](https://travis-ci.com/MaewenPell/trailing-planner)


![Trailing Planner Logo](https://github.com/MaewenPell/trailing-planner/blob/master/staticfiles/assets/logo_no_bg.png)


# trailing-planner

Trailing Planner is an online community about passionate runners, determined to train hard and push themselve beyonds their own limits.
A good and clever preparation is the key to success for reaching your goals.

There is no shortcuts, only work.

Production link : 

https://trailing-planner.herokuapp.com/

## Installing / Getting started

A quick introduction of the minimal setup you need to get a hello world up &
running.

### Before starting

Make sure that you have a version 3.9 of python installed.

```bash
git clone https://github.com/MaewenPell/trailing-planner.git
```

```bash
pip install -r requirements.txt
```

```bash
export DJANGO_SECRET_KEY="CREATE SECRET KEY"
```

```bash
./manage.py runserver
```

You are now on the local version of trailing-planner.

### Deploying / Publishing

The CI will run the differents test, if they are all green we could safely merge the additionals features


## Features

This project is in a WIP status, for now we can
* Create an account
* Register a primary goal with the distance and the elevation gain
* Register differents types of trainings including the distance, and the elevation
* The app will compute these trainings into a nice graph that permit a clear overwiew 
* It will compute the weekly status, the monthly status and the gloabal status.
* For the three best athletes a wall of fame is available at the sight of everyone


## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

This repository is following the PEP8 style guide for python. There is no auto linting at the moment in the CI but please make sure that you'll follow these rules.

## Links


- Project homepage: https://trailing-planner.herokuapp.com/
- Repository: https://github.com/MaewenPell/trailing-planner
- Issue tracker: https://github.com/MaewenPell/trailing-planner/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    me directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!

## Licensing

One really important part: Give your project a proper license. Here you should
state what the license is and how to find the text version of the license.
Something like:

"The code in this project is licensed under MIT license."