from kivy.config import Config 
Config.set('graphics', 'width', '400')		#changes the size of the windows as per ur convinient(only once!)!
Config.set('graphics', 'height', '150')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ListProperty
import thread
from subprocess import *        #everytime u needa import all these things always.

class LoginScreen(GridLayout): 				#imports the gridlayout for the beauty!
	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 2
		self.lbl1 = Label(text = "User Name")
		self.add_widget(self.lbl1) #dynamically created and adds the widget instantly
		self.username = TextInput(multiline=False) #this and the next line creates and adds the widget
		self.add_widget(self.username)
		self.lbl2 = Label(text = "Password")
		self.add_widget(self.lbl2)
		self.password = TextInput(password=True, multiline = False)
		self.add_widget(self.password)

		#the following two are the custom buttons of the class MyButton(Button) i.e. MyButton inherits Button.
		#and the bind method is useful for the event registration
		self.butn = MyButton(text = "Login")
		self.butn.bind(pressed=self.loginme)
		self.add_widget(self.butn)
		

		self.extbtn = MyButton(text = "Exit")
		self.extbtn.bind(pressed=self.btn_pressed)
		self.add_widget(self.extbtn)
	

	def btn_pressed(self, instance, pos):	#If Exit button is pressed
		exit()

	def loginme(self, instance, pos):		#If login button is pressed
		uname = self.username.text
		upass = self.password.text

		if(cmp(uname, "Tushar") == 0):
			if(cmp(upass, "#PQCD$S") == 0):
				try:
					thread.start_new_thread(self.navigate, ("th1", "2")) #If login is successful, then go to the next window. And hence create new Thread.
				except Exception, e:
					print e
				exit()									#closing the current windows just like Form.hide()! ;-)
			else:
				self.password.text = "Wrong Password"
		else:
			self.username.text = "Wrong username"
	def navigate(thrd, va, vv):	#A thread method
		call(["python", "Home.py"])	#Invoking a terminal command to start execution of the Home.py code.!

class MyButton(Button):			#Custom made Button. Always Consider keeping this same.
	pressed = ListProperty([0, 0])
	def on_touch_down(self, touch):
		if self.collide_point( *touch.pos):
			self.pressed = touch.pos
			return True

class MyApp(App):				#Starts the Application.
	def build(self):
		return LoginScreen()	#Starts the execution of the LoginScreen() class
if __name__ == '__main__': #If Main.
	MyApp().run()