
class Character:
    """Classe qui définit un personnage dans un jeu d'aventure"""
    def __init__(self):
        """Constructeur d'un objet de classe personnage"""
        self.hp,self.stats = 100,dict() """en faire des méthodes ?"""
        self.name = self.choose_name()
        self.race = self.choose_race()
        self.gender = self.choose_gender()

    def __str__(self):
        """Méthode qui affiche le nom de l'objet courant"""
        return "Ce personnage s'appelle " + self.name

    def choose_name(self):
        char_name = input("Quel est le nom de votre personnage ? ")
        return char_name

    def choose_race(self):
        """Méthode pour choisir la race du personnage"""
        while True:
            char_race = input("Quel est sa race ? [humain/elfe de la nuit/orc/mort-vivant] : ")
            if char_race == "humain":
                print(self.name,"est un humain.")
                return char_race
            elif char_race == "elfe de la nuit":
                print(self.name,"est un elfe de la nuit.")
                return char_race
            elif char_race == "orc":
                print(self.name,"est un orc.")
                return char_race
            elif char_race == "mort-vivant":
                print(self.name,"est un mort-vivant.")
                return char_race

    def choose_gender(self):
        """Méthode pour choisir le genre du personnage"""
        while True:
            char_gender = input("De quel genre est-il ? [masculin/féminin] :")
            if char_gender == "masculin":
                print(self.name,"est un homme.")
                return char_gender
            elif char_gender == "féminin":
                print(self.name,"est une femme.")
                return char_gender

    def choose_stats(self):
        """Méthode qui demande à l'utilisateur de choisir les caractéristiques de son personnage.
        Il a 300 points à répartir en 6 caractéristiques."""
        liste_stats = ['Force','Dextérité','Constitution','Intelligence','Sagesse','Charisme']
        total = 0
        stats_max = 300
        for stat in liste_stats:
            print("Choisissez une valeur pour votre caractéristique",stat.lower(),": ")
            value = int(input())
            total += value
            while total > stats_max:
                total = total - value
                print("Vous avez dépassé 300. Choisissez une valeur : ")
                value = int(input())
                total = total + value
            self.stats[stat] = value
            print(stat,"→",self.stats[stat])
            print("Points de caractéristiques restants :", stats_max - total,"points.")
        return self.stats[stat]

    def display_stats(self):
        """Méthode pour afficher les caractéristiques du personnage"""
        for stat in self.stats:
                print("-",stat,"→ ",self.stats[stat])

    def display_state(self):
        """Méthode qui affiche l'état du personnage : nom, pv, etc..."""
        if self.hp <50:
            state = self.name + " n'a plus que " + str(self.hp) + " points de vie."
        else:
            state = self.name + " a encore " + str(self.hp) + " points de vie."
        return print(state)

class Warrior(Character):
    """Classe qui définit un personnage de type guerrier"""
    def __init__(self):
        """Constructeur de la classe Guerrier qui ajoute les armes en plus de nom, tribu et genre"""
        super().__init__()
        self.weapons = { 'Arme tranchante' : [Sword(),Dagger(),Axe()],
        'Arme contondante' : [Warhammer(),Club(),Staff()]}


    def display_weapons(self):
        """Méthode qui affiche les armes du guerrier"""
        print("Armes :")
        for genre,liste_weapons in self.weapons.items():
            for weapon in liste_weapons:
                print("-",genre,":")
                print("-",weapon.name,"→ Puissance :",weapon.power)

    """Méthode initialisant l'endurance du guerrier"""                

class Wizard(Character):
    """Classe qui définit un personnage de type magicien"""
    def __init__(self):
        super().__init__()
        self.spells = { 'Magie Noire' : [Agi(),Zio(),Bufu()],
        'Magie Blanche':[Dia(),Media(),Recarm()]}

    def display_spells(self):
        """Méthode qui affiche les sorts du magicien"""
        print("Sorts :")
        for field,liste_spells in self.spells.items():
            for spell in liste_spells:
                print("-",field,":")
                print("-",spell.name,"→ Puissance :",spell.power)

    """Méthode initialisant la mana du magicien"""
   
class Weapons:
    """Méthode qui affiche le nom, la puissance et la vitesse des armes"""
    def __str__(self):
        return self.name

class Sword(Weapons):
    def __init__(self):
        self.name = "Épée"
        self.power = 70
        self.speed = 30
        """self.stamina = 25"""

class Dagger(Weapons):
    def __init__(self):
        self.name = "Poignard"
        self.power = 30
        self.speed = 80
        """self.stamina = 10"""

class Axe(Weapons):
    def __init__(self):
        self.name = "Hache de Combat"
        self.power = 80
        self.speed = 25
        """self.stamina = 30"""


class Warhammer(Weapons):
    def __init__(self):
        self.name = "Marteau de Guerre"
        self.power = 95
        self.speed = 8
        """self.stamina = 50"""

class Club(Weapons):
    def __init__(self):
        self.name = "Massue"
        self.power = 65
        self.speed = 35
        """self.stamina = 15"""

class Staff(Weapons):
    def __init__(self):
        self.name = "Bâton"
        self.power = 25
        self.speed = 66
        """self.stamina = 10"""

class Spells:
    """Méthode qui affiche le nom des sorts"""
    def __str__(self):
        return self.name

class Agi(Spells):
    def __init__(self):
        self.name = "Agi"
        self.power = 45
        """self.mana = 25"""

class Zio(Spells):
    def __init__(self):
        self.name = "Zio"
        self.power = 45
        """self.mana = 25"""

class Bufu(Spells):
    def __init__(self):
        self.name = "Bufu"
        self.power = 45
        """self.mana = 25"""

class Dia(Spells):
    def __init__(self):
        self.name = "Dia"
        self.power = 45
        """self.mana = 35"""

class Media(Spells):
    def __init__(self):
        self.name = "Media"
        self.power = 65
        """self.mana = 45"""

class Recarm(Spells):
    def __init__(self):
        self.name = "Recarm"
        self.power = 95
        """self.mana = 65"""

#char_name = input("Quel est le nom de votre personnage ? ")
#char_race = input("Quel est sa race ? [humain/elfe de la nuit/orc/mort-vivant] : ") #Créer condition entre races
#char_gender = input("De quel genre est-il ? [masculin/féminin] :") #Créer condition entre genres

char = Warrior() #créer un objet de classe Personnage/Guerrier
#char1 = Wizard() #créer un objet de classe Personnage/Magicien
char.choose_stats()
char.display_stats()
char.display_weapons()
#char1.display_spells()

char.display_state()
"""Le personnage se prend un coup"""
print(char.choose_name(),"subit une attaque.")
char.hp = char.hp - 10
char.display_state()