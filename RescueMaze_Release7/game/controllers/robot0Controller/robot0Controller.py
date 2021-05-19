###### STILL MODIFYING ############
from controller import Robot
import time
import math
import struct

timeStep = 32 
max_velocity = 6.28
messageSent = False
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
camera.recognitionEnable(timeStep)


emitter = robot.getEmitter("emitter")

gps = robot.getGPS("gps")
gps.enable(timeStep)

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

def sendMessage():
    global messageSent
    position = gps.getValues()
    if not messageSent:
        message = struct.pack('i i i c', 0, int(position[0] * 100), int(position[2] * 100), b'H')
        emitter.send(message)
        messageSent = True


def nearObject(position):
    return math.sqrt((position[0]**2) + (position[2] ** 2)) < 0.1

def getVisibleVictims():
    objects = camera.getRecognitionObjects()

    victims = []

    for item in objects:
        if item.getColors() == [1,1,1]:
            victim_pos = item.get_position()
            victims.append(victim_pos)
    return victims

def stopAtVictim():
    victims = getVisibleVictims()

    foundVictim = False
    for victim in victims:
        if nearObject(victim):
            stop()
            sendMessage()
            foundVictim = True

    if not foundVictim:
        messageSent = False

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
    wheel_left.setPosition(leftOffset - 2.1)
    wheel_right.setPosition(rightOffset + 2.1)
    robot.step(800)

    
def turn_right():
    leftOffset = positionSensor1.getValue()
    rightOffset = positionSensor2.getValue()
    wheel_left.setPosition(leftOffset + 2.1)
    wheel_right.setPosition(rightOffset - 2.1)
    robot.step(800)
    

def move_backwards():
    leftOffset = positionSensor1.getValue()
    rightOffset = positionSensor2.getValue()
    wheel_left.setPosition(leftOffset - 5.7)
    wheel_right.setPosition(rightOffset - 5.7)
    robot.step(800)

def spin():
    leftOffset = positionSensor1.getValue()
    rightOffset = positionSensor2.getValue()
    wheel_left.setPosition(leftOffset + 4.5)
    wheel_right.setPosition(rightOffset - 4.5)
    robot.step(800)
    


while robot.step(timeStep) != -1:
    speeds = [0.5 * max_velocity, 0.5* max_velocity]
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

    colour = colour_camera.getImage()
    if colour != hole_colour or colour != swamp_colour:
        if frontSensors[0].getValue() > sensor_value and frontSensors[1].getValue() > sensor_value:
            move_forward()
        else:
            if rightSensors[0].getValue() > sensor_value:
                turn_right()
            elif leftSensors[0].getValue() > sensor_value:
                turn_left()
            else:
                move_backwards()
                turn_right()
    else:
        spin()

    #stopAtVictim()
    
    #https://github.com/gopi231091/Bug0-Algorithm-Implementation-on-E-Puck-Robot/blob/master/e-puck.c
    #https://stackoverflow.com/questions/61150174/reset-webots-position-sensor