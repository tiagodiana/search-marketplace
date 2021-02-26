from flask import  render_template, request, jsonify
from flask_cors import  cross_origin
from app import app
import json



from app.models.formsearch import SearchProduct
from app.components import functions
from app.components import dbconnection

count = 0
#
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     list_products = []
#     form_search = SearchProduct()
#     print(form_search.category)
#     print(form_search.searchType.data)
#     print(list_products)
#     if form_search.searchType.data == 'cat':
#         if form_search.site.data == 'ml':
#             list_products = functions.getQueryMercadoLibre('', form_search.category.data)
#         elif form_search.site.data == 'bp':
#             list_products = functions.getQueryBuscape('', form_search.category.data)
#
#     else:
#         if form_search.site.data == 'ml':
#             if form_search.query.data:
#                 list_products = functions.getQueryMercadoLibre(form_search.query.data)
#         elif form_search.site.data == 'bp':
#             list_products = functions.getQueryBuscape(form_search.query.data)
#
#     return render_template('index.html', products=list_products, form=form_search)
#

@app.route('/queryMarketplace', methods=['POST'])
def queryMarketplace():
    global count
    print(request.method)
    print(count)
    if count == 0 and request.method == 'POST':
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
            if params['site'] == 'ml':
                if params['query']:
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
    else:
        zerocount()
    count += 1


def zerocount():
    global count
    count = 0

@app.route('/testedb', methods=['GET'])
def testedb():
    print(dbconnection.selectResearches())
    return 'teste db'
