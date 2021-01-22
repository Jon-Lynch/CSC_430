import matplotlib.pyplot as plt

infile = open('crymland.txt')
content = infile.readlines()

data = []
for item in content:
    item.rstrip('\n')
    data.append(item)

print(data)
