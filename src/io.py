# global python imports
import math, sys, random
# -----------------------------------------------------------------------------
# Panda imports
from pandac.PandaModules import * #basic Panda modules
#from direct.showbase.DirectObject import DirectObject #for event handling
from direct.actor.Actor import Actor #for animated models
from direct.interval.IntervalGlobal import * #for compound intervals
#from direct.task import Task #for update functions
# -----------------------------------------------------------------------------

class IOHandler(DirectObject):
    defaultKeys = ["arrow_up", "w", "arrow_down", "s", "arrow_left", "a", "arrow_right", "d"]
    defaultFuncs = [self.forward, self.forward, self.back, self.back, self.left, self.left, self.right, self.right]
    
    def __init__(self, game):
        self.game = game
        # disable the mouse
        base.disableMouse()
        # accept the standard directional keys
        map(self.accept, defaultKeys, defaultFuncs)
        
    # # move obj velocity using intervals
    # def setupMover(self, velocity, obj):
        # try:
            # dt = task.time - self.prevTime
            