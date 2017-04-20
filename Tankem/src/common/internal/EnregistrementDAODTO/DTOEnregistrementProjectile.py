# -*- coding: utf-8 -*-
class DTOenregistrementProjectile:
    def __init__(self, time_sec, pos_x, pos_y, pos_z, en_mouvement):
        self.time_sec = time_sec
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.en_mouvement = en_mouvement

    def getTime(self):
        return self.time_sec

    def getX(self):
        return self.pos_x

    def getY(self):
        return self.pos_y

    def getZ(self):
        return self.pos_z

    def getEnMouvement(self):
        return self.en_mouvement

