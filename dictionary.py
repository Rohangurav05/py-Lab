students={
    101:{"Name":"Rohan", "Scores":[85, 90, 78]},
    102:{"Name":"Priya", "Scores":[92, 88, 95]},
    103:{"Name":"Amit", "Scores":[25, 30, 29]}
}

for sid,details in students.items():
   avg=sum(details["Scores"])/len(details["Scores"])
   details["Average"]=avg
   details["passed"]=avg>=30

print("Students who passed :")
for sid,details in students.items():
   if details["passed"]:
      print(details["Name"])
