/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://www.arduino.cc

  This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
 */

 #define COMMON_ANODE
int redPin = 11;
int greenPin = 7;
int bluePin = 6;

int buttonPin = 0;
int buttonState = 0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
 // pinMode(13, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);  
  
    // initialize the LED pin as an output:
  pinMode(greenPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

// the loop function runs over and over again forever

  const int buttonPin = 2;     // the number of the pushbutton pin
  const int greenPin =  13;      // the number of the LED pin

// variables will change:
int buttonState = 0; 
int x = 2;

void loop(){
  if (x < 5){
    pinMode(10, OUTPUT);

    digitalWrite(10, HIGH);   // turn the LED on (HIGH is the voltage level)
                // wait for a second
    digitalWrite(10, HIGH);    // turn the LED off by making the voltage LOW
           // wait for a second
    setColor(0, 0, 0); //setting white LED to green 

      // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }

  }
  
}


void setColor(int red, int green, int blue){
  #ifdef COMMON_ANODE
    red = 255 - red;
    green = 255 - green;
    blue = 255 - blue;
  #endif
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);  
}
/*void loop() {
  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);              // wait for a second

  pinMode(12, OUTPUT);

  digitalWrite(12, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(12, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);              // wait for a second

    pinMode(11, OUTPUT);

  digitalWrite(11, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(11, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);              // wait for a second


  pinMode(10, OUTPUT);

  digitalWrite(10, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(10, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);              // wait for a second

    pinMode(9, OUTPUT);

  digitalWrite(9, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(9, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);              // wait for a second
}*/
