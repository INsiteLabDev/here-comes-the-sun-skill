from mycroft import MycroftSkill, intent_file_handler
from mycroft.util import play_mp3

class HereComesTheSun(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sun.the.comes.here.intent')
    def handle_sun_the_comes_here(self, message):
        # self.speak_dialog('sun.the.comes.here')
        self.speak_dialog('this is a test')
        # self.speak_dialog("<speak><prosody rate='10%'>" + "this is a test" + "</prosody></speak>")
        #play_mp3('/home/humaira/mycroft-skill/song.mp3')


def create_skill():
    return HereComesTheSun()
    

