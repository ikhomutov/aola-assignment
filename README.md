# feedly

## Requirements

- Python 3.10

## Installation

### Create virtual environment

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### Install required python packages

```bash
pip install -r requirements/dev.txt
```

### Create user and database for a project
```sql
CREATE USER feedly WITH PASSWORD 'feedly';
CREATE DATABASE feedly WITH OWNER feedly;
```

### Create app.env file and fill it with appropriate parameters
```bash
cp app.env.example app.env
```

### Run migrations
```bash
python manage.py migrate
```

### Optional: load fixtures
```bash
python manage.py loaddata fixtures.json
```

### Run server
```bash
python manage.py runserver
```

## API
For learning exposed API please refer to a [specification](./openapi.yaml)