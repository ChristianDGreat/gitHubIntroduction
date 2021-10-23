import django
print(django.get_version)

persons = [{"christian":"king2"},{"christian":"king3"},{"christian":"king1"}]




persons.sort(key=lambda k:k["christian"])

print(persons)
