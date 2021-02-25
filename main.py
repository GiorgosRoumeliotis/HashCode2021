# THIS SOLUTION IS MADE BY GEORGIOS ROUMELIOTIS AND MARILENA PAIRI MONOKROUSOU
#                               FEBRUARY 25th 2021

from colorama import Fore


################################ GLOBAL ####################################

simulation = 0
intersections = 0 
streets = 0 
cars = 0

dict_array = []
diadromi = []


def code_couple_logo():
	print (Fore.RED + "\n"
	" ██████  ██████  ██████  ███████       ██ ██████       ██████  ██████  ██    ██ ██████  ██      ███████ \n"
	"██      ██    ██ ██   ██ ██           ██       ██     ██      ██    ██ ██    ██ ██   ██ ██      ██      \n"
	"██      ██    ██ ██   ██ █████       ██    █████      ██      ██    ██ ██    ██ ██████  ██      █████   \n"
	"██      ██    ██ ██   ██ ██           ██       ██     ██      ██    ██ ██    ██ ██      ██      ██      \n"
	" ██████  ██████  ██████  ███████       ██ ██████       ██████  ██████   ██████  ██      ███████ ███████ \n"
	"                                                                                                        ")

	print(Fore.YELLOW +"\t\t\t| |       _  __       __ _  _  __   __  _ __    \n"
	"\t\t\t===   |_||_|(_ |_|   /  / \\| \\|_     _)/ \\ _)/| \n"
	"\t\t\t| |   | || |__)| |   \\__\\_/|_/|__   /__\\_//__ | \n" + Fore.RESET)


def read_data(filename):
	file = open(filename,"r")

	fline = file.readline().split(" ")
	simulation = int(fline[0])
	intersections = int(fline[1])
	streets = int(fline[2])
	cars = int(fline[3])

	for i in range(streets):
		dict_array.append(file.readline().split(" "))


	for i in range(cars):
		line = file.readline().split(" ")
		line[len(line) - 1] = line[len(line) - 1][0:-1]
		diadromi.append(line)

	for i in range(cars):
		diadromi[i].pop(0)


	diadromi.sort()

	return simulation


def parse_dictionaries(array):
	dicts1 = []
	for i in range(len(array)):
		dicts1.append({
		"start" : array[i][0],
		"end" : array[i][1],
		"name" : array [i][2],
		"L" : int(array [i][3])
		})


	return dicts1


def find_index(diction,key):
	for x in range(len(diction)):
		if(diction[x]['name'] == key ):
			return x

def drive_safe(destination,time,fileout):
	solution_string = ""
	temp = ""
	inter_count = 0
	for i in range(len(destination)):
		inter_count += len(destination[i])
		for j in range(len(destination[i])):
			index = find_index(dict_array,destination[i][j])
			road = dict_array[index]['name']
			inter  = dict_array[index]['end']
			green_time = dict_array[index]['L']
			time -= green_time
			solution_string += inter + "\n"
			solution_string += "1" + "\n"
			solution_string += road + " " + str(green_time) + "\n"

		if(time >= 0):
			inte = inter_count 
			temp = solution_string

		solution = str(inte) + "\n" + temp


	new = open(fileout,"w")
	new.write(solution)
	new.close()

	print(Fore.GREEN + "\t\t\t       SOLUTION IS STORED IN " + fileout)


file = "b.txt"

code_couple_logo()
time= read_data(file)
dict_array = parse_dictionaries(dict_array)
drive_safe(diadromi,time,"solution_"+file)
