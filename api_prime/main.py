import routes

from app import app

#### localhost server
#HOST = '127.0.1.2'
#### externally visible server
HOST = '0.0.0.0'
PORT = 7007


#from tienda.blueprint import tienda ## api_tienda
from api.v1.bussiness.blueprint import api_prime


#app.register_blueprint(tienda, url_prefix='/tienda') ## api_tienda
app.register_blueprint(api_prime, url_prefix='/api/v1/bussiness')


if __name__ == '__main__':
   app.run(host=HOST, port=PORT)

