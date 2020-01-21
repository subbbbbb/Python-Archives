class Player(object):
def __init__(self,x,y,col,siz,speed,controls):
self.x = x
self.y = y
self.col = col
self.siz = siz
self.speed = speed
self.controls = controls
self.swordSpeed = 0.05
self.angle = 0
self.swordLength = siz + 20
self.score = 0
def show(self):
self.xend = self.x + cos(self.angle) * self.swordLength
self.yend = self.y + sin(self.angle) * self.swordLength
strokeWeight(1)
stroke(self.col)
line(self.x,self.y,self.xend,self.yend)
noStroke()
fill(self.col)
ellipse(self.x,self.y,self.siz,self.siz)
text(self.score,self.x-3,self.y+self.siz/2+10)       
p1Controls = ['w','d','s','a','e','q']
p2Controls = ['i','l','k','j','o','u']
player1 = Player(100,100,color(255,255,0),100,1,p1Controls)
player2 = Player(300,500,color(255,0,255),100,1,p2Controls)
def setup():
size(800,800)
def draw():
background(200)
player1.show()
player2.show()
