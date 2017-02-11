import random
print "Welcome to Gladiators of Teldrin"
print "(S)tart"
print "(C)lose"
response=raw_input()
if response == "s":
    print "You are a gladiator in a massive arena, a participant in a bloody spectacle for millions to see."
    HP = 45
    mana = 5
    EnemyHP = 45
    enemyMana = 5
    print "You are facing your first enemy, also a novice in the art of combat."
    end = 0
    enemydmgMod = 1
    dmgMod = 1
    sdActive = 0
    enemysdActive = 0
    while end==0:
        print "HP= " +str(HP)
        print "Mana= " +str(mana)
        print "Do you:"
        print "(A)ttack"
        print "(B)lock"
        print "(C)ast"
        print "(R)un away"
        action = raw_input()
        if action == "r":
            print "You have run away, forfeiting the match and angering your trainers. Still, the punishment you will recieve will be far less than what you would see in the aferlife"
            end = 1
            enemydamage = 0
            damage = 0
        elif action == "a":
            toHit = random.randint(1,20)
            if sdActive == 1:
                if toHit >= 5:
                    damage = random.randint(2,16) * enemydmgMod
                    print "You hit for " + str(damage) + " HP!"
                    enemydmgMod = 1
                    sdActive = 0
                    saActive = 0
                    waActive = 0
                else:
                    print "Even with the magic in your sword arm, you missed!"
                    damage = 0
            else:
                if toHit >= 10:
                    damage = random.randint(1,8) * enemydmgMod
                    enemydmgMod = 1
                    print "You hit for " + str(damage) + " HP!"
                else:
                    print "You missed!"
                    damage = 0
                    enemydmgMod = 1
        elif action == "b":
            dmgMod = dmgMod * .5
            damage = 0
            print "You are blocking"
        elif action == "c":
            print "Which spell?"
            print "(M)agic Bullet"
            print "(S)word Dance"
            print "(W)eaken Armor"
            print "S(u)nder Weapons"
            spell = raw_input()
            if mana > 0:
                if spell == "m":
                    damage = random.randint(2,5)
                    print "The magical weapon soars through the air and slams into your enemy for " + str(damage) + " HP!"
                    mana = mana-1
                    waActive = 0
                    saActive = 0
                elif spell == "s":
                    sdActive = 1
                    print "You feel the magical energies suffuse your blades and sword arm."
                    mana = mana-1
                    damage = 0
                    saActive = 0
                    waActive = 0
                elif spell == "w":
                    waActive = 1
                    saActive = 0
                    if waActive == 1:
                        enemydmgMod = enemydmgMod * 3
                    damage = 0
                    print "You have weakened your enemy's armor for a round."
                    mana = mana -1
                elif spell == "u":
                    waActive = 0
                    saActive = 1
                    if saActive == 1:
                        dmgMod = dmgMod * .3
                    print "You have sundered your enemy's weapons"
                    damage = 0
            else:
                print "You don't have any mana"
        EnemyHP = EnemyHP - damage
        if EnemyHP <= 0:
            end = 1
            print "The enemy falls to the ground. Your sword point hovers above his throat. You look up at the master of the arena. He hold his thumb down. Everyone cheers as you slide the sword point into his throat."
            print "Would you like to do this fight again?"
            yesno = raw_input()
        elif enemyMana > 0:
            enemyChoice = random.randint (1,3)
            if enemyChoice == 1:
                toHit = random.randint (1,20)
                if enemysdActive == 1:
                    if toHit >= 5:
                        damage = random.randint(2,16) * dmgMod
                        print "He hits you for " + str(damage) + " HP!"
                        dmgMod = 1
                        enemysdActive = 0
                        enemywaActive = 0
                        enemysaActive = 0
                    else:
                        print "Even with the magic in his sword arm, he missed!"
                        damage = 0
                        dmgMod = 1
                else:
                    if toHit >= 10:
                        damage = random.randint(1,8) * dmgMod
                        enemysaActive = 0 
                        enemywaActive = 0
                        print "He hits you for " + str(damage) + " HP!"
                    else:
                        print "He missed!"
                        damage = 0
                        enemysaActive = 0
                        enemywaActive = 0
            elif enemyChoice == 2:
                enemydmgMod = enemydmgMod * .5
                damage = 0
                enemysaActive = 0
                enemywaActive = 0
                print "He blocks!"
            elif enemyChoice == 3:
                spell = random.randint (1,4)
                if spell == 1:
                    damage = random.randint (2,5)
                    enemyMana = enemyMana - 1
                    enemysaActive = 0
                    enemywaActive = 0
                    print "He fires a Magic Bullet and it arcs through the air to hit you, dealing " + str(damage) + " HP in damage"
                elif spell == 2:
                    enemysdActive = 1
                    print "Magic suffuses the enemy's sword and arm."
                    enemysaActive = 0
                    enemywaActive = 0
                    damage = 0
                    enemyMana = enemyMana -1
                elif spell == 3:
                    enemywaActive = 1
                    if enemywaActive == 1:
                        dmgMod = dmgMod * 3
                    print "The opponent weakens your armor"
                    damage = 0
                    enemysaActive = 0
                    enemyMana = enemyMana - 1
                elif spell == 4:
                    enemysaActive = 1
                    enemywaActive = 0
                    if enemysaActive == 1:
                        enemydmgMod = enemydmgMod * .3
                    damage = 0
                    print "Your sword is sundered"
                    enemyMana = enemyMana -1
        else:
            enemyChoice = random.randint (1,2)
            if enemyChoice == 1:
                toHit = random.randint (1,20)
                if enemysdActive == 1:
                    if toHit >= 5:
                        damage = random.randint(2,16) * dmgMod
                        print "He hits you for " + str(damage) + " HP!"
                        enemysdActive = 0
                        enemysaActive = 0
                        enemywaActive = 0
                    else:
                        print "Even with the magic in his sword arm, he missed!"
                        damage = 0
                        enemysdActive = 0
                        enemysaActive = 0
                        enemywaActive = 0
                else:
                    if toHit >= 10:
                        damage = random.randint(1,8) * dmgMod
                        enemysaActive = 0
                        enemywaActive = 0
                        print "He hits you for " + str(damage) + " HP!"
                    else:
                        print "He missed!"
                        damage = 0
                        enemysaActive = 0
                        enemywaActive = 0
            elif enemyChoice == 2:
                enemydmgMod = enemydmgMod * .5
                print "He blocks!"
                enemysaActive = 0
                enemywaActive = 0
                damage = 0
        HP = HP - int(damage)
        if HP<=0:
            
            print "Some are lucky enough to fight in the arena long enough to earn their freedom... Onlookers realize as you bleed out that you are not one."
            end = 1
    print "Goodbye"