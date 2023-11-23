#include <Servo.h>

Servo myservo;

void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT); //IN1
  pinMode(4, OUTPUT); //IN2
  pinMode(7, OUTPUT); //IN3
  pinMode(8, OUTPUT); //IN4
  pinMode(5, OUTPUT); //EN1
  pinMode(6, OUTPUT); //EN2

  pinMode(A7, INPUT); //Right IR
  pinMode(A6, INPUT); //Left IR
  myservo.attach(3);
  Serial.begin(9600);
}

int L_IR_Value = 0;
int R_IR_Value = 0;
// 0일때는 흰색입니다... 1일때 검정색입니다... 무튼 그렇습니다...

void line()
{
  while (1) {
    if (analogRead(A6) >= 800) {
      L_IR_Value = 0;
    }
    else {
      L_IR_Value = 1;
    }
    if (analogRead(A7) >= 800) {
      R_IR_Value = 0;
    }
    else {
      R_IR_Value = 1;
    }
    if (L_IR_Value == 1 && R_IR_Value == 1) //정지
    {
      digitalWrite(2, LOW);
      digitalWrite(4, LOW);
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      break;
    }
    if (L_IR_Value == 0 && R_IR_Value == 0) //전진
    {
      digitalWrite(2, HIGH);
      digitalWrite(4, LOW);
      digitalWrite(7, HIGH);
      digitalWrite(8, LOW);
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
    }
    if (L_IR_Value == 0 && R_IR_Value == 1) //우회전
    {
      digitalWrite(2, HIGH);
      digitalWrite(4, LOW);
      digitalWrite(7, HIGH);
      digitalWrite(8, LOW);
      analogWrite(5, 255);
      analogWrite(6, 180);
    }
    if (L_IR_Value == 1 && R_IR_Value == 0) //좌회전
    {
      digitalWrite(2, HIGH);
      digitalWrite(4, LOW);
      digitalWrite(7, HIGH);
      digitalWrite(8, LOW);
      analogWrite(5, 180);
      analogWrite(6, 255);
    }
    /*
      Serial.print("L:");
      Serial.println(analogRead(A6));
      //Serial.println(L_IR_Value);
      Serial.print("R:");
      Serial.println(analogRead(A7));
      //Serial.println(R_IR_Value);
      delay(1000);
    */
  }
}

void line_s()
{
  while (1) {
    if (analogRead(A6) >= 800) {
      L_IR_Value = 0;
    }
    else {
      L_IR_Value = 1;
    }
    if (analogRead(A7) >= 800) {
      R_IR_Value = 0;
    }
    else {
      R_IR_Value = 1;
    }
    if (L_IR_Value == 1 && R_IR_Value == 1) //정지
    {
      digitalWrite(2, LOW);
      digitalWrite(4, LOW);
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      break;
    }
    if (L_IR_Value == 0 && R_IR_Value == 0) //전진
    {
      digitalWrite(2, HIGH);
      digitalWrite(4, LOW);
      digitalWrite(7, HIGH);
      digitalWrite(8, LOW);
      analogWrite(5, 80);
      analogWrite(6, 80);
    }
    if (L_IR_Value == 0 && R_IR_Value == 1) //우회전
    {
      digitalWrite(2, HIGH);
      digitalWrite(4, LOW);
      digitalWrite(7, LOW);
      digitalWrite(8, HIGH);
      analogWrite(5, 80);
      analogWrite(6, 80);
    }
    if (L_IR_Value == 1 && R_IR_Value == 0) //좌회전
    {
      digitalWrite(2, LOW);
      digitalWrite(4, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(8, LOW);
      analogWrite(5, 80);
      analogWrite(6, 80);
    }
    /*
      Serial.print("L:");
      Serial.println(analogRead(A6));
      //Serial.println(L_IR_Value);
      Serial.print("R:");
      Serial.println(analogRead(A7));
      //Serial.println(R_IR_Value);
      delay(1000);
    */
  }
}

void motor(int lspd, int rspd, int val)
{
  digitalWrite(2, HIGH);
  digitalWrite(4, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, LOW);
  analogWrite(5, lspd);
  analogWrite(6, rspd);
  delay(val);
  digitalWrite(2, LOW);
  digitalWrite(4, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
}

int runflag = 0;
void loop() {
  // put your main code here, to run repeatedly:
  if (runflag == 0) //코드 실행부분
  {
    delay(10000);
    line();
    motor(255,255,100);
    line();
    motor(255,255,100);
    line();
    motor(255,255,100);
    runflag = 1;
  }
  else {}
}
