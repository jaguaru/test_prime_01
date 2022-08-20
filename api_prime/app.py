####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

from flask_mysqldb import MySQL

from flask import Flask, request, render_template

from flask_wtf.csrf import CSRFProtect, CSRFError
##from flask_sslify import SSLify #### para forzar el ssl y https
from itsdangerous import URLSafeTimedSerializer
from config import Configuration


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

PROD_HOST = 'localhost'
PROD_PORT = '3306'
PROD_USER = 'prime_one'
PROD_PASS = 'PrimeUser01'
PROD_DB_NAME = 'ApiPrime'

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

##TIME_SESSION = timedelta(minutes=2)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

app = Flask(__name__)
app.config.from_object(Configuration)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

app.config['MYSQL_HOST'] = PROD_HOST
app.config['MYSQL_PORT'] = int(PROD_PORT)
app.config['MYSQL_DB'] = PROD_DB_NAME
app.config['MYSQL_USER'] = PROD_USER
app.config['MYSQL_PASSWORD'] = PROD_PASS
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

if mysql:
    print('--------------------------------------------')
    print('  ----  Connected to Sigce DB!')
    print('--------------------------------------------')
else:
    print('--------------------------------------------')
    print('  ----  Conection Error!')
    print('--------------------------------------------')

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

expiration = 300 #1800 #900s=15min // 600s=10min // 300s=5min
ts = URLSafeTimedSerializer(app.config["SECRET_KEY"], expiration)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

