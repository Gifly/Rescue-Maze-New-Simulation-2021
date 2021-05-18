from controller import Robot

robot = Robot()
class Control:
    def __init__(self):
        self.wheel_left = robot.getMotor("left wheel motor")
        self.wheel_right = robot.getMotor("right wheel motor")
        self.max_velocity = 6.28
        self.speeds = [max_velocity,max_velocity]
        self.wheel_left.setVelocity(max_velocity)
        self.wheel_right.setVelocity(max_velocity)
        
    def goForward(self):
        self.wh