# gets all combinations of two items from a list

categories = ["Plains",
              "Island",
              "Swamp",
              "Mountains",
              "Forest"]

for i, j in enumerate(categories):
    for k in categories[i+1:]:
        print(j + ", " + k)

input()