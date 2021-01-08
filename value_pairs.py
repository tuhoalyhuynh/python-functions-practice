object_one = {"name": 'One', "location": 'Remote', "age": 1}
object_two = {"name": 'Two', "location": 'San Francisco'}

def value_pairs(object1, object2, key):
    arr = []
    arr.append(object1[key])
    arr.append(object2[key])
    return print(arr)

value_pairs(object_one, object_two, "location")