from controller import Robot
#Omarbranch
timeStep = 32 
max_velocity = 6.28

robot = Robot()

wheel_left = robot.getMotor("left wheel motor")
wheel_right = robot.getMotor("right wheel motor")

lefSensors = []
rightSensors = []
frontSensors = []


frontSensors.append(robot.getDistanceSensor("ps7"))
frontSensors[0].enable(timeStep)
frontSensors.append(robot.getDistanceSensor("ps0"))
frontSensors[1].enable(timeStep)

rightSensors.append(robot.getDistanceSensor("ps1"))
rightSensors[0].enable(timeStep)
rightSensors.append(robot.getDistanceSensor("ps2"))
rightSensors[1].enable(timeStep)

lefSensors.append(robot.getDistanceSensor("ps5"))
lefSensors[0].enable(timeStep)
lefSensors.append(robot.getDistanceSensor("ps6"))
lefSensors[1].enable(timeStep)

#left wheel speed, right wheel speed
speeds = [max_velocity,max_velocity]

wheel_left.setVelocity(max_velocity)
wheel_right.setVelocity(max_velocity)

wheel_left.setPosition(float("inf"))
wheel_right.setPosition(float("inf"))

while robot.step(timeStep) != -1:
    speeds[0] = max_velocity
    speeds[1] = max_velocity
    
    for i in range(2):
        #for sensors on the left
        if lefSensors[i].getValue() > 80:
            #turn right
            pass
        elif rightSensors[i].getValue() > 80:
            #turn left
            pass

    #for both fron sensors
    if frontSensors[0].getValue() > 80 and frontSensors[1].getValue() > 80:
        spin()
        #move backwards
        pass

    wheel_left.setVelocity(speeds[0])
    wheel_right.setVelocity(speeds[1])