cd ~/sites/thinkbot.net
git pull
source venv/bin/activate
source config/secrets/production.sh
pip install -r requirements.txt
cd compute_service
./manage.py migrate
./manage.py collectstatic --noinput
# restart uwsgi
# restart celery
