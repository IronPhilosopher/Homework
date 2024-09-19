team1_num = 5
team2_num = 6
print("В команде Мастера кода участников: %s" % team1_num)
print("Итого сегодня в командах участников: %s и %s" % (team1_num, team2_num))

score_2 = 42
team2_time = 18015.2
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team2_time))

score_1 = 40
team1_time = 10717.6
challange_result = ""
if team1_time / score_1 < team2_time / score_2:
    challange_result = "Победа команды Мастера кода"
elif team1_time / score_1 > team2_time / score_2:
    challange_result = "Победа команды Волшебники данных"
else:
    challange_result = "Ничья"
tasks_total = score_1 + score_2
time_avg = round( ( team1_time + team2_time) / tasks_total, 2)
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challange_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')