
int x=0;
//int arr[5000][2];
float ave = 0.0;
int i = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}

/*
MAKAKA-GRADUATE AKO ON TIME NO MATTER HOW LONG IT TAKES
*/

void loop() {
  // put your main code here, to run repeatedly:
  x = analogRead(A0);
  delay(1);
  if(i<700){
//    arr[i][0] = i;
//    arr[i][2] = x;
    Serial.print(i);
    Serial.print(",");
    Serial.print(x);
    Serial.print(",");
    ave += x;
    if(i%10==0){
      ave /= 10;
      Serial.print(ave);
      }
    else {
      Serial.print(0);
    }
    Serial.println();
    i++;
    }
  
//  Serial.println(millis());
}
