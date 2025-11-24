## User & Task Management Backend (Flask + MongoDB)

This project is a backend service built using Flask and MongoDB.
It provides:

User Management (Create, Get, Update)

Automatic Profile Completion %

Task Management (CRUD)

Clean, modular Flask architecture using Blueprints

This backend recreates the same functionality as your Node.js version, but now using Python.

# Tech Stack used
| Component             | Technology                         |
| --------------------- | ---------------------------------- |
| **Backend Framework** | Flask (Python)                     |
| **Database**          | MongoDB (Local instance)           |
| **ORM / Driver**      | Flask-PyMongo                      |
| **Password Hashing**  | bcrypt                             |
| **Request Handling**  | Flask request + JSON               |
| **Architecture**      | Flask Blueprints (modular routing) |


# Project folder structure
flask-backend/

│

├── app.py                      # Main Flask App

├── config.py                   # MongoDB connection

│

├── routes/

│   ├── users.py                # User Routes (Blueprint)

│   └── tasks.py                # Task Routes (Blueprint)

│

├── utils/

│   └── profile_completion.py   # Profile Completion Logic

│

├── requirements.txt            # Project dependencies

└── README.md  

└── .env

└── .gitignore




## How to Run the Project

Follow these steps to run the backend on your system.

# Install Dependencies

Open terminal inside the project folder:

pip install -r requirements.txt


If requirements.txt is not present, use:

pip install flask flask-pymongo bcrypt python-dotenv

# Start MongoDB Server

This project uses a local MongoDB database named:

FlaskTaskDB

If you're on Windows:
mongod

macOS / Linux:
brew services start mongodb-community


or

mongod


MongoDB must be running, otherwise Flask won't connect.

# Start the Flask Server

Run:

python app.py


The API will now be live at:

http://127.0.0.1:5000


# API Endpoints

✔ User Endpoints

POST   /users/createUser

GET    /users/<id>

PATCH  /users/updateUser/<id>

GET    /users/ProfileCompletion/<id>


✔ Task Endpoints

POST    /tasks/createTask

GET     /tasks/getTasks/<userId>

GET     /tasks/getTask/<taskId>

PATCH   /tasks/updateTask/<taskId>

DELETE  /tasks/deleteTask/<taskId>
