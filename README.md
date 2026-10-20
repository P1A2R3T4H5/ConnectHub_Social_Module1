# ConnectHub Social — Module 1
A modern Instagram-inspired social networking app built with Django, HTML, CSS and a little JavaScript.

Features: signup/login/logout, profile bio/avatar/website, image and text posts, feed, likes, comments, follow/unfollow, Explore/search, responsive interface and Django admin.

## Run on Windows / VS Code
1. Extract the ZIP and open the `ConnectHub_Social_Module1` folder in VS Code.
2. Open Terminal → New Terminal.
3. Run:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python manage.py makemigrations social
   python manage.py migrate
   python manage.py runserver
   ```
4. Visit http://127.0.0.1:8000/ and create an account.
5. Optional admin login: run `python manage.py createsuperuser`, then visit http://127.0.0.1:8000/admin/.

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal, then activate again.

This is a local starter project, not connected to the official APIs of Instagram, Snapchat, Facebook or WhatsApp. Change the development secret key and DEBUG setting before deployment.
