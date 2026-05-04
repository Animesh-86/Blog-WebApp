# Blog Project

This is a Django-based blog application.

## Project Structure

- `blog/` - Main app containing models, views, forms, templates, and templatetags.
- `mysite/` - Project configuration and settings.
- `db.sqlite3` - SQLite database file.

## Features
- User authentication (signup, login, profile)
- Blog dashboard
- Add/view datasets
- About page

## Setup Instructions

1. **Clone the repository**
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the app at `http://127.0.0.1:8000/`

## Folder Structure
```
mysite/
    db.sqlite3
    manage.py
    blog/
        ...
    mysite/
        ...
```

## License
MIT License
