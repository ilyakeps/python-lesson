class Turtle:

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.y += 1

    def degrade(self):
        if self.s <= 0:
            raise ValueError("Невозможно")
        self.y -= 1

    def pr(self):
        print(self.x, self.y, self.s)

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        steps_x = dx // self.s
        steps_y = dy // self.s

        rem_x = dx % self.s
        rem_y = dy % self.s

        total_steps = steps_x + steps_y
        if rem_x != 0:
            total_steps += 1
        if rem_y != 0:
            total_steps += 1

        return total_steps

turtle = Turtle(1,2,3)
turtle.go_up()
turtle.evolve()
turtle.degrade()
turtle.pr()


