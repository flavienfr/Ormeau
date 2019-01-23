#include <SPI.h>
#include <LoRa.h>

int debit = 0;
int tmp = 25.3;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Sender");

  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {

  // send packet
  LoRa.beginPacket();
  LoRa.print("D:");
  LoRa.print(debit);
  LoRa.print("T:");
  LoRa.print(tmp);
  LoRa.endPacket();

  debit++;

  delay(50);
}
