students={
   "abdul" : 100,
  "Ahmed" : 500,
  "waleed": 300,
  "hayye": 400,
  "zain": 200
}
topper_name = max(students, key=students.get)
topper_marks = students[topper_name]

print(f"Topper is {topper_name} with {topper_marks} marks.")