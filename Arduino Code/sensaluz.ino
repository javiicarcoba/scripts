
int lectura_sensor;
int luz = 12;
String accion;

String estado_led(){
  if (analogRead(A1)>0)
    return "El led esta encendido";
  else
    return "El led esta apagado";
}

void sensando(){
  lectura_sensor = (analogRead(A0)*100)/1000;
  if(lectura_sensor <= 40)
    digitalWrite(luz,HIGH);
  else
    digitalWrite(luz,LOW);
}

void setup() {
  Serial.begin(9600);
  pinMode(luz, OUTPUT);
}

void loop() {
  sensando();
}
