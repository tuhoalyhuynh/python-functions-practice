ppl = [ 
    {"name": "Pete", "score": 10},
    {"name": "Mike", "score" : 10},
    {"name": "Pete", "score": -8},
    {"name": "Dexter", "score": 12}
]

def count_scores(people):
    new_dict = {}
    for i in range(len(people)):
        person = people[i]
        new_dict[person["name"]] = person["score"]
    return print(new_dict)

count_scores(ppl)