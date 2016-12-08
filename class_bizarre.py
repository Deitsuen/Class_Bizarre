class Song(object):

    def __init__(self):
        lyrics = raw_input('>')
        self.music = lyrics
        if self.music != "":
            self.music += "\n"


        FaSol = raw_input('>')
        self.DoReMi = FaSol
        if self.DoReMi != "":
            self.DoReMi += "\n"


    def sing_me_a_song(self):
      print self.music
      print self.DoReMi

Musique = Song()
Musique.sing_me_a_song()
