void setup() {
  // put your setup code here, to run once:

}

boolean inWater() {
  //Is the boy in the water?
  return false; //placeholder
}

int getGPS() {
  //Where are we?
  return new int[2]; //placeholder
}

void broadcast() {
  while (inWater()) {
    Serial.print(getGPS()); //Tell the drone where we are until we leave
    delay(500); //2 Hz cycle
  }
}

void lower() {
  //lower the pod
}

void raze() {
  //raze the pod (raise is a keyword)
}

void loop() {
  while (!inWater()) {
    delay(1000);
  }
  lower();
  delay(30*60*1000); //wait 30 mins (in miliseconds)
  raze();
  broadcast();
}
