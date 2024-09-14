import time

class User:
    def __init__(self, nickname, password, age):
        if isinstance(nickname, str) and isinstance(age, int):
            self.nickname = nickname
            self.password = hash(password)
            self.age = age
            if not isinstance(self.password, int):
                raise ValueError

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        if isinstance(title, str) and isinstance(duration, int) \
        and isinstance(time_now, int) and isinstance(adult_mode, bool):
            self.title = title
            self.duration = duration
            self.time_now = time_now
            self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        a = True
        for i in self.users:
            if nickname == i.nickname:
                a = False
                break
        if a:
            self.users.append( User(nickname, password, age) )
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname:
                if i.password == hash(password):
                    self.current_user = i

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for i in videos:
            if i in self.videos:
                return
        for i in videos:
            self.videos.append(i)

    def get_videos(self, sword):
        result = []
        for i in self.videos:
            if sword.casefold() in i.title.casefold():
                result.append(i.title)
        return result

    def watch_video(self, video):
        if self.current_user != None:
            for i in self.videos:
                if video == i.title:
                    if i.adult_mode == False \
                    or self.users[ self.users.index(self.current_user) ].age >= 18:
                            for a in range(i.duration):
                                time.sleep(1)
                                i.time_now += 1
                                print(i.time_now)
                            i.time_now = 0
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
print(ur.current_user.nickname)


# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')