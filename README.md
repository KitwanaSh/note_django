# Note App
## Technologies Used
- Backend: Django, Django REST Framework (DRF)
- Frontend: ReactJS
- Database: PostgreSQL (can be changed)
- Additional Tools: Git, Pipenv, npm
### Features
- User authentication and registration
- Create, read, update, and delete notes
- Organize notes with titles and categories
- Markdown formatting for richer note content
- Search and filter notes
- Responsive design for various devices
### Getting Started
#### 1. Clone the Repository:

```git clone https://github.com/your-username/note-app.git```

#### 2. Setup Backend:

- Install pipenv and use it to manage dependencies:

```python -m pipenv install```
- Make the virtual environment active:

```pipenv shell```
- Install backend dependencies:

```pipenv install```

- Set up the database:

* Edit backend/settings.py with your database details.
* Run python manage.py migrate to create database tables.
* Create a superuser: python manage.py createsuperuser.

- Start the development server:

```python manage.py runserver```
### 3. Setup Frontend:

- Navigate to the frontend directory:
```cd frontend```
- Install frontend dependencies:
```npm install```
- Start the development server:
```npm start```

#### 4. Access the App:

- Open `http://localhost:8000` in your browser for the backend admin panel.
- Open `http://localhost:3000` in your browser for the React frontend.
- Register or login on the frontend and start managing your notes!

#### Documentation
- API Documentation: `http://localhost:8000/api/docs/`
- Backend Code: _backend/ directory_
- Frontend Code: _frontend/ directory_

#### Deployment
You can deploy the app to various platforms like Heroku, AWS, etc.
Refer to the official documentation of your chosen platform for deployment instructions.

#### Contributing
Feel free to fork the repository and contribute by adding features, improving code quality, or fixing bugs.
Create pull requests with clear messages and follow the coding style conventions.

#### Further Development
- Add features like tagging, collaboration, file attachments, etc.
- Implement push notifications or real-time updates for changes.
- Integrate with other services like Google Drive or Evernote.