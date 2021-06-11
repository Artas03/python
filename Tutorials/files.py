file = open("teams.txt", "w")

teams = ["Phoenix Suns", "Los Angeles Lakers", "Denver Nuggets", "Brooklyn Nets", "Utah Jazz"]

for i in teams:
    newline = f"{i} are amazing" + "\n"
    file.write(newline)

file.close()

with open("teams.txt", "r") as file:
    lines = file.readlines()
    for i in range(0,4):
      print(lines[i])

