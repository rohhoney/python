class Bird:
    def fly(self):
        raise NotImplementedError

error = """class Eagle(Bird):
    pass

eagle = Eagle()

eagle.fly()
"""

class Eagle(Bird):
    def fly(self):
        print("Fast")

eagle = Eagle()

eagle.fly()