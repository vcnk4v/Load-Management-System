#include "WiFi.h"
#include "ThingSpeak.h"
#include <time.h>
#include <HTTPClient.h>

//33 32 35 34 39 36

#define ChannelID 2165216
#define WriteAPIKey "AT6PH77TH5THRR6C"
#define CSE_IP "192.168.227.115"/////////////////////////////////////////////////////
#define CSE_PORT 5089
#define OM2M_ORGIN "admin:admin"
#define OM2M_MN "/~/in-cse/in-name/"
#define OM2M_AE "AE-TEST"
#define INTERVAL 15000L

#define OM2M_DATA_CONT_LOAD1 "Load1/Data"
#define OM2M_DATA_CONT_LOAD2 "Load2/Data"
#define OM2M_DATA_CONT_LOAD3 "Load3/Data"
#define OM2M_DATA_CONT_SOLAR "Solar/Data"
#define OM2M_DATA_CONT_CONVENTIONAL "Conventional/Data"
#define OM2M_DATA_CONT_LDR "LDR/Data"
const char * ntpServer = "pool.ntp.org";
long int prev_millis = 0;
unsigned long epochTime;
HTTPClient http;


unsigned long getTime() {
  struct tm timeinfo;
  time_t now = getLocalTime(&timeinfo);
  
  if (!getLocalTime(&timeinfo)) {
    // Serial.println("Failed to obtain time");
    return (0);
  }
  time( &now);
  return now;
}

char* ssid="POCO M4 5G";
char* pass="1234567890";

float curRead(int pin, char cont[]);
float maxSun=3000;
float medSun=2500;
float minSun=2000;
float abso(float a);
int curSun=33;
int curCon=34;
int corPin=32;
int curLoad2=35;
int relayCon=18;
int relayLoad2=19;
int relayLoad3=21;
int relay3=22;
int ldr=39;
void ConnectWifi();
WiFiClient client;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  ConnectWifi();
  configTime(0, 0, ntpServer);
  pinMode(curSun, INPUT);
  pinMode(curCon, INPUT);
  pinMode(corPin, INPUT);
  pinMode(relayCon, OUTPUT);
  pinMode(relayLoad2, OUTPUT);
  pinMode(relayLoad3, OUTPUT);
  pinMode(relay3, OUTPUT);

  ThingSpeak.begin(client);

}

