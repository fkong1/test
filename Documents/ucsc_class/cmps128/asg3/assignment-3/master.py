from flask import Flask, make_response, request
import os
import json
import sys

def create_app(db, endpoint='/keyValue-store'):
    app = Flask(__name__)

    def make_payload():
        return {}

    def create_response(code, msg):
        resp = make_response(json.dumps(msg), code)
        resp.headers['Response-Type'] = 'application/json'
        return resp

    @app.route(endpoint + '/<key>', methods=['GET'])
    def on_search(key):
        value = db.get(key)
        if value is None:
            return create_response(404, {
                'result': 'Error',
                'msg' : 'Key does not exist'
                #need payload?
            }        
        payload = request.form['payload'] if 'payload' in request.form else make_payload()
        exists = db.exists(subject)
        if not exists:
            return create_response(404, {
                'result': 'Error',
                'msg' : 'Key does not exist'
                'payload' : payload
            })
        return create_response(200, {
            'result': 'Success',
            'value' : value
            'payload' : payload
        })
    
    @app.route(endpoint + '/<subject>', methods=['GET'])
    def on_get(subject):
        exists = db.exists(subject)
        if not exists:
            return create_response(404, {
                'result': 'Error',
                'value': 'Not Found'
            })
        return create_response(200, {
            'result': 'Success',
            'value': db.get(subject)
        })

    @app.route(endpoint + '/<subject>', methods=['PUT'])
    def on_put(subject):
        if len(subject) > 200:
            return create_response(422, {
                "msg": "Key not valid",
                "result": "Error"
            })

        if 'val' not in request.form:
            return create_response(422, {
                "msg": "Corrupted PUT Request. Missing val in form.",
                "result": "Error"
            }) # precondition of request.form['val']

        value = request.form['val']

        if sys.getsizeof(value) > 1000000:
            return create_response(422, { # From Piazza spec comment
                "msg": "Object too large. Size limit is 1MB",
                "result": "Error"
            })

        if db.put(subject, value):
            return create_response(200, { 
                "replaced": "True",
                "msg": "Updated successfully"
            })
        return create_response(201, {
            "replaced": "False",
            "msg": "Added successfully"
        })

    @app.route(endpoint + '/<subject>', methods=['DELETE'])
    def on_delete(subject):
        if not db.delete(subject):
            return create_response(404, {
                "result": "Error",
                "msg": "Status code 404"
            })
        return create_response(200, {"result": "Success"})

    @app.route(endpoint, methods=['COUNT'])
    def on_count():
        return create_response(200, {"result": "Success", "msg": db.count()})

    return app
