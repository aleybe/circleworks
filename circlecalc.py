import math

class circleObjects:

    #circle formula
    #(x-h)**2 + (y-k)**2 = r**2
    
    def __init__(self, ixloc, iyloc, irad):
        self.x_location = ixloc
        self.y_location = iyloc
        self.radius = irad

    def AnglePoints(self, angle):
        # Parametric points on a cricle 
        # x = cx + r * cos(a)
        # y = cy + r * sin(a)
        
        #Create array for the entries at where the points will be given.
        self.pointsOnCircle = []

        #First calculate how many times the angle goes into 360degrees (full circle)
        angleIntervals = 360 / angle

        for interval in range(0, int(angleIntervals)):
            #get x value
            x = self.x_location + (self.radius * math.cos(math.radians(interval*angle)))
            y = self.y_location + (self.radius * math.sin(math.radians(interval*angle)))

            #create a point
            currentPoint = (x, y)
            self.pointsOnCircle.append(currentPoint)

        return(self.pointsOnCircle)


        