void loop() {
  // put your main code here, to run repeatedly:
  float rLoad3;
  float rLoad1;
  float rSun=curRead(curSun,"Sun: ");
  float rCon=curRead(curCon, "Conventional: ");
  float rLoad2=curRead(curLoad2, "Load2: ");
  curRead(corPin, "Correction: ");

  int rldr=analogRead(ldr);
  Serial.print("LDR: ");
  Serial.println(rldr);


  if(rldr>maxSun)
  {
      digitalWrite(relayCon,0);
      digitalWrite(relayLoad2,1);
      digitalWrite(relayLoad3,1);
      digitalWrite(relay3,0);
      rLoad1=rLoad2;
      rLoad3=rLoad2;
      rCon=0.0;
  }
  else if(rldr>medSun)
  {
      digitalWrite(relayCon,1);
      digitalWrite(relayLoad2,1);
      digitalWrite(relayLoad3,1);
      digitalWrite(relay3,1);
      rLoad1=rLoad2;
      rLoad3=rLoad2;
  }
  else if(rldr>minSun)
  {
      digitalWrite(relayCon,1);
      digitalWrite(relayLoad2,1);
      digitalWrite(relayLoad3,0);
      digitalWrite(relay3,1);
      rLoad1=rLoad2;
      rLoad3=0.0;
  }
  else 
  {
      digitalWrite(relayCon,1);
      digitalWrite(relayLoad2,0);
      digitalWrite(relayLoad3,0);
      digitalWrite(relay3,1);
      rLoad1=rCon;
      rLoad2=0.0;
      rLoad3=0.0;
      rSun=0.0;

  }
  
  Serial.print("SUN:");
  Serial.println(rSun);
  Serial.print("CONVENTIONAL:");
  Serial.println(rCon);
  Serial.print("LOAD1:");
  Serial.println(rLoad1);
  Serial.print("LOAD2:");
  Serial.println(rLoad2);
  Serial.print("LOAD3:");
  Serial.println(rLoad3);
  Serial.print("LDR:");
  Serial.println(rldr);
  ThingSpeak.setField(1,rSun);
  ThingSpeak.setField(2,rCon);
  ThingSpeak.setField(3,rLoad1);
  ThingSpeak.setField(4,rLoad2);
  ThingSpeak.setField(5,rLoad3);
  ThingSpeak.setField(6,rldr);
  Serial.println("...........");

  ThingSpeak.writeFields(ChannelID,WriteAPIKey);
  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



    if (millis() - prev_millis >= INTERVAL) {
    epochTime = getTime();
    String data;
    String server = "http://" + String() + CSE_IP + ":" + String() + CSE_PORT + String() + OM2M_MN;

    http.begin(server + String() + OM2M_AE + "/" + OM2M_DATA_CONT_LOAD1 + "/");

    http.addHeader("X-M2M-Origin", OM2M_ORGIN);
    http.addHeader("Content-Type", "application/json;ty=4");
    http.addHeader("Content-Length", "100");

    // data = "[" + String(epochTime) + ", " + String(occupancy) + ", " + String(distance) +   + "]"; 
    data = "[" + String(epochTime) + ", " + String(rLoad1) + "]"; 
    // data = "["+ String(sensordata) +   + "]"; 
    
    Serial.println(data);
    String req_data = String() + "{\"m2m:cin\": {"

      +
      "\"con\": \"" + data + "\","

      +
      "\"lbl\": \"" + "V1.0.0" + "\","

      //+ "\"rn\": \"" + "cin_"+String(i++) + "\","

      +
      "\"cnf\": \"text\""

      +
      "}}";

    Serial.println(req_data);
    int code = http.POST(req_data);
    http.end();



     http.begin(server + String() + OM2M_AE + "/" + OM2M_DATA_CONT_LOAD2 + "/");

    http.addHeader("X-M2M-Origin", OM2M_ORGIN);
    http.addHeader("Content-Type", "application/json;ty=4");
    http.addHeader("Content-Length", "100");

    // data = "[" + String(epochTime) + ", " + String(occupancy) + ", " + String(distance) +   + "]"; 
    data = "[" + String(epochTime) + ", " + String(rLoad2) + "]"; 
    // data = "["+ String(sensordata) +   + "]"; 
    
    Serial.println(data);
    req_data = String() + "{\"m2m:cin\": {"

      +
      "\"con\": \"" + data + "\","

      +
      "\"lbl\": \"" + "V1.0.0" + "\","

      //+ "\"rn\": \"" + "cin_"+String(i++) + "\","

      +
      "\"cnf\": \"text\""

      +
      "}}";

    Serial.println(req_data);
     code = http.POST(req_data);
    http.end();


    http.begin(server + String() + OM2M_AE + "/" + OM2M_DATA_CONT_LOAD3 + "/");

    http.addHeader("X-M2M-Origin", OM2M_ORGIN);
    http.addHeader("Content-Type", "application/json;ty=4");
    http.addHeader("Content-Length", "100");

    // data = "[" + String(epochTime) + ", " + String(occupancy) + ", " + String(distance) +   + "]"; 
    data = "[" + String(epochTime) + ", " + String(rLoad3) + "]"; 
    // data = "["+ String(sensordata) +   + "]"; 
    
    Serial.println(data);
   req_data = String() + "{\"m2m:cin\": {"

      +
      "\"con\": \"" + data + "\","

      +
      "\"lbl\": \"" + "V1.0.0" + "\","

      //+ "\"rn\": \"" + "cin_"+String(i++) + "\","

      +
      "\"cnf\": \"text\""

      +
      "}}";

    Serial.println(req_data);
    code = http.POST(req_data);
    http.end();

    http.begin(server + String() + OM2M_AE + "/" + OM2M_DATA_CONT_SOLAR + "/");

    http.addHeader("X-M2M-Origin", OM2M_ORGIN);
    http.addHeader("Content-Type", "application/json;ty=4");
    http.addHeader("Content-Length", "100");

    // data = "[" + String(epochTime) + ", " + String(occupancy) + ", " + String(distance) +   + "]"; 
    data = "[" + String(epochTime) + ", " + String(rSun) + "]"; 
    // data = "["+ String(sensordata) +   + "]"; 
    
    Serial.println(data);
   req_data = String() + "{\"m2m:cin\": {"

      +
      "\"con\": \"" + data + "\","

      +
      "\"lbl\": \"" + "V1.0.0" + "\","

      //+ "\"rn\": \"" + "cin_"+String(i++) + "\","

      +
      "\"cnf\": \"text\""

      +
      "}}";

    Serial.println(req_data);
    code = http.POST(req_data);
    http.end();

    http.begin(server + String() + OM2M_AE + "/" + OM2M_DATA_CONT_CONVENTIONAL + "/");

    http.addHeader("X-M2M-Origin", OM2M_ORGIN);
    http.addHeader("Content-Type", "application/json;ty=4");
    http.addHeader("Content-Length", "100");

    // data = "[" + String(epochTime) + ", " + String(occupancy) + ", " + String(distance) +   + "]"; 
    data = "[" + String(epochTime) + ", " + String(rCon) + "]"; 
    // data = "["+ String(sensordata) +   + "]"; 
    
    Serial.println(data);
   req_data = String() + "{\"m2m:cin\": {"

      +
      "\"con\": \"" + data + "\","

      +
      "\"lbl\": \"" + "V1.0.0" + "\","

      //+ "\"rn\": \"" + "cin_"+String(i++) + "\","

      +
      "\"cnf\": \"text\""

      +
      "}}";

    Serial.println(req_data);
    code = http.POST(req_data);
    http.end();

    http.begin(server + String() + OM2M_AE + "/" + OM2M_DATA_CONT_LDR + "/");

    http.addHeader("X-M2M-Origin", OM2M_ORGIN);
    http.addHeader("Content-Type", "application/json;ty=4");
    http.addHeader("Content-Length", "100");

    // data = "[" + String(epochTime) + ", " + String(occupancy) + ", " + String(distance) +   + "]"; 
    data = "[" + String(epochTime) + ", " + String(rldr) + "]"; 
    // data = "["+ String(sensordata) +   + "]"; 
    
    Serial.println(data);
   req_data = String() + "{\"m2m:cin\": {"

      +
      "\"con\": \"" + data + "\","

      +
      "\"lbl\": \"" + "V1.0.0" + "\","

      //+ "\"rn\": \"" + "cin_"+String(i++) + "\","

      +
      "\"cnf\": \"text\""

      +
      "}}";

    Serial.println(req_data);
    code = http.POST(req_data);
    http.end();
    
    prev_millis = millis();
  }
  delay(1900);
}


float curRead(int pin, char cont[]) {
  int t=10;
  float sum=0;
  float v;
  float cur;
  float noise=0.05;
  if(pin==curSun)
    noise=0.15;
  while(t--)
  {  
    int adc=analogRead(pin);
    int corAdc=analogRead(corPin);
    float corV=corAdc*3.3/4095.0;

     v=adc*3.3/4095.0;
    v=abso(v);
    corV=abso(corV);
    cur=v-corV;//2470.345;
    cur/=0.185;
    if(-1*noise<cur && cur<noise)
      cur=0;
    sum+=abso(cur);
    delay(10);
  }
  sum/=10;
  if(sum<noise)
    sum=0;
  return sum;
}



float abso(float a){
  if(a<0)
    return -1*a;
  return a;
}

void ConnectWifi()
{
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi!");
}
