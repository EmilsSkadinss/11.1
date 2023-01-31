#taisīsim karātavas
#vārdi, lists ar burtiem
#dzīvības
#mainīgais spēles statusam
import random
dzivibas=5
vārdi=["ābols", "Banāns", "ķirsis", "ananass", "gurķis","dezoksiribonukleīnskābe"]
while True:
    vārds = random.choice(vārdi)
    uzminētais_vārds =list("_" for _ in vārds) #veids, kā vienā rindā ierakstīt for ciklu, kas izvada sarkastu, kas ir vārda garumā, kas sastāv tikai no apakšsvītrām
    while dzivibas >0 and "".join(uzminētais_vārds) !=vārds:
        ievade=input("ieraksti burtu.")
        if ievade=="":
            continue
        ievade=ievade[0]
        #Gruma pārbaude
        guessed = False
        for i in range(0, len(vārds)):
            if ievade==vārds[i]: #salīdzina i-to vārda burtu ar minēto burtu.
                uzminētais_vārds[i]= ievade
                guessed=True
        if not guessed:
            dzivibas-=1
        print(f"dzivibas: {dzivibas}")
        print(uzminētais_vārds)
    if dzivibas>0:
        print("tu esi uzvarējis")
    else:
        print("go get a job useless yasuo main i hope you die!", "pareizais vārds bija", (vārds)) 
    if input("vai sākt jaunu spēli? y/n").lower()!="y":
        break
