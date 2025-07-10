📝 To-Do List Web App
A simple and responsive To-Do List web application built using Django and SQLite. Users can sign up, log in, and perform full CRUD operations (Create, Read, Update, Delete) on their tasks.


🚀 Features
✅ User Registration & Login

📝 Add, Edit, Delete tasks

📅 Mark tasks as complete/incomplete

📱 Responsive UI (mobile-friendly)

🔐 Secure user-based task management

⚙️ Technologies Used
Python 3.x

Django 4.x / 5.x

HTML5, CSS3

Bootstrap (optional)

SQLite3 (default Django DB)

🔧 Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Run the development server
bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

🗂 Project Structure
csharp
Copy
Edit
todo/
├── todo/              # Project settings
├── tasks/             # App (models, views, urls)
├── templates/         # HTML templates
├── static/            # CSS, JS, images
├── db.sqlite3         # Default database
└── manage.py
📌 To-Do (Improvements)
 Add due dates and priority

 Dark mode toggle

 Task categories/tags

 Deployment (e.g., Heroku, Render)

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributions
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

👨‍💻 Author
Prashant Kumar Tiwary
