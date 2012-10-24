from direct.interval.IntervalGlobal import *

# move obj velocity using intervals
  def setupMover(self, obj):
      try:
            dt = task.time - self.prevTime
            