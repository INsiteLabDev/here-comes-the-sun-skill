from mycroft import MycroftSkill, intent_file_handler


class HereComesTheSun(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sun.the.comes.here.intent')
    def handle_sun_the_comes_here(self, message):
        self.speak_dialog('sun.the.comes.here')


def create_skill():
    return HereComesTheSun()

