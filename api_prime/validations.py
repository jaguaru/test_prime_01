####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

from datetime import datetime

from app import app, mysql


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
def get_room_code(event_code):

    room_code = None

    try:
        cursor = mysql.connection.cursor()
        query = 'SELECT * FROM events WHERE code = "' + str(event_code) + '"'
        cursor.execute(query)
        event = cursor.fetchall()
        cursor.close()

        # print(' ---- event ', event)

        for data in event:
            room_code = data['fk_room_code']

        print(' ---- room_code ', room_code)

        print(' -----------------------------------------------')
        print('  ----  The room_code exist!')
        print(' -----------------------------------------------')
    
    except:
        room_code = None
        print(' -----------------------------------------------')
        print('  ----  The room_code doesnt exist!')
        print(' -----------------------------------------------')

    return room_code

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
def get_room_capacity(room_code):

    room_capacity = None

    try:
        cursor = mysql.connection.cursor()
        query = 'SELECT * FROM rooms WHERE code = "' + str(room_code) + '"'
        cursor.execute(query)
        room = cursor.fetchall()
        cursor.close()

        ##print(' ---- room ', room)

        if not room:
           room_capacity = 0
        else:
           for data in room:
               room_capacity = data['capacity']

        print(' ---- room_capacity ', room_capacity)

        print(' -----------------------------------------------')
        print('  ----  The room_capacity exist!')
        print(' -----------------------------------------------')
    
    except:
        room_capacity = None
        print(' -----------------------------------------------')
        print('  ----  The room_capacity doesnt exist!')
        print(' -----------------------------------------------')

    return room_capacity

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
def get_all_customers_event(fk_event_code):

    num_customers = 0

    try:
        cursor = mysql.connection.cursor()
        query = 'SELECT * FROM events WHERE fk_event_code = "' + str(fk_event_code) + '"'
        cursor.execute(query)
        customers = cursor.fetchall()
        cursor.close()

        ##print('  ----  customers  ', customers)

        if not customers:
           num_customers = 0
           print('  ----  num_customers  A  ', num_customers)
        else:
           num_customers = len(customers)
           print('  ----  num_customers  B  ', num_customers)

        print(' -----------------------------------------------')
        print('  ----  Getting the number of customers!')
        print(' -----------------------------------------------')
    
    except:
        num_customers = 0
        print(' -----------------------------------------------')
        print('  ----  Error - Cant get the number of customers!')
        print(' -----------------------------------------------')

    return num_customers

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
def register_to_event(fk_event_code, fk_customer_code, status):

    created = None

    try:
       cursor = mysql.connection.cursor()
       query_insert = 'INSERT INTO events (fk_event_code, fk_customer_code, status) VALUES (%s, %s, %s)'
       values = (fk_event_code, fk_customer_code, status)
       cursor.execute(query_insert, values)
       mysql.connection.commit()
       cursor.close()

       created = True
       print(' -----------------------------------------------')
       print('  ----  The registrarion to the event is created!')
       print(' -----------------------------------------------')
       ##response = { 'status': 'success', 'customer_register_event_code': code, 'fk_customer_code': fk_customer_code, 'message': 'The registrarion to the event is created!' }
    
    except:
       created = False
       print(' -----------------------------------------------')
       print('  ----  Error - The registrarion to the event cant be created!')
       print(' -----------------------------------------------')
       
       ##response = { 'status': 'error', 'message': 'The registrarion to the event cant be created!' }

    return created

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
def get_all_created_events():

    events = None

    try:
        cursor = mysql.connection.cursor()
        query_events = 'SELECT * FROM events WHERE type = "PUBLIC" AND status = "1"'
        cursor.execute(query_events)
        events = cursor.fetchall()
        cursor.close()

        ##print(' ---- events ', events)

        apnd_events = []

        for data in events:
            event_code = data['code']
            event_name = data['name']
            room_code = data['fk_room_code']

            json_events = { 'event_code': event_code, 'event_name': event_name, 'room_code': room_code }

            apnd_events.append(json_events)
        
        events = apnd_events
        
        print(' -----------------------------------------------')
        print('  ----  events  ', events)
        print(' -----------------------------------------------')  

        print(' -----------------------------------------------')
        print('  ----  The events exist!')
        print(' -----------------------------------------------')
    
    except:
        events = None
        print(' -----------------------------------------------')
        print('  ----  The events doesnt exist!')
        print(' -----------------------------------------------')

    return events

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
def event_cancel(fk_event_code, fk_customer_code, status):

    canceled = None

    try:
        cursor = mysql.connection.cursor()
        query_update = 'UPDATE events SET status = "' + str(status) + '" WHERE fk_event_code = "' + str(fk_event_code) + '" AND fk_customer_code = "' + str(fk_customer_code) + '"'
        cursor.execute(query_update)
        mysql.connection.commit()
        cursor.close()

        canceled = True
        print(' -----------------------------------------------')
        print('  ----  The event is canceled!')
        print(' -----------------------------------------------')
    
    except:
        canceled = False
        print(' -----------------------------------------------')
        print('  ----  Error - The event cant be canceled!')
        print(' -----------------------------------------------')

    return canceled

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
def created_event_cancel(code, status):

    canceled = None

    try:
        cursor = mysql.connection.cursor()
        query_update = 'UPDATE events SET status = "' + str(status) + '" WHERE code = "' + str(code) + '"'
        cursor.execute(query_update)
        mysql.connection.commit()
        cursor.close()

        canceled = True
        print(' -----------------------------------------------')
        print('  ----  The customer registration is canceled!')
        print(' -----------------------------------------------')
    
    except:
        canceled = False
        print(' -----------------------------------------------')
        print('  ----  Error - The customer registration cant be canceled!')
        print(' -----------------------------------------------')

    return canceled

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
def add_customer(code, phone, name, lastname, status):

    added = None

    try:
        cursor = mysql.connection.cursor()
        query_insert = 'INSERT INTO customers (code, phone, name, lastname, status) VALUES (%s, %s, %s, %s, %s)'
        values = (code, phone, name, lastname, status)
        cursor.execute(query_insert, values)
        mysql.connection.commit()
        cursor.close()

        added = True
        print(' -----------------------------------------------')
        print('  ----  The customer is created!')
        print(' -----------------------------------------------')
        ##response = { 'status': 'success', 'customer_code': code, 'message': 'The customer is created!' }
    
    except:
        added = False
        print(' -----------------------------------------------')
        print('  ----  Error - The customer cant be created!')
        print(' -----------------------------------------------')
        ##response = { 'status': 'error', 'message': 'The customer cant be created!' }

    return added

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
def creating_event(code, name, type, status, fk_room_code):

    created = None

    try:
        cursor = mysql.connection.cursor()
        query_insert = 'INSERT INTO events (code, name, type, status, fk_room_code) VALUES (%s, %s, %s, %s, %s)'
        values = (code, name, type, status, fk_room_code)
        cursor.execute(query_insert, values)
        mysql.connection.commit()
        cursor.close()

        created = True
        print(' -----------------------------------------------')
        print('  ----  The event is created!')
        print(' -----------------------------------------------')
        ##response = { 'status': 'success', 'event_code': code, 'event_name': name, 'event_type': type, 'message': 'The event is created!' }
    
    except:
        created = False
        print(' -----------------------------------------------')
        print('  ----  Error - The event cant be created!')
        print(' -----------------------------------------------')
        ##response = { 'status': 'error', 'message': 'The event cant be created!' }

    return created

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
def creating_room(code, name, capacity, status):

    created = None

    try:
        cursor = mysql.connection.cursor()
        query_insert = 'INSERT INTO rooms (code, name, capacity, status) VALUES (%s, %s, %s, %s)'
        values = (code, name, capacity, status)
        cursor.execute(query_insert, values)
        mysql.connection.commit()
        cursor.close()

        created = True
        print(' -----------------------------------------------')
        print('  ----  The room is created!')
        print(' -----------------------------------------------')
        ##response = { 'status': 'success', 'room_name': name, 'room_code': code, 'message': 'The room is created!' }
    
    except:
        created = False
        print(' -----------------------------------------------')
        print('  ----  Error - The room cant be created!')
        print(' -----------------------------------------------')
        ##response = { 'status': 'error', 'message': 'The room cant be created!' }

    return created

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

