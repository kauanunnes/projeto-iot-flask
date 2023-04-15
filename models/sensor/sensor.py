import csv
filename = 'C:/Users/kaua.nunes/Desktop/faculdade/experiancia-criativa/projeto-pbl/models/sensor.csv'

sensors = []


def refresh():  
  global sensors
  with open(filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    sensors = list(reader)
  
refresh()

def add_sensor(sensor_name,water_qtd,user_id):
  with open(filename, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)            
    writer.writerow([len(sensors) + 1, sensor_name, water_qtd, user_id])
  refresh()

def sensors_by_id(user_id):
    user_sensors = []
    for item in sensors:
      if item['user_id'] == user_id:
        user_sensors.append(item)        
    return user_sensors