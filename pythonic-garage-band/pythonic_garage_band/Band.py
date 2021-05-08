class Musician:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        wel = f"{self.__class__.__name__} instance. Name = {self.name}"
        return wel
    def get_instrument(self):
        return f"{self.machine}"
    def __str__(self):
        wel = f"My name is {self.name} and I play {self.machine}"
        return wel
    def play_solo(self):
        return f"{self.sound}"
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.machine = "guitar"
        self.sound = "face melting guitar solo"
class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.machine = "drums"
        self.sound = "rattle boom crash"
class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.machine = "bass"
        self.sound = "bom bom buh bom"



class Band:
    def __init__(self, group_name, team_member):
        self.name = group_name
        self.members = team_member
        Band.instances.append(self)
    def play_solos(self):
        newList = []
        for i in self.members:
            newList.append(i.play_solo())
        return newList
    @classmethod
    def to_list(cls):
        return cls.instances