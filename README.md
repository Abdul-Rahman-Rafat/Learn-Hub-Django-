🧠 LearnHub — Django REST + Frontend App
=========================================

LearnHub is a simple educational web application built with Django and Django REST Framework.
It provides a RESTful API along with a clean user interface (UI) for managing students and courses efficiently.

==============================================

🔍 Features
=============
User Authentication
Secure login and logout using Django’s built-in authentication system.
Protected routes — you must log in to access Students or Courses pages.

Student Management

Display all students in a responsive table.

Add a new student via an interactive form (name, year, enrollment date, image).

Assign multiple courses to a student (Many-to-Many relationship).

Instantly view the updated student list after adding or editing records.

Course Management

View all available courses.

Create new courses easily.

Link each student with one or more courses.

Responsive Frontend (Bootstrap)
A modern, responsive interface built with HTML, CSS, Bootstrap, and JavaScript.


Secured with token authentication (JWT support planned).


==============================================
| Layer          | Technology                             |
| -------------- | -------------------------------------- |
| **Backend**    | Django, Django REST Framework          |
| **Frontend**   | HTML, CSS, Bootstrap, JavaScript       |
| **Database**   | SQLite (default)                       |
| **Auth**       | Django Authentication System           |
| **Deployment** | Localhost / Gunicorn / Any WSGI server |


==============================================

🚀 How It Works
===================

1-User logs in through the Login Page.

2-Once authenticated, the user can manage students and courses.

3-All CRUD operations (Add / Edit / Delete / List) are synchronized between the frontend and backend.