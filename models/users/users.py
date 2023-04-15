import csv
from models.user_consumption.user_consumption import create_today_date
filename = 'C:/Users/kaua.nunes/Desktop/faculdade/experiancia-criativa/projeto-pbl/models/users.csv'

users = []
with open(filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    users = list(reader)

def user_by_email(email):
    user = {}
    for item in users:
      if item['email'] == email:
          user = {
              'id': item['id'],
              'name': item['name'],
              'email': item['email'],
              'weight': int(item['weight'])
          }
    return user

def register(name, email, password, weight):
    flag = True
    for user in users:
        if email == user['email']:
            flag = False
    if flag:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)            
            writer.writerow([len(users) + 1, name, email, password, False, weight])
        refresh()
        create_today_date(user_by_email(email)['id'])
    return flag
    
def refresh():
    global users
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        users = list(reader)