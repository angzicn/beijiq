from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

lm = Motor(Port.A,Direction.COUNTERCLOCKWISE)
rm = Motor(Port.B)
us = UltrasonicSensor(Port.D)
claw = Motor(Port.E)
arm = Motor(Port.F)
db = DriveBase(lm,rm,62.4,16*8)
db.use_gyro(True)

arm.run_target(500,90)
claw.run_target(500,45)
db.drive(300,0)
while True:
    if us.distance() <= 120:
        break
db.stop()
arm.run_target(500,-90)
claw.run_target(500,-15)
arm.run_target(500,90)
db.turn(180)

db.drive(300,0)
while True:
    if us.distance() <= 130:
        break
db.stop()
claw.run_target(500,45)