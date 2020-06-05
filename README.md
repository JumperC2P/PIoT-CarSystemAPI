# PIoT-CarSystemAPI

This is a part of the second assignment of Programming Internet of Things.

The project is for the **API** called by our web page.

**Author:** Hank Lee, Yiheng Liu, Yasin Li, Ting Lan.

## Brief Introduction

1. To start the project, as we use Pipenv to manage our environment, all the packages needed to be installed are recorded in Pipfile. It needs to run `pipenv install` first to install all the requied packages.
2. Under **unit_test** folder, there are the codes for unit testing of all the api provided in the project. We use `requests` to call those api to run these unit test. And also we use `socketio` to test the functionalities of sockets in the project.
3. The main program is `Car_System_Entry.py` under src folder. It can be easily started by running the command `python src/Car_System_Entry.py` or as we set **FLASK_APP** in `.flaskenv` it can be run by `flask run --host [ip_address]`
