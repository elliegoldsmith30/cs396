import time
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import random
import matplotlib.pylab as plt
amplitude = numpy.pi/4
frequency = 100
phaseOffset = 0
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
x = numpy.linspace(0, 2*numpy.pi, 1000)
targetAngles = numpy.pi/4*numpy.sin(x)
targetAngles = amplitude*numpy.sin(frequency*targetAngles+phaseOffset) 
# numpy.save("data/targetAngles.npy", targetAngles)
for x in range(1000):
	p.stepSimulation()
	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles[x], maxForce = 30)
	pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles[x], maxForce = 30)
	time.sleep(1/1000)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()