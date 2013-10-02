from rodents import Rodent
rodents = {}
file = open('rodents.csv')
for line in file:
    #line = line.rstrip()
    tag, weight = line.split(',')
    # check to see whether the tag_id is in my dictionary
    if tag not in rodents:
        rodents[tag] = Rodent(tag)
    
    rodents[tag].add_weight(weight)
        
for key in rodents:
    print rodents[key].__dict__

