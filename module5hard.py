import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return f'{self.nickname}'
class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = str(title)
        self.duration = duration
        self.watchtime = 0
        self.adult_mode = adult_mode
    def __str__(self):
        return f'{self.title}'
class UrTube:
    def __init__(self, users = (), videos = (), current_user = None):
        self.users = list(users)
        self.videos = list(videos)
        self.current_user = current_user
    def log_in(self, nickname, password):
        find = False
        ID = 0
        for i in range (len(self.users)):
            if nickname == self.users[i].nickname:
                find = True
                ID = i
                break
        if not find:
            print('Такого пользователя не существует')
        elif hash(password) == self.users[ID].password:
            self.current_user = self.users[ID]
            print(f'Вы вошли в аккаунт {self.users[ID].nickname}')
        else:
            print('Неверный пароль')

    def register(self, nickname, password, age):
        find = False
        for i in range (len(self.users)):
            if nickname == self.users[i].nickname:
                find = True
                break
        if find:
            print(f'Пользователь {nickname} уже существует')
        else:
            us = User(nickname, password, age)
            self.users.append(us)
            self.current_user = us
    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for i in videos:
            find = False
            for j in range (len(self.videos)):
                if i.title == self.videos[j].title:
                    find = True
                    break
            if not find:
                self.videos.append(i)

    def get_videos(self, title):
        result = []
        for i in self.videos:
            if title.lower() in i.title.lower():
                result.append(i.title)
        if len(result) > 0:
            print(result)
# Здесь у меня после поиска почему то выводится None, можете объяснить, почему?

    def watch_video(self, title):
        find = False
        ID = 0
        for i in range (len(self.videos)):
            if title == self.videos[i].title:
                find = True
                ID = i
                break

        if find:
            if self.current_user is not None:
                if self.videos[ID].adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                else:
                    while self.videos[ID].watchtime + 1 < self.videos[ID].duration:
                        time.sleep(1)
                        self.videos[ID].watchtime += 1
                        print(self.videos[ID].watchtime, end = ' ')
                    print('Конец видео')
            else:
                print('Войдите в аккаунт, чтобы смотреть видео')
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')