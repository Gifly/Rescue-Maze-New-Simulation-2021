#Axel branch XD
from controller import Robot
import time

timeStep = 32 
max_velocity = 6.28
sensor_value = 0.1
duration = 0
start_time = 0

robot = Robot()

###########################################

# Set RGB colours of the swamp and hole to avoid them
# These should be calibrated to match the environment
hole_colour = b';;@\xff'
swamp_colour = b'\x8e\xde\xf4\xff'


# Declare cameras
camera = robot.getCamera("camera_centre")
camera.enable(timeStep)
camerar = robot.getCamera("camera_right")
camerar.enable(timeStep)
cameral = robot.getCamera("camera_left")
cameral.enable(timeStep)

# Declare colour sensor underneith the robot
colour_camera = robot.getCamera("colour_sensor")
colour_camera.enable(timeStep)
########################################

wheel_left = robot.getMotor("left wheel motor")
wheel_right = robot.getMotor("right wheel motor")

leftSensors = []
rightSensors = []
frontSensors = []


frontSensors.append(robot.getDistanceSensor("ps7"))
frontSensors[0].enable(timeStep)
frontSensors.append(robot.getDistanceSensor("ps0"))
frontSensors[1].enable(timeStep)

rightSensors.append(robot.getDistanceSensor("ps2"))
rightSensors[0].enable(timeStep)
rightSensors.append(robot.getDistanceSensor("ps1"))
rightSensors[1].enable(timeStep)

leftSensors.append(robot.getDistanceSensor("ps5"))
leftSensors[0].enable(timeStep)
leftSensors.append(robot.getDistanceSensor("ps6"))
leftSensors[1].enable(timeStep)

positionSensor1 = robot.getPositionSensor('left wheel sensor')
positionSensor1.enable(timeStep)
positionSensor2 = robot.getPositionSensor('right wheel sensor')
positionSensor2.enable(timeStep)
#left wheel speed, right wheel speed
speeds = [max_velocity,max_velocity]

# wheel_left.setVelocity(max_velocity)
# wheel_right.setVelocity(max_velocity)

# wheel_left.setPosition(float("inf"))
# wheel_right.setPosition(float("inf"))

# def espera():
#     tiempo_segundos = robot.getTime()

#     while robot.getTime() < tiempo_segundos + 3:
#         print('adentro while')

#     print("fuera while")

def stop():
    #set left wheel speed
    speeds[0] = 0 * max_velocity
    #set right wheel speed
    speeds[1] = 0 * max_velocity
    wheel_left.setVelocity(speeds[0])
    wheel_right.setVelocity(speeds[1])
    wheel_left.setPosition(float('inf'))
    wheel_right.setPosition(float('inf'))
    

def move_forward():
    leftOffset = positionSensor1.getValue()
    rightOffset = positionSensor2.getValue()
    wheel_left.setPosition(leftOffset + 5.7)
    wheel_right.setPosition(rightOffset + 5.7)
    robot.step(800)
    
    

def turn_left():
    leftOffset = positionSensor1.getValue()
    rightOffset = positionSensor2.getValue()
    wheel_left.setPosition(leftOffset + 2)
    wheel_right.setPosition(rightOffset - 2)
    robot.step(800)
    

    
    
def turn_right():
    leftOffset = positionSensor1.getValue()
    rightOffset = positionSensor2.getValue()
    wheel_left.setPosition(leftOffset - 2)
    wheel_right.setPosition(rightOffset + 2)
    robot.step(800)
    

def move_backwards():
    #set left wheel speed
    speeds[0] = -0.7 * max_velocity
    #set right wheel speed
    speeds[1] = -0.9 * max_velocity
    wheel_left.setVelocity(speeds[0])
    wheel_right.setVelocity(speeds[1])
    wheel_left.setPosition(float('inf'))
    wheel_right.setPosition(float('inf'))
    


while robot.step(timeStep) != -1:
    
    #turn_left()
    move_forward()
    print(frontSensors[0].getValue(), frontSensors[1].getValue())
    break

   
    
    # colour = colour_camera.getImage()
    # if start_time + duration > robot.getTime():
    #     print("start time", start_time)
    #     print("Robot Time", robot.getTime())
    #     print("duration", duration)
    #     move_forward()
    # elif  colour == hole_colour or colour == swamp_colour:
    #     move_backwards()
    # else:
    #     turn_left()

    
            

    # for both fron sensors
    # if frontSensors[0].getValue() > sensor_value and frontSensors[1].getValue() > sensor_value:
    #     stop()
    #     move_backwards()
    #     turn_left()
    #     move backwards
    # else:
    #     move_forward()

    # colour = colour_camera.getImage()
    # if colour != hole_colour or colour != swamp_colour:
    #     if frontSensors[0].getValue() > sensor_value and frontSensors[1].getValue() > sensor_value:
    #         move_forward()
    #     else:
    #         if rightSensors[1].getValue() > sensor_value:
    #             turn_left()
    #             pass
    #         elif leftSensors[1].getValue() > sensor_value:
    #             turn_right()
    #         else:
    #             move_backwards()
    # else:
    #     move_backwards()

    
    