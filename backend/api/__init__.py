from flask import Flask
from api.lib.orm import build_from_record, find, find_all, find_all_by_lastname
from api.lib.db import test_conn, cursor, get_db, test_cursor
from api.models import *
import json
import psycopg2

def create_app(database, user, password):
    app = Flask(__name__)
    app.config['DATABASE'] = database
    app.config['DB_USER'] = user
    app.config['DB_PASSWORD'] = password
    
    @app.route('/')
    def home():
        return "welcome to the adventureworks app"
    
    @app.route('/persons')
    def persons():
        persons = find_all(test_cursor, Person)
        return [person.__dict__ for person in persons]
    
    @app.route('/persons/lastname/<lastname>')
    def persons_by_lastname(lastname):
        persons = find_all_by_lastname(test_cursor, lastname, Person)
        return [person.__dict__ for person in persons]

    @app.route('/addresses')
    def addresses():
        addresses = find_all(test_cursor, Address)
        return [addres.__dict__ for addres in addresses]
    
    @app.route('/person/addresses/<id>')
    def addresses_by_id(id):
        addresses = find_all(test_cursor, Address, id)
        person_with_addresses = find(test_cursor, Person, id)
        person_with_addresses.__dict__.update({'addresses': [address.__dict__ for address in addresses]})
        return person_with_addresses.__dict__

    return app