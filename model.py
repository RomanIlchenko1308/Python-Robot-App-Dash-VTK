# -----------------------------------------------------------------------------
# PythonRobotApp

class Robot:

    def __init__(self, x=0, y=0, f="NORTH"):
        print("--> __init__ Robot")
        self.coord_x = x
        self.coord_y = y
        self.vector_f = f

    # getters
    @property
    def coord_x(self):
        print("--> coordX getter Robot")
        return f"My coordinate x is {self.x}"

    @property
    def coord_y(self):
        print("--> coordY getter Robot")
        return f"My coordinate y is {self.y}"

    @property
    def vector_f(self):
        print("--> vector_f getter Robot")
        return f"Vector orientation x is {self.f}"

    # setters
    @coord_x.setter
    def coord_x(self, x_value):
        print("--> coord_x setter Robot")

        # check coordinate value
        if not (0 <= x_value <= 4):
            raise ValueError("F***ck get you right coordinate between 0 and 4")

        self.x = x_value


    @coord_y.setter
    def coord_y(self, y_value):
        print("--> coord_y setter Robot")
        # check coordinate value
        if not (0 <= y_value <= 4):
            raise ValueError("F***ck get you right coordinate between 0 and 4")

        self.y = y_value

    @vector_f.setter
    def vector_f(self, vec_direction):
        print("--> vector_f setter Robot")
        # check coordinate valueNORTH, SOUTH, EAST or WEST
        if not (vec_direction.upper()  in ["NORTH", "SOUTH", "EAST", "WEST"]):
            raise ValueError("F***ck get you right vector direction between: 'NORTH', 'SOUTH', 'EAST', 'WEST'")

        self.f = vec_direction


print("\n------------------")
obj1 = Robot(0, 0, "SOUTH")

print("\n------------------")
print(obj1.coord_x)
print(obj1.coord_y)
print(obj1.vector_f)
