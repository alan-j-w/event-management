# Eventifys — Event Management Platform

A full-stack event management platform built with Django, designed for discovering, booking, and managing cultural festivals, tech conferences, and workshops.

**Live Demo:** [eventifys.onrender.com](https://eventifys.onrender.com)

---

## Features

- **Event Discovery** — Browse a curated catalog of events with rich imagery, dates, and locations.
- **Secure Booking** — Register for events through a validated booking system with real-time inline form feedback.
- **Authentication** — Standard login/signup flow with Google OAuth integration via django-allauth.
- **Admin Dashboard** — Full Django Admin panel for managing events, bookings, and users.
- **Responsive Design** — Clean, professional UI built with Bootstrap 5 and the Inter typeface.
- **Production Ready** — Deployed on Render with WhiteNoise for static file serving and environment-based configuration.

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Django 5.x |
| Frontend | HTML5, CSS3, Bootstrap 5.3, Font Awesome 6 |
| Database | SQLite (dev), PostgreSQL-ready via `dj-database-url` |
| Auth | django-allauth (Google OAuth 2.0) |
| Static Files | WhiteNoise |
| Deployment | Render |

## Project Structure

```
event-management-main/
├── eventapp/           # Core app — models, views, forms, URLs
├── eventpr/            # Django project settings & config
├── userapp/            # Authentication — login, register, logout
├── template/           # All HTML templates (base, index, events, etc.)
├── static/             # CSS, images, and other static assets
├── pic/                # Media uploads (event images)
├── populate_events.py  # Script to seed the database with sample events
├── manage.py
├── requirements.txt
└── Procfile            # Render deployment entry point
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/alan-j-w/event-management.git
cd event-management/event-management-main

# Create a virtual environment
python -m venv env
env\Scripts\activate        # Windows
# source env/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed sample events (optional)
python populate_events.py

# Start the development server
python manage.py runserver
```

### Environment Variables

Create a `.env` file in the project root for local development:

```
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=1
```

## Screenshots

| Home | Events | Booking |
|------|--------|---------|
| Clean hero section with featured carousel | Grid layout with event cards | Validated booking form |

## License

This project is open source and available for educational purposes.

---

Developed by [Alan Joy Wilson](https://www.linkedin.com/in/alan-joy-wilson)
