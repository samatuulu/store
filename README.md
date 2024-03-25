# Online Store API

A RESTfull API application for the online store with the basic managements between products, users, feedback, orders and etc.

## Getting Started

These instructions will get you run on your local machine for development and testing purposes.

### Prerequisites

1. Docker & Docker compose
2. Django & Django REST framework

### virtualenv(optional):
After installing virtualenv and activating it.</br>
Run requirements file in order to install all packages for project.
Command will be: `pip install -r requirements.txt` in the root directory.

#### Docker commands to run project:
Once, you are in a project root directory you can see the file `docker-compose.yml`
Let's build a project via docker.
- Build a project: `docker-compose up --build`
- or if you have all the Docker images, the `docker-compose up` command will be faster.
- You can also run basic django test via command: `docker-exec -it <container_id> bash`then, `cd` to project, finally, the command to run test is `python manage.py test`

Stay cool, stay safe! :)
Happy Coding!