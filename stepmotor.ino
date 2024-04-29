#include <Stepper.h> //Loads the stepper library

// Defines the number of steps per rotation
const int stepsPerRev = 512;

// Creates an instance of stepper class
// Pins entered in sequence IN1-IN3-IN2-IN4 for proper step sequence
Stepper myStepper = Stepper(stepsPerRev, A0, A2, A1, A3);

const int stepDelay = 10;

void clockwise(int steps) {
  myStepper.step(steps);
}

void counterclockwise(int steps) {
  myStepper.step(-steps);
}

void setup() {
    // Nothing to do (Stepper Library sets pins as outputs)
    myStepper.setSpeed(10);
}

void loop() {
  clockwise(stepsPerRev);
  delay(1000);

  counterclockwise(stepsPerRev);
  delay(1000);

  myStepper.step(0);
  delay(5000);
}
