# Django-Product-Listing-app

A simple Product Listing Application in Python-Django displaying all product information includes Product Name, Price and Quantity. It provides you feature to add new products, search product and inline editing of product information.

# Steps to setup Project on local-

**Step 1** - Clone the repository using git clone.

```git clone { url }```

**Step 2** - Create virtual environment using below commands-

```virtualenv venv```

**Step 3**- Activate Virtual environment using below command-

```.\venv\Scripts\activate```

**Step 4** - Install project dependencies-

```pip install -r requirements.txt```

**Step 5**- Create postgres Database on PgAdmin

**Step 6** - Create .env file in the products folder with help of sample_env_file.txt and add all the config settings in .env file

**Step 7** - Execute below commands to migrate the Database-

```python manage.py makemigrations```

```python manage.py sqlmigrate table 0001```

```python manage.py migrate```

**Step 8** - Start the server using below command-

```python manage.py runserver```


