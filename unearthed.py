from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop,Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
################################################################################
# Funksjoner
# ------------------------------------------------------------------------------
def AU():
    for i in range(3):
        drive_base.drive(300, 0)
        wait(250)
        drive_base.stop()
        hub.imu.reset_heading(0)
#        wait(500)
        back_motor.run(1000)
        wait(400)
        back_motor.stop()
        wait(1000)
        back_motor.run(-500)
        wait(430)
        back_motor.stop()
        wait(1000)

def EWIK():
    drive_base.use_gyro(False)
    drive_base.drive(300, 0)
    wait(250)
    drive_base.stop()
    drive_base.use_gyro(True)
    hub.imu.reset_heading(0)
    drive_base.settings(1500, 1500, 850, 850)
    drive_base.curve(-140, 90, Stop.COAST_SMART)
    drive_base.straight(-460, Stop.COAST_SMART)
    drive_base.turn(84, Stop.COAST_SMART)
    drive_base.straight(-100, Stop.COAST_SMART)
    wait(500)
    drive_base.straight(100, Stop.COAST_SMART)
    drive_base.turn(90, Stop.COAST_SMART)
    drive_base.straight(140, Stop.COAST_SMART)
    drive_base.turn(-80, Stop.COAST_SMART)
    drive_base.settings(600, 600, 850, 850)
    drive_base.straight(60)
    drive_base.use_gyro(False)
    drive_base.turn(-35)
    wait(500)
    drive_base.use_gyro(True)
    front_motor.run(-1200)
    wait(1000)
    front_motor.stop()
    drive_base.settings(1500, 1500, 1500, 1500)
    drive_base.curve(-100, -110)
    drive_base.straight(-700)

def none2():
    drive_base.use_gyro(False)
    drive_base.drive(300, 0)
    wait(250)
    drive_base.stop()
    drive_base.use_gyro(True)
    hub.imu.reset_heading(0)
    drive_base.settings(1500, 1500, 1500, 1500)
    drive_base.straight(-660, Stop.COAST_SMART)
    drive_base.turn(45, Stop.COAST_SMART)
    drive_base.straight(-40, Stop.COAST_SMART)
    drive_base.settings(1500, 1500, 500, 500)
    drive_base.turn(-50, Stop.COAST_SMART)
    wait(300)
    drive_base.turn(90, Stop.COAST_SMART)
    drive_base.straight(60, Stop.COAST_SMART)
    drive_base.turn(-90)
    drive_base.straight(-30)
    drive_base.turn(-45)
    drive_base.straight(30)
    drive_base.turn()

def ogaboga():
    back_motor.run_time(-500, 500)
    back_motor.run_angle(500, 15)
    drive_base.use_gyro(False)
    drive_base.drive(-300, 0)
    wait(250)
    drive_base.stop()
    drive_base.use_gyro(True)
    wait(100)
    hub.imu.reset_heading(0)
    drive_base.settings(1500, 1500, 1500, 1500)
    drive_base.straight(550, Stop.COAST_SMART)
    drive_base.turn(-50, Stop.COAST_SMART)
    drive_base.straight(520, Stop.COAST_SMART)
    wait(300)
#    drive_base.turn(10, Stop.COAST_SMART)
    drive_base.straight(-60, Stop.COAST_SMART)
#    drive_base.turn(-36, Stop.COAST_SMART)
#    drive_base.straight(180, Stop.COAST_SMART)
#    drive_base.turn(38, Stop.COAST_SMART)
#    back_motor.run_angle(500, 93)
#    drive_base.straight(-100, Stop.COAST_SMART)
#    wait(300)
#    drive_base.straight(170, Stop.COAST_SMART)
#    drive_base.turn(160, Stop.COAST_SMART)
    drive_base.turn(-41, Stop.COAST_SMART)
    drive_base.straight(190, Stop.COAST_SMART)
    drive_base.turn(45, Stop.COAST_SMART)
    back_motor.run_angle(500, 81)
    wait(300)
    drive_base.settings(1000, 500, 500, 500)
    drive_base.straight(-220, Stop.COAST_SMART)
    wait(400)
    drive_base.straight(130, Stop.COAST_SMART)
    drive_base.settings(1000,1000,1000,1000)
    back_motor.run_angle(500, -80)
    drive_base.turn(-225, Stop.COAST_SMART)
    drive_base.straight(-230, Stop.COAST_SMART)
#    drive_base.turn(-45, Stop.COAST_SMART)
#    drive_base.straight(-30, Stop.COAST_SMART)
    back_motor.run_angle(500, 80)
    drive_base.straight(-100)
#    drive_base.turn(45, Stop.COAST_SMART)
    back_motor.run_angle(60, -70)

def ost():
    drive_base.use_gyro(False)
    drive_base.drive(-300, 0)
    wait(250)
    drive_base.stop()
    drive_base.use_gyro(True)
    wait(100)
    hub.imu.reset_heading(0)
    drive_base.settings(1000,1000,1000,1000)
    drive_base.curve(760, -30)
    drive_base.turn(-45, Stop.COAST_SMART)
    drive_base.turn(90, Stop.COAST_SMART)
    drive_base.curve(917, 20, Stop.COAST_SMART)
    drive_base.turn(-41, Stop.COAST_SMART)
    drive_base.straight(70, Stop.COAST_SMART)
    drive_base.turn(-30, Stop.COAST_SMART)
    wait(700)
    drive_base.straight(30, Stop.COAST_SMART)
    wait(400)
    drive_base.straight(-67, Stop.COAST_SMART)
    drive_base.turn(-60, Stop.COAST_SMART)
    drive_base.straight(-170, Stop.COAST_SMART)
    drive_base.curve(-200, -90, Stop.COAST_SMART)
    drive_base.straight(180, Stop.COAST_SMART)
    drive_base.turn(-21, Stop.COAST_SMART)
    drive_base.straight(120, Stop.COAST_SMART)
    drive_base.turn(45, Stop.COAST_SMART)
    drive_base.turn(-25, Stop.COAST_SMART)
    drive_base.curve(-500, 20)
    drive_base.turn(20, Stop.COAST_SMART)





#    drive_base.straight(-110, Stop.COAST_SMART)
#    back_motor.run_angle(35, -90)
#    back_motor.run(-70)
#    wait(3000)
#    back_motor.stop()








#    drive_base.straight(-30)
#    drive_base.turn(-90)
#    drive_base.straight(100)
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
hub.speaker.volume(1000)
for i in range(3):
    hub.speaker.beep(500, 100)
    wait(100)
#hub.speaker.play_notes(["C4/4", "C4/4", "G4/4", "G4/4", "A4/4", "A4/4", "G4/2", "F4/4", "F4/4", "E4/4", "E4/4", "D4/4", "D4/4", "C4/2", "G4/4","G4/4", "F4/4", "F4/4", "E4/4", "E4/4", "D4/2", "G4/4","G4/4", "F4/4", "F4/4", "E4/4", "E4/4", "D4/2", "C4/4", "C4/4", "G4/4", "G4/4", "A4/4", "A4/4", "G4/2", "F4/4", "F4/4", "E4/4", "E4/4",  "D4/4", "D4/4", "C4/1" ])
while True:
    if Button.RIGHT in hub.buttons.pressed():
        if farge_sensor.color() == Color.NONE:
            ogaboga()
