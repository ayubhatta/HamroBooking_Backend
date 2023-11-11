# install packages

    pip install -r requirements.txt

# Change Database CHARACTER

```bash
  ALTER DATABASE `database_name` CHARACTER SET utf8;
```

# Creating migrations

    python3 manage.py makemigrations
    python3 manage.py migrate
