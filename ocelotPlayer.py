#imports
import os
import kivy
import subprocess

#from gpiozero import Button as gpc
from powerOption import powerOptions
from functools import partial

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.label import Label
from kivy.config import Config

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.properties import ListProperty
####################################################################
#Basic Config#

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

####################################################################
#prototypes#
class playButton(Button):
    pass
class stopButton(Button):
    pass
class pauseButton(Button):
    pass
class volumeUpButton(Button):
    pass
class volumeDownButton(Button):
    pass
class shutdownButton(Button):
    pass
class restartButton(Button):
    pass
class rootWidget(BoxLayout):
    pass
class blankWidget(BoxLayout):
    pass
class horizontalContainer(BoxLayout):
    pass
class movieSelector(FileChooserIconView):
    pass
class longspace(Label):
    pass
class blankfiller(Label):
    pass
class homeButton(Button):
    pass

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass
class MyScreenManager(ScreenManager):
    pass
####################################################################
root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    FirstScreen:
    SecondScreen:
<FirstScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'first screen!'
            font_size: 12
        BoxLayout:
            Button:
                text: ''
                size: 40, 40
                size_hint: None, None
                on_release: app.root.current = 'player'
<SecondScreen>:
    name: 'player'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'second screen!'
            font_size: 30
        BoxLayout:
            Label:
                text: ''
                size: 40, 2
            Button:
                text: ''
                font_size: 30
                background_normal: 'ComArch_Play.png'
                size: 40, 40
                size_hint: None, None
            Button:
                text: ''
                font_size: 30
                background_normal: 'ComArch_Pause.png'
                size: 40, 40
                size_hint: None, None
            Button:
                text: ''
                font_size: 30
                background_normal: 'ComArch_Stop.png'
                size: 40, 40
                size_hint: None, None
            Button:
                text: ''
                font_size: 30
                on_release: app.root.current = 'home'
                background_normal: 'ComArch_Home.png'
                size: 40, 40
                size_hint: None, None
''')
####################################################################


#main#
class ocelotPlayer(App):

    #omxplayer manipulation methods
    def omxPlay(self,instance,dummy1,dummy2,**kwargs):
        if not self.playing:
            commandString = "omxplayer " + '--win 0,60,800,420 "{0}"'.format(kwargs['filepath'])
            self.process = subprocess.Popen(commandString, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            self.playing = True    
    def omxStop(self,instance):
        if self.playing:
            self.process.stdin.write('q')
            self.playing = False
            os.system('sudo killall dbus-daemon')
            print("posys")
    def omxPause(self, instance):
        if self.playing:
            self.process.stdin.write('p')
    def omxVolumeUp(self, instance):
        if self.playing:
            self.process.stdin.write('+')
    def omxVolumeDown(self, instance):
        if self.playing:
            self.process.stdin.write('-')

     
    #init
    def __init__(self):
        self.playing = False
        super(ocelotPlayer, self).__init__()
        #pwrButton =gpc(18)
        #upButton =gpc(15)
        #downButton =gpc(14)
        #pwrButton.when_pressed = powerOptions().shutdown
        #upButton.when_pressed = self.omxVolumeUp
        #downButton.when_pressed = self.omxVolumeDown
    

    #build
    def build(self):
        #power = powerOptions()
        #filechooser = movieSelector(on_submit = partial(self.omxPlay, filepath = "/media/usb0/tester.mp4"))
        #root = rootWidget()
        #top = horizontalContainer()
        #bottom = horizontalContainer()
        #middle = blankWidget()
        #play = playButton(on_press = self.omxPause)
        #stop = stopButton(on_press = self.omxStop)
        #pause = pauseButton(on_press = self.omxPause)
        #vUp = volumeUpButton(on_press = self.omxVolumeUp)
        #vDown = volumeDownButton(on_press = self.omxVolumeDown)
        #shutdown = shutdownButton(on_press = powerOptions.shutdown)
        #restart = restartButton(on_press = powerOptions.restart)

        #top.add_widget(shutdown)
        #top.add_widget(restart)

        #middle.add_widget(filechooser)

        #bottom.add_widget(home)
        #bottom.add_widget(blankfiller())
        #bottom.add_widget(play)
        #bottom.add_widget(blankfiller())
        #bottom.add_widget(stop)
        #bottom.add_widget(blankfiller())
        #bottom.add_widget(pause)
        #bottom.add_widget(longspace())
        #bottom.add_widget(vUp)
        #bottom.add_widget(vDown)
        
        #root.add_widget(top)
        #root.add_widget(middle)
        #root.add_widget(bottom)

        return root_widget
if __name__ == '__main__':
    ocelotPlayer().run()
