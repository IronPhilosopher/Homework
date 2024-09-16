import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname

    def __eq__(self, other):
        if other == None:
            return False
        if type(other) == str:
            return self.nickname == other
        if isinstance(other, int):
            return self.password == other

    def __ne__(self, other):
        if other == None:
            return True
        if isinstance(other, str):
            return self.nickname != other
        if type(other) is int:
            return self.password != other

   # def __contains__(self, item):
   #     return item == self.nickname


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title

    def __ne__(self, other):
        if isinstance(other, str):
            return other != self.title

    def __eq__(self, other):
        if isinstance(other, str):
            return other == self.title

class UrTube:
    def __init__(self):
        self.current_user = None

    users = []
    videos = []

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users.append( User(nickname, password, age) )
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and i.password == hash(password):
                self.current_user = i
        if nickname not in self.users:
            print('Пользователь остутствует, пройдите регистрацию.')

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for i in videos:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, sword):
        result = []
        for i in self.videos:
            if sword.casefold() in i.title.casefold():
                result.append(i)
        return result

    def watch_video(self, video):
        if self.current_user != None:
            for n in self.videos:
                if n == video:
                    if n.adult_mode == False or self.current_user.age >= 18:
                        #Условие проверяет, поставлено ли ограничение по возрасту и есть ли пользователю 18. Если ограничения нет или пользователь совершеннолетний, то видео проигрывается. Если ограничение есть, а пользователю нет 18, то срабатывает else и видео не проигрывается.
                        for i in range(n.duration):
                            time.sleep(1)
                            n.time_now += 1
                            print(n.time_now)
                        n.time_now = 0
                        print("Конец видео")
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")

        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


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
