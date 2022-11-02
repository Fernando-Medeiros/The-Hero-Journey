LIST_ENEMIES = []

with open('app/database/list_enemies', mode='r', encoding='utf-8') as file:

    for line in file.readlines():

        LIST_ENEMIES.append(line.replace("\n", "").split(':'))