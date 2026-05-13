// L298N Motor Driver Pins
const int enA = 10; // PWM Pin
const int in1 = 9;
const int in2 = 8;
const int enB = 5;  // PWM Pin
const int in3 = 7;
const int in4 = 6;

void setup() {
  Serial.begin(9600);
  pinMode(enA, OUTPUT); pinMode(in1, OUTPUT); pinMode(in2, OUTPUT);
  pinMode(enB, OUTPUT); pinMode(in3, OUTPUT); pinMode(in4, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char direction = Serial.read();      // Read 'L', 'R', 'F', or 'T'
    int speed = Serial.parseInt();       // Read the PWM value (e.g., 160)

    switch (direction) {
      case 'F': moveForward(speed); break;
      case 'L': turnLeft(speed);    break;
      case 'R': turnRight(speed);   break;
      case 'T': rotateSearch(speed); break;
      default:  stopCar();          break;
    }
  }
}

void moveForward(int s) {
  analogWrite(enA, s); analogWrite(enB, s);
  digitalWrite(in1, HIGH); digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH); digitalWrite(in4, LOW);
}

void turnLeft(int s) {
  analogWrite(enA, s); analogWrite(enB, s);
  digitalWrite(in1, LOW);  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH); digitalWrite(in4, LOW);
}

void turnRight(int s) {
  analogWrite(enA, s); analogWrite(enB, s);
  digitalWrite(in1, HIGH); digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);  digitalWrite(in4, HIGH);
}

void rotateSearch(int s) {
  turnRight(s); // Clockwise rotation
}

void stopCar() {
  digitalWrite(in1, LOW); digitalWrite(in2, LOW);
  digitalWrite(in3, LOW); digitalWrite(in4, LOW);
}
