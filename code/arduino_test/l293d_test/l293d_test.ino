const int IN1 = 2;
//3번은 서보모터
const int IN2 = 4;
const int IN3 = 7;
const int IN4 = 8;
const int EN1 = 5;
const int EN2 = 6;


void setup() {
  // put your setup code here, to run once:
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(EN1, OUTPUT);
  pinMode(EN2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(3000);
  digitalWrite(EN1, HIGH);
  digitalWrite(EN2, HIGH);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  delay(1000);
  digitalWrite(EN1, LOW);
  digitalWrite(EN2, LOW);
  delay(5000);
}
