from flask import render_template, request, jsonify
from app import app

from app.models.formsearch import SearchProduct
from app.components import functions


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    list_products = []
    form_search = SearchProduct()
    print(form_search.category)
    print(form_search.searchType.data)
    print(list_products)
    if form_search.searchType.data == 'cat':
        if form_search.site.data == 'ml':
            list_products = functions.getQueryMercadoLibre('', form_search.category.data)
        elif form_search.site.data == 'bp':
            list_products = functions.getQueryBuscape('', form_search.category.data)

    else:
        if form_search.site.data == 'ml':
            if form_search.query.data:
                list_products = functions.getQueryMercadoLibre(form_search.query.data)
        elif form_search.site.data == 'bp':
            list_products = functions.getQueryBuscape(form_search.query.data)

    return render_template('index.html', products=list_products, form=form_search)


@app.route('/mercadolibre', methods=['POST'])
def mercadolibre():
    list_products = []
    params = request.form
    query = params.get('query')
    category = params.get('category')
    site = params.get('site')
    if query:
        if site and site == 'ml':
            if query:
                list_products = functions.getQueryMercadoLibre(query)

    if len(list_products) > 0:
        return jsonify(list_products)
    else:
        return jsonify({'error': 'nothing found'})


@app.route('/buscape', methods=['POST'])
def buscape():
    list_products = []
    params = request.form
    query = params.get('query')
    category = params.get('category')
    site = params.get('site')
    if query:
        if site and site == 'ml':
            if query:
                list_products = functions.getQueryBuscape(query)
        elif site and site == 'bp':
            pass

    if len(list_products) > 0:
        return jsonify(list_products)
    else:
        return jsonify({'error': 'nothing found'})