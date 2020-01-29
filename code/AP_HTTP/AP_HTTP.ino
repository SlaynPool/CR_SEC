#include <WiFi.h>
#include <WebServer.h>
#define CHANNEL 5
const char *ssid="NicolasV";
const char *pass="12345678";
const char *www_realm="Authentification ESP32";
const char *www_username="Toto";
const char *www_password="Titiri";
IPAddress ip(192,168,42,1);
IPAddress gateway(192,168,42,254);
IPAddress subnet(255,255,255,0);
WebServer server(80);

void wifiAPSetup() {
  Serial.println("wifiAPSetup...");
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(ip,gateway,subnet); // Configuration DHCP
  //WiFi.softAP(ssid,pass); // DHCP on 192.168.4.0/24 by default if no WiFi.softAPConfig()
  WiFi.softAP(ssid,pass,CHANNEL);
  IPAddress apIP=WiFi.softAPIP();
  Serial.printf("IP address: %s\r\n",apIP.toString().c_str());
  Serial.printf("BSSID: %s\r\n",WiFi.softAPmacAddress().c_str());
}
void handleRoot() {
  server.send(200,"text/html","<h1>ESP32 - Ça marche!</h1>");
}
void handleLogin() {
  if (!server.authenticate(www_username,www_password)) {
    return server.requestAuthentication(BASIC_AUTH,www_realm,"Authentication Failed");
    //return server.requestAuthentication(DIGEST_AUTH,www_realm,"Authentication2 Failed");
  }
  server.send(200,"text/html","<h1>Bienvenue sur la zone sécurisée !</h1>");
}
void handleNotFound() {
  server.send(404,"text/plain","Fichier non trouvé !");
}
void webSetup() {
  Serial.println("WEB server setup...");
  server.on("/",handleRoot);
  server.on("/login",handleLogin);
  server.onNotFound(handleNotFound);
  server.begin();
  Serial.println("WEB server running...");
}
void setup() {
  delay(1000);
  Serial.begin(115200);
  Serial.println("Setup...");
  wifiAPSetup();
  webSetup();
  Serial.println("Setup done.");
}
void loop() {
  server.handleClient();
}
