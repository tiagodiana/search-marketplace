from flask import request, jsonify
from flask_cors import cross_origin
from app import app
import json


from app.components import functions
from app.components import dbconnection


@app.route('/queryMarketplace', methods=['POST'])
def queryMarketplace():
    global count

    list_products = []
    params = request.get_json()

    query = ''
    if params['type'] == 'cat':
        if params['site'] == 'ml':
            list_products = functions.getQueryMercadoLibre('', params['category'])
        elif params['site'] == 'bp':
            list_products = functions.getQueryBuscape('', params['category'])
        query = params['category']
    else:
        if params['query']:
            if params['site'] == 'ml':
                list_products = functions.getQueryMercadoLibre(params['query'])
            elif params['site'] == 'bp':
                list_products = functions.getQueryBuscape(params['query'])
            query = params['query']
    db_params = (
        request.remote_addr,
        params['site'],
        params['type'],
        query,
        json.dumps(list_products)
    )
    dbconnection.insertResearches(db_params)
    return jsonify(list_products)


@app.route('/researches', methods=['GET'])
@cross_origin()
def researches():
    result = dbconnection.selectResearches()
    return jsonify(result)


@app.route('/researches/<idresearches>', methods=['GET'])
@cross_origin()
def researchesId(idresearches):
    result = dbconnection.selectResearchesId(idresearches)
    result['result'] = json.loads(result['result'])
    return jsonify(result)
