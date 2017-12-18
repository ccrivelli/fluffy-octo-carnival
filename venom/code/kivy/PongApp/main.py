from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock 
from random import randint 



'''
Simply:
- create a Widget doing nothing
- create the App returning the Widget
- run the app in main


kv file is pong.kv

----------------------------------------------------
Layouts are containers used to arrange widgets.
Each widget has a canvas, i.e. a place to draw on.

'''
class PongGame(Widget):
    '''
    ObjectPropery needed to reference to the PongBall inside the kv file

    in the kv file need to give the id of the pong ball and define the 'ball' var to reference to that id
    '''

    ball = ObjectProperty(None)

    def update(self, dt):
        self.ball.move()

    def serve_ball(self):
        self.ball.center = self.center 
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))


class PongBall(Widget):
    '''
    The Properties classes are used when you create an EventDispatcher.

    Class Events
    -------------
    Our base class EventDispatcher, used by Widget, uses the power of our Properties for dispatching changes. 
    This means when a widget changes its position or size, the corresponding event is automatically fired.

    '''
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    '''
    class kivy.properties.ReferenceListProperty
    Bases: kivy.properties.Property

    Property that allows the creation of a tuple of other properties.

    For example, if x and y are NumericPropertys, we can create a ReferenceListProperty for the pos. 
    If you change the value of pos, it will automatically change the values of x and y accordingly. 
    If you read the value of pos, it will return a tuple with the values of x and y.
    '''
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    '''
    Module: kivy.vector
    The Vector represents a 2D vector (x, y). Our implementation is built on top of a Python list.
    
    called in equal intervals to animate the ball
    '''
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos









class PongApp(App):
    '''
    Clock Event - to make the ball moving
    update function of the game object to be called once every 60th of a second (60 times per second).

    Method update defined inside the PongGame class to do more then just move the ball
    '''
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game



if __name__ == '__main__':
    PongApp().run()



