# ABSTRACTION, METHOD OVERLOADING, METHOD OVERRIDING, POLYMORPHISM, INHERITANCE

from abc import ABC,abstractmethod

class app(ABC):
    @abstractmethod
    def notifications(self):
        pass
    def brightness(self):
        pass
    def audio(self):
        pass
    def welcome(self):
        print("Welcome to the app")
    def close(self):
        print("app closed")

class social_media(app):
    def __init__(self,name,notif,bright_lvl,audio_lvl):
        self.name = name
        self.notif = notif
        self.bright_lvl = bright_lvl
        self.auido_lvl = audio_lvl

    def notifications(self,new_settings):
        self.notif = new_settings
    def brightness(self,new_lvl):
        self.bright_lvl = new_lvl
    def audio(self, new_lvl):
        self.auido_lvl = new_lvl
    def welcome(self):
        print(f"Welcome to {self.name}")
    def download(self,v1,v2=None):
        if(v2 == None):
            print(f"{v1} is being downloaded")
        else:
            print(f"{v1} and {v2} are being downloaded")

yt = social_media("youtube","on",50,60)
yt.welcome()
print(yt.bright_lvl)

yt.brightness(35)
print(yt.bright_lvl)

yt.download("game 1")

yt.download("game 1" , "game2")

yt.close()

