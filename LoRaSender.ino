#include <SPI.h>
#include <LoRa.h>

float debit = 0;
float tmp = 25.3;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!LoRa.begin(915E6)) {
    Serial.println("666;666");
    while (1);
  }
}

void loop() {
  // send packet
  LoRa.beginPacket();
  LoRa.print(debit);
  LoRa.print(";");
  LoRa.print(tmp);
  LoRa.endPacket();

  debit++;

  delay(1000);
}
