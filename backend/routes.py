from flask import Flask, request
import os
import json
######## config###########
api = Flask(__name__)
inventory_file_path = os.path.join(os.path.dirname(__file__), "inventory.json")
##########################

def write_json(path, json_data):
    with open(path, 'w') as file_out:
        json.dump(json_data, file_out)


def read_json(path):
    with open(path) as file_in:
        return json.load(file_in)


############ ENOKI ENDPOINTS########
@api.route('/add-enoki')
def add_enoki():

    # input from form or wherever your new JSON is coming from...
    # It could also be coming from a REST API etc:
    # input = request.form['data']
    # {"new": "data"}


    # read in existing JSON
    existing_json = read_json(inventory_file_path)
    # {"existing": "json"}


    # add new JSON to existing JSON however you see fit
    stock = existing_json["enoki"]["stock"] -  1
    if stock <=0:
        # dont update
        response_body = {
            "current_stock": stock,
            "recieved": 0
        }
    else:
        existing_json['enoki']['stock'] = stock
        response_body = {
            "current_stock": stock,
            "recieved": 1
        }

    # now update datastore
    write_json(inventory_file_path, existing_json)
    return response_body

@api.route('/remove-from-cart-enoki')
def remove_enoki():

    # input from form or wherever your new JSON is coming from...
    # It could also be coming from a REST API etc:
    # input = request.form['data']
    # {"new": "data"}


    # read in existing JSON
    existing_json = read_json(inventory_file_path)
    # {"existing": "json"}


    # add new JSON to existing JSON however you see fit
    stock = existing_json["enoki"]["stock"] +  1
    existing_json['enoki']['stock'] = stock
    response_body = {
        "current_stock": stock,
        "removed": 1
    }
    # now update datastore
    write_json(inventory_file_path, existing_json)
    return response_body




############ OYSTER ENDPOINTS########

@api.route('/add-enoki')
def add_enoki():

    # input from form or wherever your new JSON is coming from...
    # It could also be coming from a REST API etc:
    # input = request.form['data']
    # {"new": "data"}


    # read in existing JSON
    existing_json = read_json(inventory_file_path)
    # {"existing": "json"}


    # add new JSON to existing JSON however you see fit
    stock = existing_json["enoki"]["stock"] -  1
    if stock <=0:
        # dont update
        response_body = {
            "current_stock": stock,
            "recieved": 0
        }
    else:
        existing_json['enoki']['stock'] = stock
        response_body = {
            "current_stock": stock,
            "recieved": 1
        }

    # now update datastore
    write_json(inventory_file_path, existing_json)
    return response_body

@api.route('/remove-from-cart-enoki')
def remove_enoki():

    # input from form or wherever your new JSON is coming from...
    # It could also be coming from a REST API etc:
    # input = request.form['data']
    # {"new": "data"}


    # read in existing JSON
    existing_json = read_json(inventory_file_path)
    # {"existing": "json"}


    # add new JSON to existing JSON however you see fit
    stock = existing_json["enoki"]["stock"] +  1
    existing_json['enoki']['stock'] = stock
    response_body = {
        "current_stock": stock,
        "removed": 1
    }
    # now update datastore
    write_json(inventory_file_path, existing_json)
    return response_body
