# **Web shop on django, just pet-project**

## Well we have next system of website:
____
- / - main page **WoW**
- /login/ login page **WoW AMAZING**
- /registration/ - registration page
- /about/ - page with information about us
- /privacy/ - page with privacy politics
- /product/ - page with goods list
- /product/X - page with detail informationabout goods, where X = integer number
- /product_api/ - page with goods but in API vision
- /product_api/X - page with detail information about goods, where X = integer number, but in API vision
- /swagger/ - well on this page you can test HTTP requests for API system (made by drf-yasg)
- /redoc/ - documentation for API made by (drf-yasg)
____
## How install it on locale machine
- deploy postgresql
- pip install -r requirements.txt or /path/to/requirements.txt (if tou change folder for requirements)
- python manage.py makemigrations (if tou delete our DB)
- pythom manage.py migrate
- python manage.py runserver

## How it looks?
____
# Work in progress
