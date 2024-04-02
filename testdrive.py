#Upload the library files
import RPi.GPIO as GPIO
from time import sleep

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

pwm3 = GPIO.PWM(ENC, 2000)

pwm3.start(75)

pwm4 = GPIO.PWM(ENF, 2000)

pwm4.start(75)

try:
    while True:
        #The following 4 lines lets rear motors go forward
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        
        GPIO.output(IN5, GPIO.HIGH)
        GPIO.output(IN6, GPIO.LOW)
        GPIO.output(IN7, GPIO.HIGH)
        GPIO.output(IN8, GPIO.LOW)
        
        sleep(3)
        #The following 4 lines let the rear motors go backwards
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        
        GPIO.output(IN5, GPIO.LOW)
        GPIO.output(IN6, GPIO.HIGH)
        GPIO.output(IN7, GPIO.LOW)
        GPIO.output(IN8, GPIO.HIGH)
        
        sleep(3)
        #The following 4 lines lets the left rear go forward, while the right rear goes backward (turns rover right)
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        
        GPIO.output(IN5, GPIO.HIGH)
        GPIO.output(IN6, GPIO.LOW)
        GPIO.output(IN7, GPIO.LOW)
        GPIO.output(IN8, GPIO.HIGH)
        sleep(3)
        #The following 4 lines lets the left rear go backward, while the right rear goes forward (turns rover left)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        
        GPIO.output(IN5, GPIO.LOW)
        GPIO.output(IN6, GPIO.HIGH)
        GPIO.output(IN7, GPIO.HIGH)
        GPIO.output(IN8, GPIO.LOW)
        sleep(3)
        
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        
        GPIO.output(IN5, GPIO.LOW)
        GPIO.output(IN6, GPIO.LOW)
        GPIO.output(IN7, GPIO.LOW)
        GPIO.output(IN8, GPIO.LOW)
        sleep(3)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Clean Up")
