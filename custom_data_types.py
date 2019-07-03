class Point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)
         

p = Point(5, 3)
q = Point(-1, 0)

print("p", p)
print("q", q)
print("p+q", p.add(q))