import random
class Starter():

    #Initiliaze starters
    def __init__(self,name):
        self.name=name
        self.health=15
        self.level=1
        self.experience=0
        if(name=="Charmander"):
            self.attacks=["Scratch"]
        elif(name=="Bulbasaur"):
            self.attacks=["Tackle"]
        elif(name=="Squirtle"):
            self.attacks=["Tackle"]


    #For attack turns
    def attack(self):
        attackPower=(random.randint(1,4)+self.level)
        print(self.name,"used",self.attacks[0]+"!")
        print("It hit for",str(attackPower)+"hp!")
        return attackPower

class randomEnemy():

    #Initialize enemies
    def __init__(self):
        self.level=0
        enemies={1:"Pidgey",2:"Rattata",3:"Weedle",4:"Caterpie"}
        self.health=8
        x=random.randint(1,4)
        self.number=x
        self.name=enemies[x]

    #For attack turns
    def attack(self):
        attackPower=random.randint(1,3)+self.level
        attacks={1:"Peck",2:"Tackle",3:"Poison Sting",4:"String Shot"}
        print(self.name,"used",attacks[self.number]+"!")
        print("It hit for",str(attackPower)+"hp!")
        return attackPower

def battle(starter,enemy):
    while (starter.health>0 and enemy.health>0):
        enemy.health-=starter.attack()
        if(enemy.health<=0):
            starter.experience+=random.randint(10,25)
            return (enemy.name+" fainted.")
        print(starter.name,"has",starter.health,"health")
        print(enemy.name,"has",enemy.health,"health")
        input("Enter to continue")
        starter.health-=enemy.attack()
        if(starter.health<=0):
            print(starter.name+" died.")
            exit()
        print(starter.name,"has",starter.health,"health")
        print(enemy.name,"has",enemy.health,"health")
        input("Enter to continue")
    print("Starter health:",starter.health)
    print("Enemy health:",enemy.health)

def gymBattle(starter):
    print("You challenge Brock...")
    #Create geodude
    geodude=Enemy()
    geodude.level=3
    geodude.name="Geodude"
    battle(starter,geodude)
    #create onix
    onix=Enemy()












def main():
    answer=input("Please pick C for Charmander, B for Bulbasaur or S for Squirtle: ")
    starters={"C":"Charmander","B":"Bulbasaur","S":"Squirtle"}
    start=Starter(starters[answer])
    x=100
    startHealth=15
    while(True):
        menu=input("Press 1 to battle, 2 to heal your pokemon, 3 to see their health/experience or 4 to challenge a gym: ")
        if(menu=="1"):
            wildEnemy=randomEnemy()
            print("A wild",wildEnemy.name,"appeared!")
            print(battle(start,wildEnemy))
            if(start.experience>x):
                start.level+=1
                start.health=startHealth+5
                startHealth+=5
                print(start.name,"leveled up to",str(start.level)+"!")
                start.experience=start.experience-x
                x+=x*.25
        elif(menu=="2"):
            start.health=15
        elif(menu=="3"):
            print("Lvl "+str(start.level),start.name+": "+str(start.health)+"hp",str(start.experience)+"xp")
        elif(menu=="4"):
            gymBattle(start)







if __name__ == '__main__':
    main()
