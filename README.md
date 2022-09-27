# Medina Tech Limited Assignment

Clone the project\
`git clone https://github.com/rkshaon/medina-tech-limited-assignment.git`

Change directory\
`cd medina-tech-limited-assignment`

Create virtual environment in Linux\
`python -m venv env`

Activate virtual environment in Linux\
`source env/bin/activate`

Install dependency\
`pip install -r requirements.txt`

Run the server\
`python manage.py runserver`

## APIs

**Registration**\
*URL* : `BASE-URL/user/registration`\
*Method*: `POST`\
*Data*:\
Role 1 - Admin, 2 - Vendor, 3 - Customer\
`{
    "name": "Rezaul Karim Shaon",
    "username": "rkshaon",
    "email": "rkshaon.ist@gmail.com",
    "password": "12345678",
    "role": "1"
}`\
*Response*: you'll get a response message with status `True` or `False`

**Login**\
*URL* : `BASE-URL/user/login`\
*Method*: `POST`\
*Data*:\
`{
    "credential": "rkshaon",
    "password": "12345678"
}`\
*Response*: you'll get a response message with a `Token`

**Logout**\
*URL* : `BASE-URL/user/logout`\
*Method*: `POST`\
*Data*: No data required\
*Response*: you'll get a response message with status `True` or `False`

**Profile**\
*URL* : `BASE-URL/user/profile`\
*Method*: `GET`\
*Data*: No data required\
*Header*: You have to provide token\
*Response*: you'll get a response with User's Data\

**Weather Type List**\
*URL* : `BASE-URL/weather`\
*Method*: `GET`\
*Data*: No data required\
*Header*: You have to provide token\
*Response*: you'll get a response with weather type list\

**Add Weather Type**\
*URL* : `BASE-URL/weather/add`\
*Method*: `POST`\
*Data*:\
`{
    "name": "Hot",
    "lowest_temp": "30",
    "hightest_temp": "100"
}`\
*Header*: You have to provide token\
*Response*: you'll get a response message with status `True` or `False`

**Get Weather Type**\
*URL* : `BASE-URL/weather/<id>`\
*Method*: `GET`\
*Data*: No data required\
*Header*: You have to provide token\
*Response*: you'll get a response weather type details

**Edit Weather Type**\
*URL* : `BASE-URL/weather/<id>`\
*Method*: `PUT`\
*Data*:\
`{
    "name": "Hot"
}`\
*Header*: You have to provide token\
*Response*: you'll get a response message with status `True` or `False`

**Delete Weather Type**\
*URL* : `BASE-URL/weather/<id>`\
*Method*: `DELETE`\
*Data*: No data required\
*Header*: You have to provide token\
*Response*: you'll get a response message with status `True` or `False`

**Product List**\
*URL* : `BASE-URL/product`\
*Method*: `GET`\
*Data*: No data required\
*Header*: You have to provide token\
*Response*: you'll get a response with product list\

**Add Product**\
*URL* : `BASE-URL/product/add`\
*Method*: `POST`\
*Data*:\
`{
    "name": "Product Name",
    "quantity": "100"
}`\
*File*: Attach an image file with name `image`\
*Header*: You have to provide token\
*Response*: you'll get a response message with status `True` or `False`

**Get Weather Recommended Product**\
*URL* : `BASE-URL/product/weather-recommended`\
*Method*: `GET`\
*Data*: No data required\
*Header*: You have to provide token\
*Response*: you'll get a response message with product details

**Get Product**\
*URL* : `BASE-URL/product/<id>`\
*Method*: `GET`\
*Data*: No data required\
*Header*: You have to provide token\
*Response*: you'll get a response message with product details

**Edit Product**\
*URL* : `BASE-URL/product/<id>`\
*Method*: `PUT`\
*Data*:\
`{
    "product_type": "3"
}`\
*Header*: You have to provide token\
*Response*: you'll get a response message with status `True` or `False`

**Delete Product**\
*URL* : `BASE-URL/product/<id>`\
*Method*: `DELETE`\
*Data*: No data required\
*Header*: You have to provide token\
*Response*: you'll get a response message with status `True` or `False`

**Search Products**\
*URL* : `BASE-URL/product?name=some-product-name&weather=some-weather-type-name`\
*Method*: `GET`\
*Data*: No data required\
*Header*: You have to provide token\
*Response*: you'll get a response with product list\
*Note*: You can provide both query parameter or any one - return result will be according to those parameters.
