
#include <DistanceSRF04.h>

DistanceSRF04 Dist;
int distance;


// LED on Pin 13 for digital on/off demo

void setup() 
{ 
  // Attach each Servo object to a digital pin
  Serial.begin(9600);
  Dist.begin(2,3);
 
} 

void loop(){

  Serial.println(Dist.getDistanceInch());
  //Serial.print("\nDistance in inches: ");
  //Serial.println(distance); 
  
  //Serial.write(523);
  delay(50);
  
}


