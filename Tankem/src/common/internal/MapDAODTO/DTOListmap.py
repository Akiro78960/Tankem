# -*- coding: utf-8 -*-
class DTOlistmap:

    # Constructor
    def __init__(self):
        self.array_maps = []

    # Getters
    def appendList(self, DTOmap):
        self.array_maps[DTOmap.getID()] = DTOmap

    def getMap(self, id_niveau):
        return self.array_maps[id_niveau]
