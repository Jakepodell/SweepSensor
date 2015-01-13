// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 

#include <DistanceSRF04.h>

DistanceSRF04 Dist;
int distance;
 
Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 
int deltaP=45;
int pos2, oldpos;
 
void setup() 
{ 
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
  
  Serial.begin(9600);
  Dist.begin(2,3);  
} 
 
 
void loop() 
{  
   /* if(Serial.available()>0){
      if(pos2!=0)oldpos = pos2;
      pos2 = Serial.parseInt();
      if(pos2!=0){
        int diff = abs(pos2 - oldpos);
        Serial.print("Diff : ");
        Serial.println(diff);
        myservo.write(pos2);
        Serial.println(pos2);
        delay(10*diff);
        distance = Dist.getDistanceInch();
      //Serial.print("position: ");
      Serial.print(pos2);
      //Serial.print("distance: ");
      Serial.print(" | ");
      Serial.println(distance);
      }
    }*/
    myservo.write(pos);    // tell servo to go to position in variable 'pos' 
    delay(500);
    
    distance = Dist.getDistanceInch();
    //Serial.print("position: ");
    Serial.println(distance);
    //Serial.print("distance: ");
    //Serial.print(" | ");
    Serial.println(pos);
    pos+=deltaP;
    if(pos<0 || pos>180){
      deltaP*=-1;
    }

    
    
    
    
  //  Serial.println();
    
} 
