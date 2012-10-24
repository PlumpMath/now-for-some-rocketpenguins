# global python imports
import math, sys, random
# -----------------------------------------------------------------------------
# Panda imports
from pandac.PandaModules import * #basic Panda modules
from direct.showbase.DirectObject import DirectObject #for event handling
from direct.actor.Actor import Actor #for animated models
from direct.interval.IntervalGlobal import * #for compound intervals
from direct.task import Task #for update functions
# -----------------------------------------------------------------------------

class World(object):
    def __init__(self):
        self.iohandler = io.IOHandler()
        self.setupModels()
        self.setupLights()
        self.setupCollisions()