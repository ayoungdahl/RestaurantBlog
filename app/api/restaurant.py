from flask import jsonify, request
from app.api import bp
from app.models import Restaurant

@bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    return jsonify(Restaurant.to_collection(Restaurant.query, page, per_page, 'api.get_restaurants'))