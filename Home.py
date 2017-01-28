from kivy.config import Config 
Config.set('graphics', 'width', '900')		#changes the size of the windows as per ur convinient(only once!)!
Config.set('graphics', 'height', '507')
import MySQLdb
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.switch import Switch
import time
from kivy.uix.image import Image
import thread
from subprocess import *        #everytime u needa import all these things always.

class MainScreen(FloatLayout): 				#imports the gridlayout for the beauty!
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.strt = 0
		self.db = myDB()
		self.cols = 2
		self.wimg = Image(source='assets/home.jpg', allow_stretch = True)
		self.add_widget(self.wimg)

		self.lbl1 = Label(text = "[size=20][color=1ff5f1]Welcome Tushar[/color][/size]", markup = True, size_hint=(.6, .6), pos_hint={'x':.2, 'y':.6})
		self.add_widget(self.lbl1)

		self.lbl2 = Label(text = "[color=1ff5f1]Select The action that you would like to perform[/color]", markup = True, size_hint=(.6, .6), pos_hint={'x':.2, 'y':.49})
		self.add_widget(self.lbl2)

		self.spinner = Spinner(
		text='Add Account',
		# available values
		values=('Add an entry of password', 'get details'),
		size_hint= (None, None),
		size=(300, 50),
		pos_hint={'center_x': .5, 'center_y': .5})
		self.add_widget(self.spinner)
		
		self.btn1 = MyButton(text = "Go for it!", size_hint=(.2, .1), pos_hint={'x':.15, 'y':0})
		self.btn1.bind(pressed=self.performit)
		self.add_widget(self.btn1)
		
		self.btn2 = MyButton(text = "Exit", size_hint=(.2, .1), pos_hint={'x':.6, 'y':0})
		self.btn2.bind(pressed=self.performexit)
		self.add_widget(self.btn2)
	def addAcc(self, instance, pos): #inserts the details of an account

		tm = time.ctime()
		sql = "INSERT INTO mainTable (accName, accuName, accPass, accDate) VALUES ('" + self.p1.text + "', '" + self.p2.text + "', '" + self.p3.text + "', '" + tm + "')"
		try:
			self.db.ExecuteNonQuery(sql)
			self.p1.text = "Data successfully added! ;-)"
			self.p2.text = ""
			self.p3.text = ""
		except Exception, e:
			print e
	def revert(self, instance, pos):
		thread.start_new_thread(self.navigate, ("th1", "2")) #If login is successful, then go to the next window. And hence create new Thread.
		exit()
	def navigate(thrd, va, vv):	#A thread method
		call(["python", "Home.py"])	#Invoking a terminal command to start execution of the Home.py code.!

	def performexit(self, instance, pos):
		self.db.con.close()
		exit()
	def performit(self, instance, pos):	#If the requirement is selected and we are ready to go.
		work = self.spinner.text
		self.remove_widget(self.spinner)
		self.remove_widget(self.btn1)
		self.btn4 = MyButton(text = "Back", size_hint=(.2, .1), pos_hint={'x':.375, 'y':0})
		self.btn4.bind(pressed=self.revert)
		self.add_widget(self.btn4)
		self.wimg.source = "assets/home.jpg"

		if(cmp(work, "Add an entry of password") == 0):
			self.btn3 = MyButton(text = "Add an account!", size_hint=(.2, .1), pos_hint={'x':.15, 'y':0})
			self.btn3.bind(pressed=self.addAcc)
			self.add_widget(self.btn3)
	
			self.lbl3 = Label(text = "[color=1ff5f1]Account Name[/color]", markup = True, size_hint=(.6, .6), pos_hint={'x':.2, 'y':.4})
			self.add_widget(self.lbl3)

			self.p1 = TextInput(multiline = False, size_hint=(.5, .08), pos_hint={'x':.25, 'y':.6})
			self.add_widget(self.p1)
			self.lbl2.text = "Adding An Account! ;-)"

			self.lbl3 = Label(text = "[color=1ff5f1]User Name[/color]", markup = True, size_hint=(.6, .6), pos_hint={'x':.2, 'y':.26})
			self.add_widget(self.lbl3)

			self.p2 = TextInput(multiline = False, size_hint=(.5, .08), pos_hint={'x':.25, 'y':.46})
			self.add_widget(self.p2)
			self.lbl2.text = "Adding An Account! ;-)"
		
			self.lbl3 = Label(text = "[color=1ff5f1]Password[/color]", markup = True, size_hint=(.6, .6), pos_hint={'x':.2, 'y':.14})
			self.add_widget(self.lbl3)

			self.p3 = TextInput(multiline = False, size_hint=(.5, .08), pos_hint={'x':.25, 'y':.34})
			self.add_widget(self.p3)
			self.lbl2.text = "Adding An Account! ;-)"
		else:
			self.tmp = 1
			self.lbl2.text = "Welcome to the see the password!!"
			self.btn3 = MyButton(text = "See the password.!", size_hint=(.2, .1), pos_hint={'x':.15, 'y':0})
			self.btn3.bind(pressed=self.getInfo)
			self.add_widget(self.btn3)
			hi = ()
			sql = "SELECT * from mainTable"
			try:
				data = self.db.ExecuteScalar(sql)
				for row in data:
					hi = hi + (row[1], '')
			except Exception, e:
				print e
			self.sub = Spinner(
			text='Select Account',
			# available values
			values=hi,
			size_hint= (None, None),
			size=(300, 50),
			pos_hint={'center_x': .5, 'center_y': .6})
			self.add_widget(self.sub)

	def getInfo(self, instance, pos):
		self.tpk = self.sub.text
		self.remove_widget(self.sub)
		hi = ()
		sql = "SELECT * FROM mainTable where accName = '" + self.tpk + "'"
		try:
			self.data = self.db.ExecuteScalar(sql)
			for self.row in self.data:
					hi = hi + (self.row[3], '')
		except Exception, e:
			print e
		aName    = self.row[1]
		aUserNm	 = self.row[2]
	 	aUserPas = self.row[3]
		aAddDate = self.row[4]
		
		self.remove_widget(self.sub)
		self.remove_widget(self.btn3)
		self.lbl11 = Label(text = "[i][size=18][color=f4a460]Account Name :- " + aName + ".[/color][/size][/i]", markup = True, size_hint=(.8, .8), pos_hint={'x':-.2, 'y':.1})
		self.lbl12 = Label(text = "[i][size=18][color=ffffff]User Name :-   " + aUserNm + ".[/color][/size][/i]", markup = True, size_hint=(.8, .8), pos_hint={'x':-.2, 'y':-.23})
		self.lbl13 = Label(text = "[i][size=18][color=ffffff]Password :- " + aUserPas + ".[/color][/size][/i]", markup = True, size_hint=(.8, .8), pos_hint={'x':-.2, 'y':-.27})
		self.lbl14 = Label(text = "[i][size=18][color=ffffff]Date :- \"" + aAddDate + "\" .[/color][/size][/i]", markup = True, size_hint=(.8, .8), pos_hint={'x':.3, 'y':-.27})
		self.add_widget(self.lbl11)
		self.add_widget(self.lbl12)
		self.add_widget(self.lbl13)
		self.add_widget(self.lbl14)
			
class MyButton(Button):			#Custom made Button. Always Consider keeping this same.
	pressed = ListProperty([0, 0])
	def on_touch_down(self, touch):
		if self.collide_point( *touch.pos):
			self.pressed = touch.pos
			return False
class myDB:
	def __init__(self):
		self.con = MySQLdb.connect("localhost", "roxyUser", "qwerty", "passTable")
		self.cmd = self.con.cursor()
	def ExecuteNonQuery(self, query):
		try:
			self.cmd.execute(query)
			self.con.commit()
		except Exception, e:
			print e
			self.con.rollback()
	def ExecuteScalar(self, query):
		try:
			self.cmd.execute(query)
		except:
			self.con.rollback
			return -1
		data = self.cmd.fetchall()
		return data

class MyApp(App):				#Starts the Application.
	def build(self):
		return MainScreen()	#Starts the execution of the LoginScreen() class
if __name__ == '__main__': #If Main.
	MyApp().run()