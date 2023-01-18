import time
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
for x in range(1000):
	p.stepSimulation()
	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	time.sleep(1/1000)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()