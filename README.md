# Dinewise

Dinewise is a modern restaurant ordering web application built with Django. It allows users to browse restaurant menus, add items to a cart, securely register and log in, and pay using the Gokwik payment gateway. The app features a clean, responsive UI and supports receipt downloads after payment.

## Setup & Run Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Dinewise
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv vibecodingvenv
   vibecodingvenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the app**
   - Open your browser and go to `http://127.0.0.1:8000/`

## Features

- Browse multiple restaurants with unique menus
- Add items to cart (only from one restaurant at a time)
- Delete items or clear the cart
- User registration and login with secure password hashing
- Payment integration using Gokwik (simulated)
- Downloadable payment receipt
- Beautiful, responsive design

## Technologies Used

- Python 3
- Django
- HTML5, CSS3, JavaScript
- SQLite (default, can be changed)

## Folder Structure

```
Dinewise/
├── Dinewise/                # Django project settings
├── Dinewise_app/            # Main app (views, models, templates, static)
├── Dinewise_retailer_app/   # Retailer app (optional)
├── vibecodingvenv/          # Virtual environment
├── db.sqlite3               # Database
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── Procfile                 # For deployment (Heroku, etc.)
```

## Key Files

- `Dinewise_app/models.py`: Models for users, menu items, cart, and payments
- `Dinewise_app/views.py`: All view logic (menu, cart, payment, authentication)
- `Dinewise_app/templates/`: HTML templates for all pages
- `Dinewise_app/static/`: CSS, JS, and images

## Payment Integration

- The payment gateway uses Gokwik (simulated for demo purposes)
- Payment details are stored in the database
- After payment, users are redirected to a receipt page with a downloadable receipt

## Customization

- Add new restaurants and menu items by editing templates and models
- Change payment gateway integration in `views.py` as needed
- Update styles in `static/index.css` for branding

## License

This project is for educational/demo purposes. For production use, please review and update security, payment, and deployment settings.

---

For any queries or contributions, please contact the project maintainer.
