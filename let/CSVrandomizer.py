import csv, random
from prettytable import PrettyTable

namesdict = {'A':'Alejandra', 'M':'Miranda', 'V':'Valeria'}
x = PrettyTable()
x.field_names = ['Tareas','Responsable']

with open('tareas.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        NumParticipants = len(row["Participantes"])
        WinnerNum = random.randint(1,NumParticipants)
        WinnerInitial = row['Participantes'][WinnerNum-1:WinnerNum]
        WinnerName = namesdict[WinnerInitial]
        x.add_row([row['Tareas'],WinnerName])

print(x)

