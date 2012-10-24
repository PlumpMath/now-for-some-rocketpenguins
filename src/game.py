# global python imports
import math, sys, random
# -----------------------------------------------------------------------------
# Panda imports
import direct.directbase.DirectStart #starts panda
from pandac.PandaModules import * #basic Panda modules
from direct.showbase.DirectObject import DirectObject #for event handling
from direct.actor.Actor import Actor #for animated models
from direct.interval.IntervalGlobal import * #for compound intervals
from direct.task import Task #for update functions
# -----------------------------------------------------------------------------
# local imports
from world import World
from io import IOHandler

# singleton class game
# handle tasks, coordinate world with models, lights and io actions
class Game(object):
    def __init__(self):
        self.world = World(self)
        self.iohandler = IOHandler(self)