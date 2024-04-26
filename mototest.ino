
const int ENA = 6; // PWM pin for motor driver A
const int IN1 = 7; // Motor A input 1
const int IN2 = 5; // Motor A input 2

const int ENB = 3; // PWM pin for motor driver B
const int IN3 = 4; // Motor B input 1
const int IN4 = 2; // Motor B input 2


const int ENC = 11;  // PWM pin for second motor driver A
const int IN5 = 12; // Second motor A input 1
const int IN6 = 13; // Second motor A input 2

const int END = 9;  // PWM pin for second motor driver B
const int IN7 = 10; // Second motor B input 1
const int IN8 = 8; // Second motor B input 2

void setup() {
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  
  pinMode(ENC, OUTPUT);
  pinMode(IN5, OUTPUT);
  pinMode(IN6, OUTPUT);
  
  pinMode(END, OUTPUT);
  pinMode(IN7, OUTPUT);
  pinMode(IN8, OUTPUT);

  // Initialize PWM frequency
  // PWM frequency = 976.5625 Hz (default for Arduino UNO)
  // No need to set PWM frequency explicitly for Arduino UNO

  // Start PWM with duty cycle of 75%
  analogWrite(ENA, 191); // Duty cycle: 75%
  analogWrite(ENB, 191); // Duty cycle: 75%
  analogWrite(ENC, 191); // Duty cycle: 75%
  analogWrite(END, 191); // Duty cycle: 75%
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readString();
    Serial.println("Received message: " + message);
    if (message == "Forward") {
      Serial.println("Moving Forward");
      moveForward();
    }
    else if (message == "Backwards")
    {
      moveBackward();
    }
    else if (message == "right"){
      turnRight();
    }
    else if (message == "Left"){
      turnLeft();
    }
    else if (message == "Stop"){
      stopMotors();
    }
  }
}

void moveForward() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  
  digitalWrite(IN5, LOW);
  digitalWrite(IN6, HIGH);
  digitalWrite(IN7, HIGH);
  digitalWrite(IN8, LOW);
}

void moveBackward() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  
  digitalWrite(IN5, HIGH);
  digitalWrite(IN6, LOW);
  digitalWrite(IN7, LOW);
  digitalWrite(IN8, HIGH);
}

void turnLeft() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  
  digitalWrite(IN5, LOW);
  digitalWrite(IN6, HIGH);
  digitalWrite(IN7, LOW);
  digitalWrite(IN8, HIGH);
}

void turnRight() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  digitalWrite(IN5, HIGH);
  digitalWrite(IN6, LOW);
  digitalWrite(IN7, HIGH);
  digitalWrite(IN8, LOW);
}

void stopMotors() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  digitalWrite(IN5, LOW);
  digitalWrite(IN6, LOW);
  digitalWrite(IN7, LOW);
  digitalWrite(IN8, LOW);
}
