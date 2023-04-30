# Install packages
pip install -r deps.txt

# CSS
python manage.py tailwind build

# Migrate
python manage.py migrate