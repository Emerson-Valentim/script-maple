import buff
import matard
import matare
import pet

rotacao = 10
run = 0
direita = 0
pet1 = 0
fome = 15

while run < rotacao:

    while direita < 2:
        matard.matar()
        direita +=1
        run += 1
        if run == rotacao:
            buff.buff()
            run = 0
    if pet1 == fome:
        pet.pet()
        pet1 = 0
    while direita >= 0:
        matare.matar()
        direita -= 1
        pet1 += 1



