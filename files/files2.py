file = open("teams.txt", "r")

outfile = ""

for i in range(0,5):
    if i == 0:
        file.readline()
    else:
        outfile = outfile + file.readline()


file = open("teams.txt", "w")

file.write("This is a new line \n")
file.write(outfile)



file = open("teams.txt", "r")

lines = file.readlines()

print(lines)