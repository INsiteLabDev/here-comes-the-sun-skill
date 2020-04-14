from mycroft import MycroftSkill, intent_file_handler
from mycroft.util import play_mp3

class HereComesTheSun(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sun.the.comes.here.intent')
    def handle_sun_the_comes_here(self, message):
        # self.speak_dialog('sun.the.comes.here')
        # self.speak_dialog('this is a test')
        self.speak_dialog("<speak><prosody rate='x-slow'>" + "this is a test" + "</prosody></speak>")
        #play_mp3('/home/humaira/mycroft-skill/song.mp3')

        #self.speak("<speak>Prosody can be used to change the way words sound. The following words are <prosody volume='x-loud'> quite a bit louder than the rest of this passage. </prosody> Each morning when I wake up, <prosody rate='x-slow'>I speak quite slowly and deliberately until I have my coffee.</prosody> I can also change the pitch of my voice using prosody. Do you like <prosody pitch='+5%'> speech with a pitch that is higher, </prosody> or <prosody pitch='-10%'> is a lower pitch preferable?</prosody></speak>")



def create_skill():
    return HereComesTheSun()
    

