# Django Admin - Event Booking System

## 📋 Overview

This Django project implements an event booking system with a focus on customizing and configuring the Django Admin Panel. The system enables management of events, categories, locations, participants, and bookings through a user-friendly admin interface.

## 🏗️ Project Structure

```
da-intensivkurs-backend-06-aufgabe/
├── core/                    # Main Django configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   └── ...
├── events_app/             # App for events
│   ├── models.py           # Event, EventCategory, Location
│   ├── admin.py            # Admin configuration for events
│   └── migrations/         # Database migrations
├── bookings_app/           # App for bookings
│   ├── models.py           # Participant, Booking
│   ├── admin.py            # Admin configuration for bookings
│   └── migrations/         # Database migrations
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## 🛠️ Technology Stack

- **Django 5.2** - Web Framework
- **SQLite** - Database
- **Python 3.x** - Programming Language

## 📊 Data Models

### Events App
- **EventCategory**: Categorization of events
- **Location**: Event venues with addresses
- **Event**: Main model for events (displayed as "Liveact" in admin)

### Bookings App
- **Participant**: Participants with first name, last name, and email
- **Booking**: Bookings with confirmation status

## 🚀 Installation and Setup

### 1. Clone repository
```cmd
git clone <repository-url>
cd da-intensivkurs-backend-06-aufgabe
```

### 2. Create virtual environment
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```cmd
pip install -r requirements.txt
```

### 4. Migrate database
```cmd
python manage.py migrate
```

### 5. Create superuser
```cmd
python manage.py createsuperuser
```

### 6. Start server
```cmd
python manage.py runserver
```

### 7. Access admin panel
Open your browser and go to: `http://127.0.0.1:8000/admin/`

## ⚙️ Admin Panel Features

### Event Management
- **Display**: Title, category, location, and date
- **Search**: By title and date
- **Filter**: By category
- **Date hierarchy**: Grouping by date
- **Fieldsets**: Divided into "General" and "Organization"

### Booking Management
- **Filter**: By confirmation status (confirmed)
- **Read-only fields**: Booking date automatically set

### Participant Management
- **Prepopulated fields**: Full name automatically generated from first and last name
- **Help texts**: Available for all input fields

## 🎯 Implemented Exercise Tasks

### ✅ Task 1: Project Setup
- Project cloned and migrated
- Superuser created
- Admin panel accessible

### ✅ Task 2: Model Registration
- All models registered in both apps
- Admin classes created for each model

### ✅ Task 3: List Display Customization
- Event overview shows: title, category, location, date
- capacity field hidden

### ✅ Task 4: Search and Filter Functions
- Search function for title and date
- Filter by category implemented

### ✅ Task 5: Fieldsets Layout
- Event form divided into two sections:
  - **General**: title, category, date
  - **Organization**: location, capacity

### ✅ Task 6: Date Hierarchy
- Date hierarchy added for events

### ✅ Task 7: Booking Filter
- Filter for confirmed bookings (confirmed=True)

### ✅ Task 8: Model Renaming
- Event model displayed as "Liveact" in admin
- Sorting by date implemented

### ✅ Task 9: Read-only Fields
- booking_date configured as read-only

### ✅ Task 10: Prepopulated Fields
- full_name field added
- Automatic combination of first_name and last_name

### ✅ Task 11: Help Texts
- Help texts added for first_name, last_name, and email

## 📝 Usage

### Creating Test Data
1. Log into the admin panel
2. Create EventCategories (e.g., "Concert", "Workshop", "Conference")
3. Create Locations with names and addresses
4. Create Events with all required fields
5. Create Participants
6. Create Bookings and confirm them

### Using Admin Features
- **Search**: Use the search bar to find events by title or date
- **Filter**: Use the sidebar to filter by categories or confirmation status
- **Date Navigation**: Use the date hierarchy for time-based navigation

## 🔧 Important Admin Configurations

### EventAdmin
```python
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "location", "date"]
    search_fields = ["title", "date"]
    list_filter = ["category"]
    date_hierarchy = 'date'
    fieldsets = (...)
```

### BookingAdmin
```python
class BookingAdmin(admin.ModelAdmin):
    list_filter = ["confirmed"]
    readonly_fields = ["booking_date"]
```

### ParticipantAdmin
```python
class ParticipantAdmin(admin.ModelAdmin):
    prepopulated_fields = {"full_name": ["first_name", "last_name"]}
```

## 📚 Further Documentation

- [Django Admin Documentation](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)
- [Django Models Documentation](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Django Migrations Documentation](https://docs.djangoproject.com/en/5.2/topics/migrations/)

## 🤝 Development

This project was created as an exercise for the Django intensive course to demonstrate the functionalities and customization possibilities of the Django Admin Panel.

## 📄 License

This project was created for educational purposes.