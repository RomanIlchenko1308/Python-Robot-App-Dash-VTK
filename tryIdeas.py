# value = 10
#
# print(not (0 <= value <= 4))
#
# vec_direction = "north"
#
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


obj2 = Hello(1, 1)


# -------------------------------------------------ç
vector_deg = {
    "NORTH": 0,
    "EAST": 90,
    "SOUTH": 180,
    "WEST": 270
}
print(vector_deg["NORTH"])
