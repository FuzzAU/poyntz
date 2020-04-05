from .models import Point
from peewee import fn
import pendulum
import datetime

# The types of points that can be awarded
allowed_point_types = ['good', 'excellent', 'need_improvement', 'bad']
# Categories where points can be awarded
allowed_categories = ['listening', 'packing_up', 'eating', 'sleeping', 'learning']


def to_native_date(pendulum_date):
    """
    Convert from pendulum date to a native date as peewee doesn't support
    """
    d = datetime.date(year=pendulum_date.year, month=pendulum_date.month, day=pendulum_date.day)
    return d


def add_point(category : str, point_type : str, awarded_date : datetime.date = None):
    if category not in allowed_categories:
        raise Exception('Category provided is not in the allowed list')

    if point_type not in allowed_point_types:
        raise Exception('Point type provided is not in the allowed list')
    
    if awarded_date is None:
        point = Point(category=category, point_type=point_type)
    else:
        point = Point(category=category, point_type=point_type, awarded_date = awarded_date)
    point.save()


def get_all_points():
    return list(Point.select())


def points_today():
    today_points = Point.select().where(Point.awarded_date==datetime.datetime.now()).order_by(Point.awarded_date, Point.category)
    return list(today_points)


def summary_by_point_type_for_period(period : str):
    """
    Get a count of points for a given category over a specified period type
    """
    now = pendulum.now()
    q = Point.select(Point.point_type, fn.COUNT(Point.point_type).alias('num_points')).where(
        (Point.awarded_date >= to_native_date(now.start_of(period))) & 
        (Point.awarded_date <= to_native_date(now.end_of(period)))
    ).group_by(Point.point_type)
    return q


def get_summary():
    week_summary = summary_by_point_type_for_period('week')
    month_summary = summary_by_point_type_for_period('month')

    week_summary_dict = {p.point_type:p.num_points for p in week_summary}
    month_summary_dict = {p.point_type:p.num_points for p in month_summary}
    return {'month': month_summary_dict, 'week': week_summary_dict}

