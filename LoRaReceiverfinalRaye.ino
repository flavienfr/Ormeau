#include <SPI.h>
#include <LoRa.h>

const int csPin = 3;
const int resetPin = 6;   
const int irqPin = 2;  

byte recv[255];
byte snd[10];

byte add;
float tmp;
float debit;
String str;

void setup() {
  Serial.begin(19200); //communication local
  while (!Serial);

  Serial1.begin(9600);//communication vers la raspberry
  while (!Serial1);

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

    int crc = 0;
    for (int x=0; x < packetSize-1;x++)
    {
      for (int j=0; j<8; j++)
      {
        crc += recv[x]>>j & 0x01;
      }
    }

    //code de fonction
    if(recv[1]==1/*& recv[packetSize-1] == crc*/)//code fonction (all)
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


      //réponse positice à pierre
      snd[0] = byte(add);
      snd[1] = byte(1); //-------------> code fontion donné par l'utilisateur sur IHM 
      int crc = 0;
      for (int x=0; x < 1;x++)
      {
        for (int j=0; j<8; j++)
        {
          crc += snd[x]>>j & 0x01;
        }
      }
      snd[2] = byte(crc);

      LoRa.beginPacket();
      LoRa.write(snd,2);
      LoRa.endPacket();
  
      String addchar = String(add);
      String tmpchar = String(tmp);
      String debitchar = String(debit);
      str = ";1;"+ addchar + ";" + tmpchar + ";" + debitchar;
      Serial1.println(str);
    }
    

    //envois valeur à la raspberry réception ok ou valeur
    if(verification() == 1)
    {
      for(int i = 0;verification() == 1 & i<5;i++)//fair en sorte de pouvoir quitter la boucle si trop long.
      {
        Serial1.println(str);
        delay(2000);
      }  
    }
  }
}

int verification()
{
  int lu = 0;
  delay(500);
  while(Serial1.available())
  {
    lu = Serial1.read();
  }
  if(lu == 123)
  {
    Serial.println("Réponse Raspberry");
    return 0;
  }
  else if(lu == 234)//code à définir si message mauvais
  {
    return 1;
  }
  else
  {
    Serial.println("Erreur Raspberry");
    return 1;
  }
}
