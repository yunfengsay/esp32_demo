#include <Arduino.h>
#include <WiFi.h>
#include <WiFiAP.h>

WiFiAPClass WiFiAP;

// Set these to your desired credentials.
const char *ssid = "ESP32AP";
const char *password = "011111111";

uint8_t x=1;
IPAddress local_IP(192, 168, x, 1);  
IPAddress gateway(192, 168, x, 1);
IPAddress subnet(255, 255, 255, 0);


void setup() {
  Serial.begin(9600);
  Serial.println();
  Serial.println("Configuring access point...");

  // You can remove the password parameter if you want the AP to be open.
  WiFiAP.softAPConfig(local_IP,gateway,subnet);
  WiFiAP.softAP(ssid, password);

  Serial.println("Server started");
}

void loop() {
  delay(2000);
  Serial.print("AP IP address: ");
  Serial.println(WiFiAP.softAPIP());

  Serial.print("softAP Broadcast IP: ");
  Serial.println(WiFiAP.softAPBroadcastIP());

  Serial.print("softAP NetworkID: ");
  Serial.println(WiFiAP.softAPNetworkID());

  Serial.print("softAP SubnetCIDR: ");
  Serial.println(WiFiAP.softAPSubnetCIDR());

  Serial.print("softAP Hostname: ");
  Serial.println(WiFiAP.softAPgetHostname());

  Serial.print("softAP macAddress: ");
  Serial.println(WiFiAP.softAPmacAddress());

  Serial.print("softAP StationNum: ");
  Serial.println(WiFiAP.softAPgetStationNum());
}

