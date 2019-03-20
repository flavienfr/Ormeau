#include <SPI.h>
#include <LoRa.h>

const int csPin = 3;
const int resetPin = 6;   
const int irqPin = 2;  

byte recv[255];
byte add;
float tmp;
float debit;
int crc;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  LoRa.setPins(csPin, resetPin, irqPin);
  Serial.println("LoRa Receiver");
 
  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  // try to parse packet
  int packetSize = LoRa.parsePacket();
  if (packetSize) 
  {
    // received a packet
    int i= 0;
    
    Serial.print("receive packet of ");
    Serial.print(packetSize);
    Serial.print(" bytes : ");
    
    // read packet
    while (LoRa.available()) {
      byte b = LoRa.read();
      recv[i]=b;
      
      Serial.print(b);
      Serial.print(":");
      i++;
    }

    crc = 0;
    for (int x=0; x < packetSize;x++)
    {
      for (int j=0; j<8; j++)
      {
        crc += recv[x]>>j & 0x01;
      }
    }

    
    if(recv[1]==1)//code fonction (all) et crc calculé == crc recu
    {
      add = recv[0];
      tmp = (recv[2]+recv[3]);
      tmp /= 10;
      debit = recv[4]+recv[5];
      debit /=10;
      
      Serial.println("");
      Serial.print("Adresse : ");
      Serial.println(add);
      Serial.print("Temperature : ");
      Serial.println(tmp);
      Serial.print("Debit : ");
      Serial.println(debit);
      Serial.print("crc calculé: ");
      Serial.println(crc);
    }
  }
}
