black    = (   0,   0,   0,  255)
white    = ( 255, 255, 255,  255)
red      = ( 255,   0,   0,  255)
green    = (   0, 255,   0,  255)

def Distance (node1, node2):
	return (node1[0] - node2[0])**2 + (node1[1] - node2[1])**2

class Line:
	def __init__ (self, start_x, start_y, end_x, end_y, name, start=False):
		self.x1 = start_x
		self.x2 = end_x
		self.y1 = start_y
		self.y2 = end_y
		self.name  = name
		self.isStartPath = start
		self.enterPaths = []
		self.exitPaths = []
		self.startNode = (start_x, start_y)
		self.endNode = (end_x, end_y)
		self.magnitude = (end_x - start_x)**2 + (end_y - start_y)**2

	def __str__ (self):
		return str(self.startNode) + " " + str(self.endNode) + " " + self.name

	def Draw (self, screen):
                pygame.draw.line (screen, white, (self.x1, screen.Info().current_h - self.y1), (self.x2, screen.Info().current_h - self.y2), 3)

class Maze:
	def __init__ (self, paths, threshold):
		self.paths = paths
		self.threshold = threshold**2

	def Parse (self):
		for l in self.paths:
			for j in self.paths:
				if (j != l):
					if (Distance(l.endNode, j.startNode) < self.threshold):
						l.exitPaths.append (j)
						j.enterPaths.append (l)
						l.endNode = j.startNode
					elif (Distance (l.startNode, j.endNode) < self.threshold):
						l.enterPaths.append (l)
						j.enterPaths.append (j)
						l.startNode = j.endNode

	def Traverse (self):
		old = []
		toGo = []
		current = self.paths[0]
		while (current):
			for l in current.exitPaths:
				print current, "goes to ", l
				toGo.append (l)
			old.append (current)
			if (len (toGo) and toGo[0] not in old):
				current = toGo.pop(0)
			else:
				current = 0

	def __str__ (self):
		return str (len (self.paths)) + " paths, with a threshold of " + str (self.threshold)
