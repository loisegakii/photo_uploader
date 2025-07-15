#  Photo Gallery Web App

A full-stack Django web application for uploading, storing, and browsing user-contributed photos. 
Users can register, log in, upload photos with descriptions and tags, and view them in a beautiful gallery.
  
##  Features

- User authentication (Register, Login, Logout)
- Photo upload form with title, description, and image
- Responsive photo gallery view
- User-specific profile page
- Tailwind CSS styling
- PostgreSQL database integration
- Media file handling (images)

---

##  Project Structure
photo_gallery_project/
├── gallery/ # Django app with views, models, urls, templates
├── media/ # Uploaded user photos (auto-created)
├── photo_gallery_project/ # Project settings
├── templates/ # Global templates including base.html
├── static/ (optional) # Your custom static files
├── venv/ # Virtual environment (not tracked)
├── manage.py # Django CLI entry point
└── README.md # This file


## Setup Instructions

**1**. **Clone the repository**
git clone https://github.com/your-username/photo-gallery-app.git
cd photo-gallery-app
**2**. **Create and activate a virtual environment**
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux

**3**. **Install dependencies**
pip install -r requirements.txt

**4**. **Set up PostgreSQL (or use SQLite for testing)**
Ensure your settings.py has correct DB credentials.

**5. Run migrations**
python manage.py makemigrations
python manage.py migrate

**6. Create a superuser (optional)**
python manage.py createsuperuser

**7. Start the development server**

python manage.py runserver

# Requirements
Python 3.8+
Django 3.2
PostgreSQL (or SQLite)
Tailwind CSS (via CDN or built locally)

# Author

Loise Gakii
