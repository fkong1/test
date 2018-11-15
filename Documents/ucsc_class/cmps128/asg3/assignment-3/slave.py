from flask import Flask, make_response, request
import requests
import json

def create_app(mainip, endpoint='/keyValue-store'):
    app = Flask(__name__)

    def create_response_helper(response):
        msg = json.loads(response.text)
        code = response.status_code
        resp = make_response(json.dumps(msg), code)
        resp.headers['Response-Type'] = 'application/json'
        return resp

    @app.route(endpoint + '/search' + '/<subject>', methods=['GET'])
    def on_search(subject):
        return create_response_helper(requests.get('http://' + mainip + endpoint + '/' + subject)) 

    @app.route(endpoint + '/<subject>', methods=['GET'])
    def on_get(subject):
        return create_response_helper(requests.get('http://' + mainip + endpoint + '/' + subject)) 

    @app.route(endpoint + '/<subject>', methods=['PUT'])
    def on_put(subject):
        value = request.form['val']
        return create_response_helper(requests.put(
            'http://' + mainip + endpoint + '/' + subject,
            data={'val': value})) 

    @app.route(endpoint + '/<subject>', methods=['DELETE'])
    def on_delete(subject):
        return create_response_helper(requests.delete('http://' + mainip + '/keyValue-store/' +
                               subject) ) 

    @app.route(endpoint, methods=['COUNT'])
    def on_count():
        return create_response_helper(requests.request(
            'COUNT', 'http://' + mainip + '/keyValue-store/' + subject)) 

    return app

