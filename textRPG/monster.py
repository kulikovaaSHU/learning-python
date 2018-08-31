class Monster:
    def __init__(self, name, mtype, health, attack1_1, attack1_2, attack1_des, attack2_1, attack2_2, attack2_des, attack3_1, attack3_2, attack3_des):
        self.name = name,
        self.type = mtype,
        self.health = health,
        self.attack1_1 = attack1_1,
        self.attack1_2 = attack1_2,
        self.attack1_des = attack1_des,
        self.attack2_1 = attack2_1,
        self.attack2_2 = attack2_2,
        self.attack2_des = attack2_des,
        self.attack3_1 = attack3_1,
        self.attack3_2 = attack3_2,
        self.attack3_des = attack3_des

    def attack_range(self, attack_num):
            if attack_num == 1:
                result = [self.attack1_1, self.attack1_2]
                return result
            elif attack_num == 2:
                result = [self.attack2_1, self.attack2_2]
                return result
            elif attack_num == 3:
                result = [self.attack3_1, self.attack3_2]
                return result
