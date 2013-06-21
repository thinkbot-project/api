cd ~/sites/mechanicsacademy.com
git pull
source venv/bin/activate
source config/secrets/production.sh
pip install -r requirements.txt
cd lms
./manage.py migrate
./manage.py collectstatic --noinput
# restart uwsgi