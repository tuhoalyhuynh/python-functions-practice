obj1 = {"company": 'General Assembly', "course": 'Software Engineering Immersive'}

def does_key_exist(obj, key):
    if key in obj:
        return print(True)
    else:
        return print(False)

does_key_exist(obj1, "company")
does_key_exist(obj1, "year")