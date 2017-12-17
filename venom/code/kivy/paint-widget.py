## Understanding Widgets ..

from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.uix.button import Button 
from kivy.graphics import Color, Ellipse, Line

class MyWidget(Widget):
	
	def on_touch_down(self, touch):
		with self.canvas:
			print(touch)
			Color(1,1,0)
			d = 30
			Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d*2,d))
			touch.ud['line'] = Line(points=(touch.x, touch.y))
  

	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]


class MyApp(App):
	
	def build(self):
		# define the parent to hold widget child and button child
		parent = Widget()
		self.childwidget = MyWidget()
		clearbutton = Button(text='Clear Canvas')
		clearbutton.bind(on_release=self.clear_canvas)
		parent.add_widget(self.childwidget)
		parent.add_widget(clearbutton)
		return parent
        


	def clear_canvas(self, obj):
		self.childwidget.canvas.clear()





if __name__ == '__main__':
	MyApp().run()


