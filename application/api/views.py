"""
views.py

URL route handlers

"""

from application.api import app
from application.decorators import cached, json_response, api_key_required
from flask import make_response, redirect, url_for
from flask.views import View

from application.models import Product
from application.funcs import random_key




"""
API methods
"""

@app.route('/products/',methods=['GET'])
@json_response
def list_products():
	products = Product.all().get()
	return products


@app.route('/products/',methods=['POST'])
@api_key_required
@json_response
def create_product(product_id=None,product_name=None):
	if product_id is None or len(product_id) <= 3:
		product_id = random_key(10)

	product = Product(product_id=product_id,product_name=product_name)
	product.put()
	import logging
	logging.error(product.properties())
	return product




"""
Redirects
"""


@app.route( '/' )
@cached
def api():
	return redirect(url_for('api_docs'))