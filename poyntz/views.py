from flask import render_template

from .app import app
from .models import Point

#from .point_tracking import Ladder, Point


#ladder = Ladder(max_points=6)


@app.route("/")
def home():
    return "Nick's Point Tracking Prototype"


# @app.route("/add/<point_type>")
# def point_type(point_type):
#     if not hasattr(Point, point_type):
#         abort(404)
    
#     # Get the requested point and add it to the list
#     point = getattr(Point, point_type)
    
#     try:
#         ladder.add_point(point)
#         return('Added {} point'.format(point_type))
#     except Exception as e:
#         return str(e)


# @app.route("/points")
# def view_points():
#     return str(ladder)
