from fabric.api import local
import os

def collect():
    local('heroku run python src/manage.py collectstatic --noinput')

def start():
    local('heroku local web')

def env():
    local('heroku config:set DJANGO_SETTINGS_MODULE=todo.settings.production')

def log():
    local('heroku logs')

def untrack():
    local('git add -A')

def migrate():
    local('heroku maintenance:on --app my-asana')
    local('heroku run python src/manage.py makemigrations')
    local('heroku run python src/manage.py migrate')
    local('heroku maintenance:off --app my-asana')


def git():
    local('git pull origin master')

def heroku():
    local('heroku maintenance:on --app my-asana')
    local('git push heroku master')
    local('heroku maintenance:off --app my-asana')

def deploy():
    local('git add .')
    print "Enter the git commit comment: "
    comment = raw_input()
    local(' git commit -m "%s"'%comment)
    local('git push origin master')
    local('heroku maintenance:on --app my-asana')
    local('git push heroku master')
    local('heroku maintenance:off --app my-asana')

def runserver():
    local('python src/manage.py runserver 0.0.0.0:8000')

def aws():
    local('git status')
    local('git add .')
    comment = raw_input("Enter the commit comment: ")
    local('git commit -m "%s"'%comment)
    local('git push origin master')
