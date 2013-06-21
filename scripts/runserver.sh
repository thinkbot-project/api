#!/usr/bin/env bash

setup_env() {
    source venv/bin/activate
    source config/secrets/$1.sh
    if [ $1 = "local" ]
    then
	source ~/Work/FEniCS/dev/share/dolfin/dolfin.conf && export PYTHONPATH=${PYTHONPATH}:../:../../ && export CC=/usr/bin/gcc && export CXX=/usr/bin/g++
    fi
}

run_webapp() {
    if [ $1 = "local" ]
    then
	cd compute_service
	./manage.py celeryd -l info --autoreload &
	./manage.py runserver 8001
    else
	sudo -E venv/bin/uwsgi --ini config/uwsgi/thinkbot.net.ini
    fi
}


if [ $1 = "local" ] || [ $1 = "production" ]
then
    BASE_DIR="$( cd "$( dirname "$0" )" && pwd )"
    cd ${BASE_DIR}/..
    setup_env $1
    run_webapp $1
else
    echo "You need to run this script with ./runserver.sh {local|production}"
fi
