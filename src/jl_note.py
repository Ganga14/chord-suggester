from pychord_jl.constants.scales import NOTE_VAL_DICT
from math import cos,sin,pi

class Note:
    NUMBER_OF_NOTES = 12
    STEP_ANGLE = 360.0 / NUMBER_OF_NOTES
    def __init__(self, str_value):
        self.str_value = str_value
        self.pychord_value = NOTE_VAL_DICT[str_value]

    @property
    def position_in_5th_circle(self):
        return (self.pychord_value * 7) % 12

    @property
    def angle_in_5th_circle_degrees(self):
        return self.position_in_5th_circle * self.STEP_ANGLE

    # https://towardsdatascience.com/feature-engineering-time-3934038e0dbe
    @property
    def x_y_in_5th_circle(self):
        angle_radians = (self.angle_in_5th_circle_degrees * pi) / 180

        return (
            sin(angle_radians),
            cos(angle_radians)
        )
    
    def __sub__(self,other):
        self_x_y = self.x_y_in_5th_circle
        other_x_y = other.x_y_in_5th_circle

        return (
            self_x_y[0] - other_x_y[0],
            self_x_y[1] - other_x_y[1],
        )

    def __str__(self):
        return self.str_value
