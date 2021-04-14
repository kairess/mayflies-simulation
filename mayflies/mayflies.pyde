w, h = 1920, 1080
n_flies = 1024
mx, my = w // 2, h // 2
moving = False
time_moved = millis()

class Fly:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random(-1, 1)
        self.dy = random(-1, 1)
        
    def step(self):
        self.dx += random(-1, 1)
        self.dy += random(-1, 1)
    
        self.dx = min(self.dx, 1)
        self.dx = max(self.dx, -1)
        self.dy = min(self.dy, 1)
        self.dy = max(self.dy, -1)

        self.x += self.dx
        self.y += self.dy
        
        if moving:
            self.x = self.x + (mx - self.x) / 20 + self.dx
            self.y = self.y + (my - self.y) / 20 + self.dy


flies = []

for i in range(n_flies):
    flies.append(Fly(random(mx - 100, mx + 100), random(my - 100, my + 100)))


def setup():
    size(w, h)
    noStroke()


def mouseMoved():
    global mx, my, moving, time_moved

    mx = mouseX
    my = mouseY

    moving = True
    time_moved = millis()


def draw():
    global moving, time_moved
    
    background(0, 0, 0)
    
    for fly in flies:
        fly.step()
        
        fill(255, 255, 255)
        
        if fly.dx > fly.dy:
            rect(fly.x, fly.y, 3, 2)
        else:
            rect(fly.x, fly.y, 2, 3)
    
    if millis() - time_moved > 1000:
        moving = False
