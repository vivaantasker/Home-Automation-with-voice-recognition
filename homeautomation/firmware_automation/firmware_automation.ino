
#include <Arduino.h>

void setup() {
    Serial.begin(115200);
    pinMode(2,OUTPUT);
    pinMode(4,OUTPUT);
    pinMode(5,OUTPUT);
    pinMode(12,OUTPUT);
    pinMode(13,OUTPUT);
    pinMode(14,OUTPUT);
    pinMode(15,OUTPUT);
    pinMode(18,OUTPUT);
    pinMode(19,OUTPUT);
    pinMode(21,OUTPUT);
    pinMode(22,OUTPUT);
    pinMode(23,OUTPUT);
    pinMode(25,OUTPUT);
    pinMode(26,OUTPUT);
    pinMode(27,OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        // Read the first byte (should be 0xFF)
        byte startByte = Serial.read();
        Serial.print("Start Byte: ");
        Serial.println(startByte, HEX); // Debug output

        if (startByte == 0xFF) {
            // Read the number of bytes to follow
            if (Serial.available() > 0) {
                byte numBytes = Serial.read();
                Serial.print("Number of bytes: ");
                Serial.println(numBytes);

                // Read the subsequent bytes
                for (int i = 0; i < numBytes; i++) {
                    if (Serial.available() >= 1) {  
                        byte dataByte = Serial.read();
                        Serial.print("Data Byte: ");
                        Serial.println(dataByte, HEX);

                        // Extract the number (5 bits) and the on/off state (1 bit)
                        byte number = dataByte >> 3; // Take upper 5 bits
                        byte onOffState = (dataByte >> 2) & 0x01; // 1 bit for on/off
                        byte delaySeconds = dataByte & 0x03; // Take lower 2 bits for delay (0-3 seconds)
                        
                        Serial.print("Entry ");
                        Serial.print(i + 1);
                        Serial.print(": Number = ");
                        Serial.print(number);
                        Serial.print(", On/Off State = ");
                        Serial.print(onOffState == 1 ? "ON" : "OFF");
                        Serial.print(", Delay = ");
                        Serial.println(delaySeconds);
                        
                        // Handle the on/off state
                        if (onOffState == 1) {
                            digitalWrite(number,HIGH);//Serial.println("Action: ON");
                        } else {
                            digitalWrite(number,LOW);//Serial.println("Action: OFF");
                        }
                        
                        // Delay for the specified seconds
                        delay(delaySeconds * 1000); // Delay in seconds
                    } else {
                        Serial.println("Not enough data available for the next byte.");
                    }
                }
            } else {
                Serial.println("No number of bytes available.");
            }
        } else {
            Serial.println("Start byte not recognized.");
        }
    }
}
