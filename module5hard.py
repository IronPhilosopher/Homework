import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users[nickname] = User(nickname, password, age)
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_in(self, nickname, password):
        if nickname in self.users:
            if self.users[nickname].password == hash(password):
                self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for i in videos:
            if i in self.videos:
                return
        for i in videos:
            self.videos[i.title] = i

    def get_videos(self, sword):
        result = []
        for i in self.videos:
            if sword.casefold() in i.casefold():
                result.append(i)
        return result

    def watch_video(self, video):
        if self.current_user != None:
            if video in self.videos:

                if self.videos[video].adult_mode == False or self.users[self.current_user].age >= 18:
                    for i in range(self.videos[video].duration):
                        time.sleep(1)
                        self.videos[video].time_now += 1
                        print(self.videos[video].time_now)
                    self.videos[video].time_now = 0
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