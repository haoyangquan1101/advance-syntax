# 面向对象实现"游戏装备"
# 装备类
class Equipment:
    def __init__(self, name, level):
        self.name = name      # 装备名称
        self.level = level    # 装备等级

    def equip(self):
        pass  # 装备的通用方法

# 具体装备类（继承自 Equipment）
class Weapon(Equipment):
    def equip(self):
        print(f"装备 {self.name} (等级{self.level}) → 攻击力+{self.level*10}")

class Armor(Equipment):
    def equip(self):
        print(f"穿上 {self.name} (等级{self.level}) → 防御力+{self.level*8}")

class Artifact(Equipment):
    def equip(self):
        print(f"激活 {self.name} (等级{self.level}) → 全属性+{self.level*5}")

# 创建对象并调用方法
sword = Weapon("火焰剑", 5)
shield = Armor("龙鳞盾", 3)
ring = Artifact("智慧之戒", 7)

sword.equip()
shield.equip()
ring.equip()