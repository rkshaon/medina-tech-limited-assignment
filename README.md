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
**Registration**
*URL* : `http://127.0.0.1:8000/user/registration`
*Method*: `POST`
Role 1 - Admin, 2 - Vendor, 3 - Customer\
`{
    "name": "Rezaul Karim Shaon",
    "username": "rkshaon",
    "email": "rkshaon.ist@gmail.com",
    "password": "12345678",
    "role": "1"
}`

