long valor;
#define led1 13
#define led2 12
#define led3 11
#define led4 10
int delay_bet_leds = 100;
int last_delay = 1000; 
long last_value = 0;

void turn_leds(int mode){
  for(int i = 13; i > 9; i--){
    digitalWrite(i, mode);
    delay(delay_bet_leds);
  }
  delay(last_delay);
} 

void setup() {
  Serial.begin(9600);
  Serial.println("Inicio de sketch - valores del potenciometro");
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
 
}
 
void loop() {
  // leemos del pin A0 valor
  valor = analogRead(A0);
  if(valor != last_value){
    Serial.print("El valor es = ");
    Serial.println(valor);
    delay_bet_leds = 1023 - valor;
    Serial.print("dbl = ");
    Serial.println(delay_bet_leds);
  }
  turn_leds(1);
  turn_leds(0);
  //Imprimimos por el monitor serie

  last_value = valor;
  delay(1000);
}
