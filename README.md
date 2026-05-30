🖥️ Computer Shop Management System

A full-stack web application built using Django, Python, HTML, CSS, and JavaScript for managing a computer shop with product listings, user authentication, and admin control panel.

📌 About the Project

This project is a Django-based e-commerce system designed for a computer shop. It allows users to browse products, manage a shopping cart, and place orders, while admins can manage products and users through the Django admin panel.

🚀 Features
🔐 User Registration & Login System

🛒 Shopping Cart Functionality

📦 Product Management (Add / Update / Delete)

🧑‍💼 Admin Dashboard

🖼️ Media Upload Support (Product Images)

🎨 Responsive UI using HTML, CSS, Bootstrap

⚡ Secure backend using Django framework

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript, Bootstrap

Backend: Python, Django

Database: SQLite (default Django DB)

Tools: Git, GitHub

📁 Project Structure
computer_shop/
│

├── shop/                  # Main application

├── templates/             # HTML templates

├── static/                # CSS, JS files

├── media/                 # Uploaded images (ignored in GitHub)

├── db.sqlite3             # Database (ignored in GitHub)

├── manage.py

└── requirements.txt


⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/Computer-Shop.git
cd Computer-Shop

3. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

5. Install dependencies 
pip install -r requirements.txt

7. Run migrations
python manage.py migrate

9. Start development server
python manage.py runserver
🔐 Admin Panel

To access admin panel:

python manage.py createsuperuser

Then go to:

http://127.0.0.1:8000/admin

⚠️ Important Notes
.env file is used for secret keys (not uploaded to GitHub)
db.sqlite3 and media/ folders are ignored for security
Project is in development mode (DEBUG=True)
👨‍💻 Author

Sayali
Student Developer | Django Enthusiast

📌 Future Improvements
Payment gateway integration
Advanced search & filters
Order tracking system
Deployment on cloud (Render / PythonAnywhere)

⭐ Show Support
If you like this project, give it a ⭐ on GitHub!
