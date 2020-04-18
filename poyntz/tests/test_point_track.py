import pytest
from ..point_tracking import *
from ..app import *
import os


def cleanup_database():
    """
    Clean up test database file if it exists
    """
    db_file = app.config.get('DATABASE')['name']
    if os.path.exists(db_file):
        print('Cleaning up database file {}'.format(db_file))
        os.remove(db_file)
    else:
        print('Unable to find {} for cleanup'.format(db_file))


@pytest.fixture(autouse=True)
def test_database_setup():
    cleanup_database()
    create_tables()
    yield
    # Delete the test database
    print('Finalising')
    cleanup_database()
    

def test_ladder():
    # Adding a point type that isn't supported should fail
    with pytest.raises(Exception):
        award_point(allowed_categories[0], 'make_up_point_type')
    # Adding a category type that isn't supported should fail
    with pytest.raises(Exception):
        award_point('made_up_category', allowed_point_types[0])

    # Add 'good' points for all categories for today
    for category in allowed_categories:
        award_point(category, allowed_point_types[0])
    
    # Check that the points for today are in the database
    today = points_today()
    assert len(today) == len(allowed_categories)

    pass
