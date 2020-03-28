import pytest
from ..point_tracking import Point, Ladder


def test_ladder():
    # Create a test with 5 possible points
    points = Ladder(max_points = 5)
    
    points.add_point(Point.good)
    points.add_point(Point.good)
    points.add_point(Point.excellent)
    points.add_point(Point.need_improvement)
    points.add_point(Point.naughty)

    # Check that we can't add more than the specified number of points
    with pytest.raises(Exception):
        points.add_point(Point.add)

    # Check we have the right number of points
    assert len([p for p in points.ladder if p.value is Point.good.value]) == 2
    assert len([p for p in points.ladder if p.value is Point.excellent.value]) == 1
    assert len([p for p in points.ladder if p.value is Point.need_improvement.value]) == 1
    assert len([p for p in points.ladder if p.value is Point.naughty.value]) == 1

    points.reset()
    assert len(points.ladder) == 0

    pass
