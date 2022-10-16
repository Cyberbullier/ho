from flask import Flask, request, jsonify, send_from_directory
import os
import json
# import flask_cors
######## config###########
inventory_file_path = os.path.join(os.path.dirname(__file__), "inventory.json")


app = Flask(__name__, static_url_path='/', static_folder='../build')
# flask_cors.CORS(app) #comment this on deployment
CONFIG = {"headers": {
'Access-Control-Allow-Origin': '*',
'Content-Type': 'application/json',
}}
##########################

def write_json(path, json_data):
    with open(path, 'w') as file_out:
        json.dump(json_data, file_out)


def read_json(path):
    with open(path) as file_in:
        return json.load(file_in)


############ app ENDPOINTS ########
@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')



@app.route('/decrement-stock', methods = ['POST'])
def decrement_stock():
    app.logger.debug("/decrement-stock")

    # input from form or wherever your new JSON is coming from...
    # It could also be coming from a REST app etc:
    # input = request.form['data']
    # {"new": "data"}


    # read in existing JSON
    existing_json = read_json(inventory_file_path)

    # product_name = "Enoki"
    payload = request.get_json()

    product_name = payload["name"]


    # add new JSON to existing JSON however you see fit
    stock = existing_json[product_name]["stock"] -  1
    app.logger.debug(f"current stock: {stock + 1}")
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

@app.route('/increment-stock', methods = ['POST'])
def increment_stock():
    app.logger.debug("/increment-stock")

    # input from form or wherever your new JSON is coming from...
    # It could also be coming from a REST app etc:
    # input = request.form['data']
    # {"new": "data"}


    # read in existing JSON
    existing_json = read_json(inventory_file_path)
    app.logger.debug(request)


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




