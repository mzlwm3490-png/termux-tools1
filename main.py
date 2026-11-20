from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from code import Dd
#Builder.load_file('myapp.kv')

class Myapp(App):
	def build(self):
		return Dd()
	pass

if __name__=='__main__':
	
	Myapp().run()