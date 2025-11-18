import random
import time
from datetime import datetime

class VirtualSensor:
    def __init__(self, name, min_val, max_val):
        self.name = name
        self.min_val = min_val
        self.max_val = max_val

    def read(self):
        return round(random.uniform(self.min_val, self.max_val), 2)

class SensorSystem:
    def __init__(self):
        self.temp_sensor = VirtualSensor("Temperature", 18.0, 32.0)
        self.humidity_sensor = VirtualSensor("Humidity", 35.0, 85.0)
        self.temp_threshold = 30.0
        self.humidity_threshold = 75.0
        self.log_file = "sensor_log.txt"

    def read_sensors(self):
        temp = self.temp_sensor.read()
        humidity = self.humidity_sensor.read()
        return temp, humidity

    def check_alerts(self, temp, humidity):
        alerts = []
        if temp > self.temp_threshold:
            alerts.append(f"⚠️ High Temperature Alert! ({temp}°C)")
        if humidity > self.humidity_threshold:
            alerts.append(f"⚠️ High Humidity Alert! ({humidity}%)")
        return alerts

    def log_data(self, temp, humidity):
        with open(self.log_file, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}, Temp: {temp}, Humidity: {humidity}\n")

    def run(self, interval=2, duration=20):
        print("📡 SensorSim Monitoring Started...")
        start_time = time.time()
        while time.time() - start_time < duration:
            temp, humidity = self.read_sensors()
            print(f"🌡️ Temp: {temp}°C | 💧 Humidity: {humidity}%")

            alerts = self.check_alerts(temp, humidity)
            for alert in alerts:
                print(alert)

            self.log_data(temp, humidity)
            time.sleep(interval)

        print("📁 Monitoring Ended. Data logged to sensor_log.txt")

# Run Simulation
if __name__ == "__main__":
    system = SensorSystem()
    system.run()import random
import time
from datetime import datetime

class VirtualSensor:
    def __init__(self, name, min_val, max_val):
        self.name = name
        self.min_val = min_val
        self.max_val = max_val

    def read(self):
        return round(random.uniform(self.min_val, self.max_val), 2)

class SensorSystem:
    def __init__(self):
        self.temp_sensor = VirtualSensor("Temperature", 18.0, 32.0)
        self.humidity_sensor = VirtualSensor("Humidity", 35.0, 85.0)
        self.temp_threshold = 30.0
        self.humidity_threshold = 75.0
        self.log_file = "sensor_log.txt"

    def read_sensors(self):
        temp = self.temp_sensor.read()
        humidity = self.humidity_sensor.read()
        return temp, humidity

    def check_alerts(self, temp, humidity):
        alerts = []
        if temp > self.temp_threshold:
            alerts.append(f"⚠️ High Temperature Alert! ({temp}°C)")
        if humidity > self.humidity_threshold:
            alerts.append(f"⚠️ High Humidity Alert! ({humidity}%)")
        return alerts

    def log_data(self, temp, humidity):
        with open(self.log_file, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}, Temp: {temp}, Humidity: {humidity}\n")

    def run(self, interval=2, duration=20):
        print("📡 SensorSim Monitoring Started...")
        start_time = time.time()
        while time.time() - start_time < duration:
            temp, humidity = self.read_sensors()
            print(f"🌡️ Temp: {temp}°C | 💧 Humidity: {humidity}%")

            alerts = self.check_alerts(temp, humidity)
            for alert in alerts:
                print(alert)

            self.log_data(temp, humidity)
            time.sleep(interval)

        print("📁 Monitoring Ended. Data logged to sensor_log.txt")

# Run Simulation
if __name__ == "__main__":
    system = SensorSystem()
    system.run()
