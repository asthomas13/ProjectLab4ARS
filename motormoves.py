import RPi.GPIO as GPIO
from time import sleep
#set GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Set up the pins of the rear Motors
#For the left rear motors
ENA = 11
IN1 = 13
IN2 = 15
#For the right rear motors
ENB = 16
IN3 = 18
IN4 = 22

#Set up the pins for the front motors
#For the left front motors
ENC = 19 #On the L298N, it it s ENA
IN5 = 21 #On the L298N, it it s IN1
IN6 = 23 #On the L298N, it it s IN2
#For the right front motors
ENF = 37 #On the L298N, it it s ENB
IN7 = 29 #On the L298N, it it s IN3
IN8 = 31 #On the L298N, it it s IN4


GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

GPIO.setup(IN5, GPIO.OUT)
GPIO.setup(IN6, GPIO.OUT)
GPIO.setup(ENC, GPIO.OUT)

GPIO.setup(IN7, GPIO.OUT)
GPIO.setup(IN8, GPIO.OUT)
GPIO.setup(ENF, GPIO.OUT)

pwm1 = GPIO.PWM(ENA, 2000)

pwm1.start(75)

pwm2 = GPIO.PWM(ENB, 2000)

pwm2.start(75)

pwm3 = GPIO.PWM(ENC, 2000) #The frequency is set at 2kHz

pwm3.start(75) #Duty cycle is set at 75%

pwm4 = GPIO.PWM(ENF, 2000) #Frequency is set at 2kHz

pwm4.start(75) #Duty cycle is set at 75%

#Function to move the rover forward
def forward(distance_cm):
    distance_per_pulse_cm = 1
    pulses = int(distance_cm / distance_per_pulse_cm)
    
    #The following 4 lines lets all motors go forward
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
        
    GPIO.output(IN5, GPIO.HIGH)
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.HIGH)
    GPIO.output(IN8, GPIO.LOW)
        
    #Send pulses
    for _ in range(pulses):
        pass
    stop()
    
#Function to move the rover backward
def backward(distance_cm):
    distance_per_pulse_cm = 1
    pulses = int(distance_cm / distance_per_pulse_cm)
    
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
        
    GPIO.output(IN5, GPIO.LOW)
    GPIO.output(IN6, GPIO.HIGH)
    GPIO.output(IN7, GPIO.LOW)
    GPIO.output(IN8, GPIO.HIGH)
        
    #Send pulses
    for _ in range(pulses):
        pass
    stop()
    
def turn_left(angle):
    pass

def turn_right(angle):
    pass

def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
        
    GPIO.output(IN5, GPIO.LOW)
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.LOW)
    GPIO.output(IN8, GPIO.LOW)
    
def cleanup():
    GPIO.cleanup()

def movements(filename):
    with open(filename, 'r') as file:
        for line in file:
            command, distance = line.strip().split()
            distance = float(distance)
            if command == 'forward':
                forward(distance)
            elif command == 'backward':
                backward(distance)    
            elif command == 'left':
                turn_left(distance)    
            elif command == 'right':
                turn_right(distance)    
        
def main():
    try:
        movements('movements.txt')
        sleep(1)
        stop()
    except KeyboardInterrupt:
        cleanup()
        
if __name__ == "__main__":
    main()