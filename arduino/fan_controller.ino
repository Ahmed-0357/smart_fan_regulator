#include <Servo.h>
#define servoPin 3
#define temperature A0

Servo myservo;

int human_count; // number of individuals retrieved from computer vision
int fan_speed; // fan speed
  
void setup()
{
myservo.attach(servoPin);
pinMode(temperature, INPUT);
Serial.begin(9600); // Initialize serial port
while (!Serial) {} //wait serial connection
human_count = 2; 
}

void loop()
{
// ---- temp reading ----  
int tempReading = analogRead(temperature);
// If using 5v input
float voltage = tempReading * 5.0; 
// Divided by 1024
voltage /= 1024.0;
//Converting from 10mv per degree
float tempC = (voltage - 0.5) * 100;
 
// ---- number of individuals ----
while (Serial.available() > 0) 
{
human_count = Serial.read() ;
}

// ---- set fan speed (0 - 90)----
if(human_count == 0) 
{
  fan_speed = 90;
}
else 
{ 
  float ev = 0.5*human_count + 0.1*tempC; 
  float norm_value = pow(2.71, ev)/(1+pow(2.71, ev));
  fan_speed = 90 * (1-norm_value); 

}
 myservo.write(fan_speed);
       
// ---- print temp value, number of individuals and fan speed ----
Serial.print(tempC);
Serial.print(",    ");
Serial.print(human_count);
Serial.print(",    ");
Serial.println((90-fan_speed));
}