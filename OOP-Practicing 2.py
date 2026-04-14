class weapons:
    def __init__(self, name="", damage=0):
        self.__name = name
        self.__damage = damage
        
        #sets
    def set_name(self, name):
        self.__name = name
    
    def set_damage(self, damage):
        self.__damage = damage
    
    def get_name(self):
        return self.__name
    
    def get_damage(self):
        return self.__damage

def main():
    weapons = []

    sword = weapons("Sword", 25)
    axe = weapons("Axe", 25)
    bow = weapons("Bow", 15)

    weapons.append(sword)
    weapons.append(axe)
    weapons.append(bow)

    # //: d i s p l a y :\\ #

    for weapon in weapons:
        print("Weapon", weapon.get_name()) 
        print("Damage", weapon.get_damage())

main()
    