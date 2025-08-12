# 🏨 Django Hotel Booking Platform

A **full‑stack hotel booking web application** built with Django that showcases secure OTP-based login, dynamic guest management, and powerful hotel search & filtering, powered by a real hotel dataset imported from CSV.

---

## 🚀 Features

### 🔐 OTP-Based Login
- Server‑side generated 6‑digit OTP tied to user session.
- OTP expires automatically after **5 minutes**.
- Secure validation with error messages for expired/invalid codes.

### 👥 Guest Management
- Add multiple guest details via a dynamic **Bootstrap modal**.
- Client‑side validation for guest name.
- Add / Remove guest rows instantly without page reload.
- Guest list updates dynamically on the main screen.

### 🏨 Hotel Search & Filtering
- Search hotels by **City**.
- Filter results by **Hotel Name** in real time.
- View details: Name, Address, Rating, Price, Amenities.
- Graceful “No hotels found” message.
- 
- ### 📂 Dataset Integration
- Import large hotel datasets **from CSV** into the database using a custom Django management command:
- python manage.py import_hotels path/to/hotels_with_price.csv

- - Dataset fields: City, Hotel Name, Address, Price, Rating, Amenities.

---

## 🛠 Tech Stack

- **Backend:** Django (Python 3)
- **Frontend:** HTML, Bootstrap 4, JavaScript
- **Database:** SQLite (default, easily swappable for PostgreSQL/MySQL)
- **Other:** Django Admin, Custom Management Command for CSV import

- 
## 📂 Project Structure
hotelbooking/
│
├── hotelbooking/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── otp/ # OTP login app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/otp/
│
├── guests/ # Guest management app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/guests/
│
├── hotel/ # Hotel search and dataset import app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── management/commands/import_hotels.py
│ └── templates/hotel/
│
├── templates/base.html # Shared base template
└── static/ # Static files (CSS, JS)
---

## ⚙️ Installation & Setup

1. **Clone the repository**
   git clone https://github.com/MARK1705/Hotel-Booking-platform-using-Django.git
cd Hotel-Booking-platform-using-Django

2. **Create a virtual environment & activate**
   python -m venv venv

Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Apply migrations**
python manage.py makemigrations
python manage.py migrate

5. **Import your hotel dataset**
python manage.py import_hotels "C:\path\to\hotels_with_price.csv"


6. **Run the server**
python manage.py runserver


7. **Access the app**
- Go to `http://127.0.0.1:8000` for OTP login flow.
- Manage Guests at `/guests/`.
- Search Hotels at `/hotel/search/`.

---

## 📌 Future Improvements
- Email/SMS OTP delivery instead of console log.
- More hotel filters (price range, rating).
- User accounts with booking history.
- Deployment to cloud (Heroku, Render, etc.).

- ---

**Author:** Mergu Bharath kumar 
💡 *Built as a Django learning and demonstration project.*
