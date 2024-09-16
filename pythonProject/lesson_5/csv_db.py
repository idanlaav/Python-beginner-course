import csv
def create_user(username, password):
    try:
        print(username)
        print(password)
        f = open('data.csv', 'a', newline='')
        writer = csv.DictWriter(f, fieldnames=['username','password'])
        writer.writerow({'username':username,'password':password})
    except Exception:
        return False
    return True

def login(username,password):
    f = open('data.csv', 'r')
    reader =csv.DictReader(f)
    for row in reader:
        if row["username"] == username and row["password"] == password:
            return True
    return False