# Product overview

Prenatal care, also known as antenatal care, is a type of preventive healthcare. Its goal is to provide regular check-ups that allow doctors or midwives to treat and prevent potential health problems throughout the course of the pregnancy and to promote healthy lifestyles that benefit both mother and child

Pre-natal-care app enables an expecting mother to make appointments with an near-by obstetrician-gynecologist incase she needs medical attention without having to make a call. Calls sometimes cause miscommunication due to language barrier or diffferences in accents. With this app, the expecting mother just needs to type and answer the different questions required to make an appointment.

### Prerequisites

Ensure that you have the following tools available on your machine;

- [Git](https://git-scm.com/) A distributed version control system
- [Python](https://www.python.org/) A general purpose programming language
- [Postgresql](https://www.postgresql.org/) An open source relational database
- A tool to create isolated Python environments preferably [Virtualenv](https://virtualenv.pypa.io/en/stable/)
- [Pip](https://pypi.org/project/pip/) A tool for installing python packages

### Installing

While in your preferred terminal;

Start by cloning the repository to your local machine

```bash
git clone https://github.com/Prenatal/prenatal-care-app-backend.git

cd prenatal-care-app-backend/
```

Make and activate a python virtual environment using `virtualenv`

```bash
virtualenv venv

source venv/bin/activate
```

With the virtual environment activated, install the project dependencies

```bash
pip3 install -r requirements.txt
```

## Database configuration

The project uses [Postgresql](https://www.postgresql.org/) database engine to persist data
and uses the default settings.

```json
{
  "DB_NAME": "pre-natal-care-db",
  "DB_USER": "postgres",
  "DB_HOST": "localhost",
  "DB_PORT": "5432",
  "DB_PASSWORD": ""
}
```

You can override the configuration key and value by setting a corresponding environment variable eg

```bash
# To overide the DB_NAME
export DB_NAME=prenatal-db
```

## Making migrations

The application migrations files are not pushed to github so you will have to generate them on your own.

After you have succeeded with the database setup, run the following commands


```bash
# Create the migrations from the applications models
python3 manage.py makemigrations

# Execute the generate migrations on the database .
python3 manage.py migrate
```

## Running the tests

Trigger the application tests by running

```bash
python3 manage.py tests
```

## Serving the application

You can start a local server by running

```bash
python3 manage.py runserver
```

## Database configuration

The project uses [Postgresql](https://www.postgresql.org/) database engine to persist data
and uses the default settings.


## Built With

- [Django](https://docs.djangoproject.com/en/2.1/) -A python web framework
- [Django REST Framework](https://maven.apache.org/) - A flexible toolkit for building Web APIs in Django

## Authors

See also the list of [contributors](https://github.com/Prenatal/prenatal-care-app-backend/graphs/contributors) who participated in this project.
