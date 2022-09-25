# value = 10
#
# print(not (0 <= value <= 4))
#
# vec_direction = "north"
# print("\n--------------------")
# print(vec_direction.upper() in ["NORTH", "SOUTH", "EAST", "WEST"])

# ------
class Hey:
    def __init__(self, x=0, y=0):
        print("--> __init__ Hey")
        self.x = x
        self.y = y
        print("--> ", self.x, self.y)


class Hello(Hey):
    def __init__(self, x, y):
        print("--> __init__ Hello")
        super().__init__(x, y)
        self.f = "North"
        self.print_out()

    def print_out(self):
        print("--> print_out Hello")
        print(f"{self.x}, {self.y}, {self.f}")

print("\n--------------------")
obj2 = Hello(1, 1)


# # -------------------------------------------------ç
# vector_deg = {
#     "NORTH": 0,
#     "EAST": 90,
#     "SOUTH": 180,
#     "WEST": 270
# }
#
# print(vector_deg["NORTH"])


class Rotate:
    __vector_deg = {
        "NORTH": 0,
        "EAST": 90,
        "SOUTH": 180,
        "WEST": 270
    }

    def __init__(self):
        print("--> __init__ Rotate")
        self.current_angle = self.__vector_deg["NORTH"]

    def rot_left(self):
        print("--> rot_left Rotate")
        self.current_angle -= 90
        return f"The current angle is: {self.current_angle}"

    def rot_right(self):
        print("--> rot_left Rotate")
        self.current_angle += 90
        return f"The current angle is: {self.current_angle}"

print("\n--------------------")
rot_obj1 = Rotate()
print(rot_obj1.current_angle)
print(rot_obj1.rot_left())
print(rot_obj1.rot_left())
print(rot_obj1.rot_left())
print(rot_obj1.current_angle)