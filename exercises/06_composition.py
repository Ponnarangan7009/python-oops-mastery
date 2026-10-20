"""Exercise: write a complete composition example.

A MusicPlayer has a Speaker. The player stores the speaker object and asks
it to play a sound. Complete all TODOs, then use the caller.
"""


class Speaker:
    def play_sound(self):
        # TODO: print "Speaker is playing sound."
        pass


class MusicPlayer:
    def __init__(self, speaker):
        # TODO: store the Speaker object on this MusicPlayer
        pass

    def play_music(self):
        # TODO: ask the stored speaker to play sound
        # Then print "Music is playing."
        pass


speaker = Speaker()
music_player = MusicPlayer(speaker)
music_player.play_music()
