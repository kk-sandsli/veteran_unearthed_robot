from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop,Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
################################################################################
# Funksjoner


################################################################################
# Definisjoner
hub = PrimeHub(front_side=-Axis.Z,top_side=-Axis.Y)
farge_sensor = ColorSensor(Port.A)

left_motor  = Motor(Port.F,Direction.COUNTERCLOCKWISE)
right_motor  = Motor(Port.B)
front_motor = Motor(Port.D)
back_motor = Motor(Port.C)
drive_base  = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=112)
################################################################################

while True:
    if Button.LEFT in hub.buttons.pressed():
        drive_base.use_gyro(False)
        drive_base.straight(-10)
        drive_base.use_gyro(True)
        drive_base.settings(1000, 1000, 1100, 950)
        drive_base.curve(735,45,Stop.COAST_SMART)
        drive_base.turn(-90,Stop.COAST_SMART)
        wait(1000)
        drive_base.settings(200, 1000, 1100, 950)
        drive_base.straight(250,Stop.COAST_SMART)
        drive_base.settings(1000, 1000, 1100, 950)
        drive_base.straight(-100,Stop.COAST_SMART) #####W
        drive_base.turn(-45,Stop.COAST_SMART)
        drive_base.straight(-350,Stop.COAST_SMART)
        drive_base.turn(45,Stop.COAST_SMART)
        drive_base.curve(350,-35,Stop.COAST_SMART)
        drive_base.straight(-10, Stop.COAST_SMART)
        drive_base.turn(-30,Stop.COAST_SMART)
        #drive_base.straight(-200, Stop.COAST_SMART)
        
# update
# update 2
