## Description

In this sample api we will implement a simple hospital automation system as a simple REST api. 
We have departments, doctors, patients and rendezvous. For each components of this system we will implement CRUD operations 
and also we will implement some more custom endpoints as well.

## Installation
In order to install and start development, follow these steps.

1. Fork the repository.
2. Clone repository to your local machine.
3. Install Python 3.
4. Install Virtualenv (`$ pip3 install virtualenv`).
5. Create a new virtual environment for this project (`$ virtualenv api_venv`).
6. Activate the environment.
    * For Windows (`$ venv\Scripts\activate`).
    * For Unix (`$ source venv/bin/activate`).
7. Change folder to `sample_api/api`.
8. Install all dependencies to python environment (`$ pip3 install -r requirements.txt`).
9. Run Django server locally (`$ python3 manage.py runserver`).
10. If you don't get any error messages then server is running, visit `http://127.0.0.1:8000/`
11. You can browse around models in the admin panel, visit `http://127.0.0.1:8000/admin`
    * Username: `admin`
    * Password: `4dm1np4ss`
    * You can add new content or update contents via this panel.

## How to develop
For developing a new endpoint you can follow these steps.

1. First of all browse `http://127.0.0.1:8000/hospital/doctor/1`
    * This request returns us the information about the doctor with id 1.
    * Our task is creating new endpoints which are similar to this one.
2. There are two options to develop new functionality for this api
    * Implement a new method and register this method as endpoint. This can be done by following steps
        * Create a new method which similar to existing ones in the file `api/hospital/views.py`
        * After a method, implement some of the `GET`, `POST`, `PUT`, `DELETE` types of requests.
        * Register this new method in the file `api/hospital/urls.py`.
            * You may consult previous ones.
    * Implement a new type of request for existing method. This can be done by following steps
        * This type of development is simple than the previous one.
        * Implement some of the `GET`, `POST`, `PUT`, `DELETE` types of requests that are not exist.

## How to test
You can test your new endpoint with tools such as Postman or HTTPGet.

## More Info

1. You may require more information about [models of Django](https://docs.djangoproject.com/en/1.10/topics/db/models/)
to do some query on database or create new content.
2. You may need more information about [writing views](https://docs.djangoproject.com/en/1.10/topics/http/views/).
3. You may need to look into [Django](https://docs.djangoproject.com/en/1.10/).
