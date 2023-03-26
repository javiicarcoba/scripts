// Incluimos librería
#include <DHT.h>

#define DHTPIN 11
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);
float temp;
float hum;
 
void setup() {
  Serial.begin(9600);
  dht.begin();
 
}
 
void loop() {
  hum = dht.readHumidity();
  temp = dht.readTemperature();
 
  Serial.print("Humedad: ");
  Serial.print(hum);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(temp);
  Serial.println(" ºC");
  delay(2000);
}
