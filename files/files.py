file = open("teams.txt", "w")

file.write("Arsenal \n")
file.write("Tottenham \n")
file.write("Chelsea \n")
file.write("Manchester United \n")
file.write("Liverpool \n")

file.close()

file = open("teams.txt", "r")

print(file.readline())
file.readline()
file.readline()
file.readline()
print(file.readline())

file.close()

