import json
dirr = {
    "10AM - 11AM":"10AM - 11AM",
    "11AM - 12PM":'11AM TO 12PM',
    "12PM - 1PM":"12PM - 1PM",
    "2PM - 3PM":"2PM - 3PM",
    "3PM - 4PM":"3PM - 4PM"
}

time = json.dumps(dirr)
print(type(time))

print(type(json.loads(time)))

li = [] 
for i in json.loads(time).values():
    li.append(i)
print(li)