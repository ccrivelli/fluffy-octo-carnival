from kivy.app import App 
from kivy.uix.widget import Widget 

'''
Simply create:
- a Widget that is doing nothing
- the App that is returning the Widget
- run the app in main


kv file is pong.kv

'''
class PongWidget(Widget):
	pass


class PongApp(App):
	def build(self):
		return PongWidget()

if __name__ == '__main__':
	PongApp().run()



