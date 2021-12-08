import random as rand

class playerMovement():

    def __init__(self) -> None:
        pass

    def up(self):
        return -2

    def down(self):
        return 2

    def left(self):
        return -1

    def right(self):
        return 1

    def rand_mv_square(self):
        self.up()
        pos = 1
        while True:
            if pos == 1:
                pos = pos + rand.choice([self.down, self.right])()
            elif pos == 2:
                pos = pos + rand.choice([self.down, self.left])()
            elif pos == 3:
                pos = pos + rand.choice([self.up, self.right])()
            elif pos == 4:
                pos = pos + rand.choice([self.up, self.left])()
            print(pos)

pmv = playerMovement()


pmv.rand_mv_square()
