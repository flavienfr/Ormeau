#include <SPI.h>
#include <LoRa.h>

void setup() {
  Serial1.begin(9600);
  while (!Serial1);

  Serial1.println("LoRa Receiver");

  if (!LoRa.begin(915E6)) {
    Serial1.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  // try to parse packet
  int packetSize = LoRa.parsePacket();
  if (packetSize) {

    // read packet
    while (LoRa.available()) {
      Serial1.print((char)LoRa.read());
    }
    
    Serial1.println();
    // print RSSI of packet
    //Serial.print("' with RSSI ");
    //Serial.println(LoRa.packetRssi());
  }
}
