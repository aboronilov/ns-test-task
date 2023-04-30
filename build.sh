# Install packages
pip install -r deps.txt

# CSS
python manage.py tailwind build
python manage.py collectstatic --no-input

# Migrate
python manage.py migrate