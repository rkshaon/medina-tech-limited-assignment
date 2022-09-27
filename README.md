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
*Response*: you'll get a response message with a `Token`

**Profile**\
*URL* : `BASE-URL/user/profile`\
*Method*: `GET`\
*Data*: No data required\
*Header*: You have to provide token\
*Response*: you'll get a response message with a `Token`
