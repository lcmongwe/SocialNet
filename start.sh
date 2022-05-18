export SECRET_KEY=abc
export SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://lucy:4444@localhost/nets'

# python3 manage.py shell
python3 manage.py server
# python3 manage.py db init
# python3 manage.py db migrate -m "initial migration"
# python3 manage.py db upgrade
# python manage.py db stamp head

