from time import sleep

class MotorSystems:
    def dual_motor_homming(self, master_motor, slave_motor, speed):
        master_motor.set_power(speed)
        slave_motor.follow(master_motor)
        sleep(2)
        velocity = master_motor.read_speed()
        while True:
            velocity = master_motor.read_speed()
            slave_motor.follow(master_motor)
            #self.read_encoder()
            if(abs(velocity) < 150):
                break
        
        master_motor.set_power(0)
        master_motor.zero_encoder()
        slave_motor.set_power(0)
        slave_motor.zero_encoder()

