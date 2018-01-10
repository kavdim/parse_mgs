import postgresql

db = postgresql.open('pq://root:root@localhost:5432/mgs')

query = db.query("SELECT object.object_number, object.name, client_number, client.name, client.settings FROM client, object WHERE client.object_id = object.object_id and object.group_id = '6' and client.name != 'Сибирь-Мониторинг Валявин Алексей' ORDER BY object.object_number, client_number")

phone1 = "" phone2 = "" address = "" for qu in query:

s = qu[4].split("\r\n")
if len(s) == 4:
    phone1 = s[0].strip("Phone1=")
    phone2 = s[1].strip("Phone2=")
    address = s[2].strip("Address=")
print(phone1, " - ", phone2, " - ", address)
if len(s) == 8:
    phone1 = s[2].strip("Phone1=")
    phone2 = s[3].strip("Phone2=")
    address = s[4].strip("Address=")
print(phone1, " - ", phone2, " - ", address)
print(qu[0], "; ", qu[1], "; ", qu[2], "; ",qu[3], "; ", phone1, "; ", phone2, "; "
