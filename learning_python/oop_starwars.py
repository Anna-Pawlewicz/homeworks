class Lightsaber:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "Lightsaber with {} blade".format(self.color)


class ForceUser:
    force_users = 0

    def __init__(self, inner_peace=0):
        self._inner_peace = inner_peace
        ForceUser.force_users += 1

    def __del__(self):
        ForceUser.force_users -= 1

    def meditate(self):
        self._inner_peace += 1


class Jedi(ForceUser):
    def __init__(self, inner_peace=0, alive=True):
        super().__init__(inner_peace)
        self.__rank = Jedi.check_rank(inner_peace)
        self.alive = alive
        self.lightsaber = None

    def meditate(self):
        self._inner_peace += 2
        self.__rank = Jedi.check_rank(self._inner_peace)

    def get_rank(self):
        return self.__rank

    def build_lightsaber(self, color):
        self.lightsaber = Lightsaber(color)

    @classmethod    #fabryka, produkuje obiekt o konkretnych parametrach
    def master(cls):
        return cls(30)

    @classmethod
    def knight(cls):
        return cls(20)

    @classmethod
    def jedi(cls):
        return cls(10)

    @classmethod
    def padawan(cls):
        return cls(0)

    @staticmethod
    def greeting():
        return "May the Force be with you"

    @staticmethod
    def check_rank(inner_peace):
        if inner_peace < 0:
            return
        if inner_peace < 10:
            return "Jedi Padawan"
        elif inner_peace < 20:
            return "Jedi"
        elif inner_peace < 30:
            return "Jedi Knight"
        else:
            return "Jedi Master"


kenobi = Jedi(20)
#print(kenobi.__inner_peace)    # nie zadziała bo atrybut jest prywatny
print(Jedi.greeting())
#print(10, Jedi.check_rank(10))
print(kenobi.get_rank)
kenobi.meditate()
print(kenobi.get_rank())

yoda = Jedi.master()
print(yoda.get_rank())

anakin = Jedi.padawan()
print(anakin.get_rank())

quigon = Jedi(100, alive=False)
print(isinstance(yoda, Jedi))
print(isinstance(yoda, ForceUser))

leia = ForceUser()
print(isinstance(leia, Jedi))
print(isinstance(leia, ForceUser))
print(leia._inner_peace)
leia.meditate()
print(leia._inner_peace)

print(kenobi.lightsaber)
kenobi.build_lightsaber("blue")
print(kenobi.lightsaber)

print(ForceUser.force_users)
del leia
print(ForceUser.force_users)
