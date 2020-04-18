from flask import render_template, jsonify, abort, request, Response

from .app import app
from .models import Point
from .point_tracking import *

import json


@app.route("/")
def home():
    word_mapping = {
        'good': 'Good',
        'excellent': 'Excellent',
        'need_improvement': 'Need Improvement',
        'bad': 'Bad',
    }
    return render_template('index.html', 
        categories=allowed_categories,
        point_types=allowed_point_types,
        word_mapping=word_mapping,
    )


@app.route("/summary")
def summary():
    summary = get_summary()
    return jsonify(summary)


@app.route("/award", methods=['POST'])
def award():
    # Extract important fields
    if 'category' not in request.args:
        abort(400, description='category data missing from query')
    
    if 'point_type' not in request.args:
        abort(400, description='point_type data missing from query')

    category = request.args.get('category')
    point_type = request.args.get('point_type')

    if ' a' in point_type:
        point_type = point_type.replace(' a', '')
        point_type = point_type.strip()

    try:
        award_point(category, point_type)
    except Exception as e:
        abort(400, description=str(e))

    return Response('Awarded {} to {}'.format(point_type, category))
