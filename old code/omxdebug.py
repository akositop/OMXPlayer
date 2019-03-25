import kivy
import os
import subprocess
import omxplayermanipulator

from omxplayermanipulator import omxManip
from functools import partial

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

##########################################################
class ocelotRoot(BoxLayout):
	def __init__(self,**kwargs):
        	super(ocelotRoot,self).__init__(**kwargs)
        	self.player = omxManip()
        	
##########################################################
#Main 
class ocelotMain(App):
        
	def __init__(self,**kwargs):
                super(ocelotMain,self).__init__(**kwargs)
	def build(self):
		return ocelotRoot()

if __name__ == '__main__':
	ocelotMain().run()
