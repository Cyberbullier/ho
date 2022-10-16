from flask import Flask, request, jsonify
import os
import json
# import flask_cors
######## config###########
inventory_file_path = os.path.join(os.path.dirname(__file__), "inventory.json")


api = Flask(__name__, static_url_path='', static_folder='../build')
# flask_cors.CORS(api) #comment this on deployment
CONFIG = {"headers": {
'Access-Control-Allow-Origin': '*',
'Content-Type': 'application/json',
}}
# api = Flask(__name__)
##########################

def write_json(path, json_data):
    with open(path, 'w') as file_out:
        json.dump(json_data, file_out)


def read_json(path):
    with open(path) as file_in:
        return json.load(file_in)


############ API ENDPOINTS ########
@api.route('/')
def home():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    api.logger.debug("home request")

    return response_body


@api.route('/decrement-stock', methods = ['POST'])
# @cross_origin()
def decrement_stock():
    api.logger.debug("/decrement-stock")

    # input from form or wherever your new JSON is coming from...
    # It could also be coming from a REST API etc:
    # input = request.form['data']
    # {"new": "data"}


    # read in existing JSON
    existing_json = read_json(inventory_file_path)

    # product_name = "Enoki"
    payload = request.get_json()

    product_name = payload["name"]


    # add new JSON to existing JSON however you see fit
    stock = existing_json[product_name]["stock"] -  1
    api.logger.debug(f"current stock: {stock + 1}")
    if stock <0:
        # dont update
        response_body = {
            "current_stock": stock,
            "added": 0
        }
    else:
        existing_json[product_name]['stock'] = stock
        response_body = {
            "current_stock": stock,
            "added": 1
        }

    # now update datastore
    write_json(inventory_file_path, existing_json)
    return jsonify(response_body)

@api.route('/increment-stock', methods = ['POST'])
def increment_stock():
    api.logger.debug("/increment-stock")

    # input from form or wherever your new JSON is coming from...
    # It could also be coming from a REST API etc:
    # input = request.form['data']
    # {"new": "data"}


    # read in existing JSON
    existing_json = read_json(inventory_file_path)
    api.logger.debug(request)


    payload = request.get_json()
    product_name = payload["name"]


    # add new JSON to existing JSON however you see fit
    stock = existing_json[product_name]["stock"] +  1
    existing_json[product_name]['stock'] = stock
    response_body = {
        "current_stock": stock,
        "removed": 1
    }
    # now update datastore
    write_json(inventory_file_path, existing_json)
    return jsonify(response_body)




