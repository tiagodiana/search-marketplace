from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, HiddenField
from wtforms.validators import DataRequired


class SearchProduct(FlaskForm):
    query = StringField('query')
    category_choices = [('', 'Selecione a categoria'), ('celular', 'Celular'), ('geladeira', 'Geladeira'), ('tv', 'Televisores')]
    category = SelectField('category', choices=category_choices)
    site_choices = [('ml', 'Mercado Livre'), ('bp', 'Buscapé')]
    site = SelectField('site', choices=site_choices)
    searchType = HiddenField('searchType')
