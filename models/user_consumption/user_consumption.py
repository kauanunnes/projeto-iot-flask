import csv
from datetime import date, datetime, timedelta
# from users.users import users
filename = 'C:/Users/kaua.nunes/Desktop/faculdade/experiancia-criativa/projeto-pbl/models/water_day_by_user.csv'
today = date.today()

consumptions = []
with open(filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    consumptions = list(reader)

def find_by_date_and_id(date, id):
    consumption = {}
    for item in consumptions:
      if item['user_id'] == id and item['date'] == date:
        consumption = item
    return consumption

def increase_consumption(date, id, qtd):
  for row in consumptions:
    if row['user_id'] == id and row['date'] == date:
        row['total_consumption'] = int(qtd) + int(row['total_consumption'])
  with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['date', 'user_id', 'total_consumption'])
    writer.writeheader()
    writer.writerows(consumptions)

def create_today_date(id):
   if any(find_by_date_and_id(today.strftime("%d-%m-%Y"), id)):
      print(find_by_date_and_id(today.strftime("%d-%m-%Y"), id))
      return
   with open(filename, mode='a', newline='') as file:
    # create a writer object
    writer = csv.writer(file)
    
    # write the new row to the file
    writer.writerow([today.strftime("%d-%m-%Y"), id, 0])

def refresh():
   global consumptions
   with open(filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    consumptions = list(reader)
