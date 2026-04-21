# Creating an empty dictionary
student = {}
# Adding key-value pairs
student["name"] = "Rahul"
student["age"] = 20
student["course"] = "Python"
print("Dictionary after adding elements:")
print(student)
# Updating a value
student["age"] = 21
print("\nDictionary after updating a value:")
print(student)
# Deleting a key-value pair
del student["course"]
print("\nDictionary after deleting a key-value pair:")
print(student)

Dictionary after adding elements:
{'name': 'Rahul', 'age': 20, 'course': 'Python'}
Dictionary after updating a value:
{'name': 'Rahul', 'age': 21, 'course': 'Python'}
Dictionary after deleting a key-value pair:
{'name': 'Rahul', 'age': 21}