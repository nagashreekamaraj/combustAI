#include "DHT.h"

// ----- DHT22 Setup -----
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

// ----- MQ-2 Setup -----
#define MQ2PIN 32
#define MQ2_THRESHOLD 3000  // Gas warning threshold

// ----- LED & Buzzer Setup -----
#define LED_PIN 16
#define BUZZER_PIN 18

int prevMQ2 = 0; // store previous MQ-2 reading

void setup() {
  Serial.begin(115200);
  dht.begin();

  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  Serial.println("Sensors & Alerts Initialized...");
}

void loop() {
  // --- Read DHT22 ---
  float temperature = dht.readTemperature();  // °C
  float humidity = dht.readHumidity();        // %

  // --- Read MQ-2 ---
  // For testing without gas, we simulate variation:
  // int mq2Analog = random(1000, 4000); // Uncomment for simulation
  int mq2Analog = analogRead(MQ2PIN);      // Real reading

  float mq2Voltage = mq2Analog * (3.3 / 4095);

  // --- Display Sensor Readings ---
  Serial.println("----------- Sensor Readings -----------");
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("DHT22 read error!");
  } else {
    Serial.print("Temperature: "); Serial.print(temperature); Serial.println(" °C");
    Serial.print("Humidity: "); Serial.print(humidity); Serial.println(" %");
  }

  Serial.print("MQ-2 Analog Value: "); Serial.println(mq2Analog);
  Serial.print("MQ-2 Voltage: "); Serial.print(mq2Voltage); Serial.println(" V");

  // --- Gas Alert Logic ---
  if (mq2Analog > MQ2_THRESHOLD && prevMQ2 <= MQ2_THRESHOLD) {
    Serial.println("⚠ WARNING: Incomplete Combustion Detected!");

    // Blink LED and beep buzzer 3 times
    for (int i = 0; i < 3; i++) {
      digitalWrite(LED_PIN, HIGH);
      digitalWrite(BUZZER_PIN, HIGH);
      delay(300);
      digitalWrite(LED_PIN, LOW);
      digitalWrite(BUZZER_PIN, LOW);
      delay(300);
    }
  }

  prevMQ2 = mq2Analog; // update previous value

  Serial.println("--------------------------------------\n");
  delay(2000); // check every 2 seconds
}
