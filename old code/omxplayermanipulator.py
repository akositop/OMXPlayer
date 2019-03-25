import os
import subprocess

class omxManip():

    def __init__(self):
        self.playing = False
        self.paused = False

    def omxPlay(self, filepath, subtitlepath):
        if not self.playing:
            if subtitlepath != " ":
                commandString = "omxplayer " + "--win 0,40,800,420 --subtitle "+ subtitlepath+ " " + filepath
            else:    
                commandString = "omxplayer " + "--win 0,40,800,420 " + filepath
            self.process = subprocess.Popen(commandString, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            self.playing = True
        
    def omxStop(self, instance):
        if self.playing:
            self.process.stdin.write('q')
            self.playing = False
            os.system('sudo killall dbus-daemon')
            print("posys")
    def omxPause(self, instance):
        if self.playing and not self.paused:
            self.process.sdtin.write('p')
            self.pause = True
        else:
            self.process.stdin.write('p')
            self.pause = False
            
    def omxChangeVideoSize(height, width, curPos):
        pass
    def omxSubtitle():
        pass
    def omxVolumeUp():
        pass
    def omxVolumeDown():
        pass
    def omxNext():
        pass
    def omxPrev():
        pass
