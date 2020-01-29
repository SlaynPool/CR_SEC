code$ head -n15 AP_HTTP.ino 
#include <WiFi.h>
#include <WebServer.h>
#define CHANNEL 5
const char *ssid="NicolasV";
const char *pass="87654321";
const char *www_realm="Authentification ESP32";
const char *www_username="Toto";
const char *www_password="Totoro";
IPAddress ip(192,168,42,1);
IPAddress gateway(192,168,42,254);
IPAddress subnet(255,255,255,0);
WebServer server(80);

void wifiAPSetup() {
  Serial.println("wifiAPSetup...");
................
