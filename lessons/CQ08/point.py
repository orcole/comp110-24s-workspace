from __future__ import annotations

"""Create Point class."""

__author__ = "730547498"


class Point: 
    """Creating Point class."""
    # attributes
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float): 
        """Defining the contructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None: 
        """Updating the point by the new factor."""
        self.x = self.x * factor  # x = x * factor 
        self.y = self.y * factor  # y = y * factor

    def scale(self, factor: int) -> Point:  
        """Updating the point again by the factor."""
        p1: Point = Point(self.x * factor, self.y * factor)
        return p1