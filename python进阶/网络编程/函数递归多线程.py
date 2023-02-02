
import math
import threading
from queue import Queue
from turtle import Turtle, Screen


class Location:
    def __init__(self, xpos=0, ypos=0, heading=90):
        self.xpos = xpos
        self.ypos = ypos
        self.heading = heading

    def clone(self):
        return Location(self.xpos, self.ypos, self.heading)


class Terrapin(Turtle):
    def tolocation(self, location):
        tm.q.put((self.penup,))
        tm.q.put((self.setx, location.xpos))
        tm.q.put((self.sety, location.ypos))
        tm.q.put((self.setheading, location.heading))
        tm.q.put((self.pendown,))

    def draw_tree(self, startpos, size=100):  # 递归
        if size < 1:
            return

        self.tolocation(startpos)

        tm.q.put((self.forward, size))

        angle = math.radians(startpos.heading)
        startpos.xpos += size * math.cos(angle)
        startpos.ypos += size * math.sin(angle)

        tm.q.put((self.right, 45))
        startpos.heading -= 45

        tm.new_thread(pond.get().draw_tree, startpos.clone(), size / 2)

        tm.q.put((self.left, 90))
        startpos.heading += 90

        self.draw_tree(startpos, size / 2)

        pond.put(self)  # finished with this turtle, return it to pond


class ThreadManager:
    def __init__(self):
        self.q = Queue()
        self.threads = Queue()

    def new_thread(self, method, *arguments):
        thread = threading.Thread(target=method, args=arguments)
        thread.daemon = True
        thread.start()
        self.threads.put(thread)

    def process_queue(self):
        while not self.q.empty():
            command, *arguments = self.q.get()
            command(*arguments)

        if threading.active_count() > 1:
            screen.ontimer(self.process_queue, 100)


screen = Screen()

# Allocate all the turtles we'll need ahead as turtle creation inside
# threads calls into Tk which fails if not running in the main thread
pond = Queue()

for _ in range(100):
    turtle = Terrapin(visible=False)
    turtle.speed('fastest')
    pond.put(turtle)

tm = ThreadManager()

tm.new_thread(pond.get().draw_tree, Location())

tm.process_queue()

screen.exitonclick()