
####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

#import requests
import json, time, datetime, string, random

from datetime import datetime, timedelta
from json import dumps

from validations import get_room_code, get_room_capacity, register_to_event, get_all_customers_event, get_all_created_events
from validations import add_customer, creating_event, creating_room, event_cancel, created_event_cancel

from flask import Flask, Blueprint, render_template, redirect, url_for, request, jsonify, make_response
from app import app, mysql


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

TIME_SLEEP = 0.5

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

datetime_now_str = str(datetime.now())

# print('--------------------------------------------')
# print('----------  Fecha y hora ', datetime_now_str)
# print('--------------------------------------------')

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

api_prime = Blueprint('/v1/bussiness', __name__)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

string_ascii = 'ABCDEFGHIJKLMNPQRSTUVWYYZ'
digits = '123456789'
def code_generator(size=8, chars=string_ascii + digits):
    token_gen = ''.join(random.choice(chars) for _ in range(size))
    return str(token_gen)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####  API EXAMPLE
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "room_name": "Blue", "capacity": "100" }' http://0.0.0.0:7007/api/v1/bussiness/create_room/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "room_name": "White", "capacity": "500" }' http://0.0.0.0:7007/api/v1/bussiness/create_room/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "room_name": "Purple", "capacity": "200" }' http://0.0.0.0:7007/api/v1/bussiness/create_room/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "room_name": "Yellow", "capacity": "400" }' http://0.0.0.0:7007/api/v1/bussiness/create_room/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "room_name": "Magenta", "capacity": "150" }' http://0.0.0.0:7007/api/v1/bussiness/create_room/
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
@api_prime.route('/create_room/', methods=["GET", "POST"])
def create_room():

   code = str(code_generator())
   name = str(request.json.get('room_name'))
   capacity = str(request.json.get('capacity'))

   status = '1' #### status: 0 = canceled, 1 = created

   print(' -----------------------------------------------')
   print(' ----  code ', code)
   print(' ----  name ', name)
   print(' ----  capacity ', capacity)
   print(' ----  status ', status)
   print(' -----------------------------------------------')

   create_room = creating_room(code, name, capacity, status)

   if create_room == True:
      response = { 'status': 'success', 'room_name': name, 'room_code': code, 'message': 'The room is created!' }
   else:
      response = { 'status': 'error', 'message': 'The room cant be created!' }

   return jsonify(response)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####  API EXAMPLE
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_name": "Weeding", "event_type": "PUBLIC", "room_code": "8172Y2EP" }' http://0.0.0.0:7007/api/v1/bussiness/create_event/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_name": "Community Party", "event_type": "PUBLIC", "room_code": "VSMEUQTV" }' http://0.0.0.0:7007/api/v1/bussiness/create_event/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_name": "Conference", "event_type": "PRIVATE", "room_code": "GF82Q7QY" }' http://0.0.0.0:7007/api/v1/bussiness/create_event/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_name": "Conference Python", "event_type": "PUBLIC", "room_code": "BHZL37BC" }' http://0.0.0.0:7007/api/v1/bussiness/create_event/
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
@api_prime.route('/create_event/', methods=["GET", "POST"])
def create_event():

   code = str(code_generator())
   name = str(request.json.get('event_name'))
   type = str(request.json.get('event_type')) #### PUBLIC or PRIVATE
   fk_room_code = str(request.json.get('room_code')) #### room code

   status = '1' #### status: 0 = canceled, 1 = created

   print(' -----------------------------------------------')
   print(' ----  code ', code)
   print(' ----  name ', name)
   print(' ----  type ', type)
   print(' ----  fk_room_code ', fk_room_code)
   print(' ----  status ', status)
   print(' -----------------------------------------------')
  
   event_create = creating_event(code, name, type, status, fk_room_code)

   if event_create == True:
      response = { 'status': 'success', 'event_code': code, 'event_name': name, 'event_type': type, 'message': 'The event is created!' }
   else:
      response = { 'status': 'error', 'message': 'The event cant be created!' }

   return jsonify(response)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####  API EXAMPLE
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "1SZEGNW9" }' http://0.0.0.0:7007/api/v1/bussiness/cancel_event_created/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "U9G6T568" }' http://0.0.0.0:7007/api/v1/bussiness/cancel_event_created/
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
@api_prime.route('/cancel_event_created/', methods=["GET", "POST"])
def cancel_event_created():

   code = str(request.json.get('event_code'))

   status = '0' #### status: 0 = canceled, 1 = created

   print(' -----------------------------------------------')
   print(' ----  code ', code)
   print(' ----  status ', status)
   print(' -----------------------------------------------')
  
   event_canceled = created_event_cancel(code, status)

   if event_canceled == True:
      response = { 'status': 'success', 'message': 'The event is canceled!' }
   else:
      response = { 'status': 'error', 'message': 'The event cant be canceled!' }

   return jsonify(response)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####  API EXAMPLE
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "1SZEGNW9", "customer_code": "M7P6HWA6" }' http://0.0.0.0:7007/api/v1/bussiness/register_event_customer/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "U9G6T568", "customer_code": "BUCRFR41" }' http://0.0.0.0:7007/api/v1/bussiness/register_event_customer/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "86W1YLES", "customer_code": "M7P6HWA6" }' http://0.0.0.0:7007/api/v1/bussiness/register_event_customer/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "UFY1RYP4", "customer_code": "BB7FLW1Q" }' http://0.0.0.0:7007/api/v1/bussiness/register_event_customer/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "UFY1RYP4", "customer_code": "M44K3G1Y" }' http://0.0.0.0:7007/api/v1/bussiness/register_event_customer/
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
@api_prime.route('/register_event_customer/', methods=["GET", "POST"])
def register_event_customer():

   code = str(code_generator())
   fk_event_code = str(request.json.get('event_code'))
   fk_customer_code = str(request.json.get('customer_code'))

   status = '1' #### status: 0 = canceled, 1 = created

   print(' -----------------------------------------------')
   print(' ----  code ', code)
   print(' ----  fk_event_code ', fk_event_code)
   print(' ----  fk_customer_code ', fk_customer_code)
   print(' ----  status ', status)
   print(' -----------------------------------------------')


   room_code = get_room_code(fk_event_code)
   print('  ----  room_code  ', room_code)

   room_capacity = int(get_room_capacity(room_code))
   print('  ----  room_capacity  ', room_capacity)

   all_customers = int(get_all_customers_event(fk_event_code))
   print('  ----  all_customers  ', all_customers)


   if all_customers < room_capacity:
      event_register = register_to_event(fk_event_code, fk_customer_code, status)

      if event_register == True:
          response = { 'status': 'success', 'customer_register_event_code': code, 'fk_customer_code': fk_customer_code, 'message': 'The registration to the event is created!' }
      else:
          response = { 'status': 'error', 'message': 'The registration to the event cant be created!' }
   else:
      response = { 'status': 'error', 'message': 'The event is full!' }
   
   return jsonify(response)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####  API EXAMPLE
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "1SZEGNW9", "customer_code": "M7P6HWA6" }' http://0.0.0.0:7007/api/v1/bussiness/cancel_event_customer/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "U9G6T568", "customer_code": "BUCRFR41" }' http://0.0.0.0:7007/api/v1/bussiness/cancel_event_customer/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "UFY1RYP4", "customer_code": "BB7FLW1Q" }' http://0.0.0.0:7007/api/v1/bussiness/cancel_event_customer/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "event_code": "UFY1RYP4", "customer_code": "M44K3G1Y" }' http://0.0.0.0:7007/api/v1/bussiness/cancel_event_customer/

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
@api_prime.route('/cancel_event_customer/', methods=["GET", "POST"])
def cancel_event_customer():

   fk_event_code = str(request.json.get('event_code'))
   fk_customer_code = str(request.json.get('customer_code'))

   status = '0' #### status: 0 = canceled, 1 = created

   print(' -----------------------------------------------')
   print(' ----  fk_event_code ', fk_event_code)
   print(' ----  fk_customer_code ', fk_customer_code)
   print(' ----  status ', status)
   print(' -----------------------------------------------')

   cancel_event = event_cancel(fk_event_code, fk_customer_code, status)

   print(' ----  cancel_event  ', cancel_event)

   if cancel_event == True:
      response = { 'status': 'success', 'message': 'The customer registration is canceled!' }
   else:
      response = { 'status': 'error', 'message': 'The customer registration cant be canceled!' }

   return jsonify(response)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####  API EXAMPLE
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "phone": "9612345201", "name": "ULYSES", "lastname": "GOMEZ" }' http://0.0.0.0:7007/api/v1/bussiness/create_customer/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "phone": "9612345202", "name": "ATHENA", "lastname": "HERNANDEZ" }' http://0.0.0.0:7007/api/v1/bussiness/create_customer/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "phone": "9612345203", "name": "PTOLOMEO", "lastname": "CASTILLOS" }' http://0.0.0.0:7007/api/v1/bussiness/create_customer/
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "phone": "9612345204", "name": "ANDROMEDA", "lastname": "FERNANDEZ" }' http://0.0.0.0:7007/api/v1/bussiness/create_customer/
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
@api_prime.route('/create_customer/', methods=["GET", "POST"])
def create_customer():

   code = str(code_generator())
   phone = str(request.json.get('phone'))
   name = str(request.json.get('name'))
   lastname = str(request.json.get('lastname'))

   status = '1' #### status: 0 = blocked, 1 = active

   print(' -----------------------------------------------')
   print(' ----  code ', code)
   print(' ----  phone ', phone)
   print(' ----  name ', name)
   print(' ----  lastname ', lastname)
   print(' ----  status ', status)
   print(' -----------------------------------------------')

   create_client = add_customer(code, phone, name, lastname, status)

   if create_client == True:
      response = { 'status': 'success', 'customer_code': code, 'message': 'The customer is created!' }
   else:
      response = { 'status': 'error', 'message': 'The customer cant be created!' }
   
   return jsonify(response)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####  API EXAMPLE
####--------------------------------------------------------------------------
####  curl -X GET -H "Content-Type: application/json" -H "Accept: application/json" http://0.0.0.0:7007/api/v1/bussiness/get_all_events/
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
@api_prime.route('/get_all_events/', methods=["GET", "POST"])
def get_all_events():

   all_events = get_all_created_events()

   print(' -----------------------------------------------')
   print('  ----  all_events  ', all_events)
   print(' -----------------------------------------------')

   if all_events:
      response = { 'status': 'success', 'all_events': all_events, 'message': 'Showing all the events!' }
   
   if not all_events:
      response = { 'status': 'error', 'all_events': all_events, 'message': 'Cant show all the events!' }

   return jsonify(response)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

