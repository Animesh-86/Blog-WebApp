# MySite Blog Platform

A minimalist and modern blogging platform built with Django and Tailwind CSS.

## Features

- Secure user authentication (signup, login, logout)
- Create, view, and manage blogs
- Responsive design with Tailwind CSS
- Admin dashboard for user and blog stats

## Project Structure

```
mysite/
  manage.py
  db.sqlite3
  blog/
    models.py
    views.py
    forms.py
    urls.py
    templates/
      blog/
        base.html
        home.html
        signup.html
        login.html
        dashboard.html
        profile.html
        add_dataset.html
        view_blog.html
    migrations/
  mysite/
    settings.py
    urls.py
```

## Setup

1. **Install dependencies:**
   ```sh
   pip install django
   ```

2. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

3. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

4. **Access the site:**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Usage

- Sign up for a new account
- Log in to access your dashboard
- Add, view, and manage your blogs

## License

MIT License
