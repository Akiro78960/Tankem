#-*- coding: utf-8 -*-
class DTOenregistrementJoueur:
    def __init__(self, time_sec, pos_x, pos_y):
        self.time_sec = time_sec
        self.pos_x = pos_x
        self.pos_y = pos_y

    def getTime(self):
        return self.time_sec

    def getX(self):
        return self.pos_x

    def getY(self):
        return self.pos_y
