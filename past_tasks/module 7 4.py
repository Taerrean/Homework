team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
print('В команде %s участников: %s!' % (team1, team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
score_2 = 42
team2_time = 18015.2
print('Команда {} решила задач: {}!'.format(team2, score_2))
print('{} решили задачи за {} с!'.format(team2, team2_time))
score_1 = 40
challenge_result = 'Победила дружба!'
team1_time = 1552.512
time_avg = (team1_time/score_1 + team2_time/score_2)/2
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {time_avg} секунды на задачу!')