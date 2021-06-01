def setup():
    # 1. Use the size function to set the size of your sketch
    size(800, 600)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    # global bg, frog
    global bg
    global frog
    global frog_x
    global frog_y
    frog_x = 500
    frog_y = 450
    global car
    global car2
    global car3
    global car4
    global car5
    car = Car(0, 450, 50, 4)
    car2 = Car(250, 350, 50, -6)
    car3 = Car(300, 250, 50, 8)
    car4 = Car(50, 150, 50, -5)
    car5 = Car(150, 50, 50, 7)
    # bg = loadImage("froggerBackground.png")
    bg = loadImage("froggerBackground.png")
    frog = loadImage("frog.png")
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    bg.resize(800, 600)
    frog.resize(25, 25)
    
def draw():
    global frog_x
    global frog_y
    # 4. Use the background function to draw the background
    background(bg)
    # 5. Use the image function to draw the frog.
    image(frog, frog_x, frog_y)
    # Run the program and check the background and frog are displayed.
    
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    # global frog_x, frog_y
    
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    car.update()
    car.draw()
    car2.update()
    car2.draw()
    car3.update()
    car3.draw()
    car4.update()
    car4.draw()
    car5.update()
    car5.draw()
    
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
    if(car.intersects(frog)):
        frog_x = 300
        frog_y = 550
    if(car2.intersects(frog)):
        frog_x = 300
        frog_y = 550
    if(car3.intersects(frog)):
        frog_x = 300
        frog_y = 550
    if(car4.intersects(frog)):
        frog_x = 300
        frog_y = 550
    if(car5.intersects(frog)):
        frog_x = 300
        frog_y = 550
    
    # 9. Create more car objects of different lengths, speed, and size
    if(keyPressed):
        if(keyCode == LEFT):
            frog_x = frog_x - 2
        elif(keyCode == RIGHT):
            frog_x = frog_x + 2
        elif(keyCode == UP):
            frog_y = frog_y - 2
        elif(keyCode == DOWN):
            frog_y = frog_y + 2

    if(frog_y < 0):
        exit()

class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
            
    def intersects(self, frog):
      
        if ((frog_x > self.x) and (frog_x < (self.x + self.length)) and (frog_y > self.y - 10) and frog_y < self.y + 25):
            return True
        else:
            return False
