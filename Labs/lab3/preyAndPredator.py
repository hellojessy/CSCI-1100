def bunnyPopNext(bPop,fPop):
    bPopNext = (10*bPop)/(1+0.1*bPop)- 0.05*bPop*fPop
    return bPopNext

def foxPopNext(fPop,bPop):
    fPopNext = 0.4 * fPop + 0.02 * fPop * bPop
    return fPopNext


bPop = int(input('Number of bunnies ==> '))
print (bPop)
fPop   = int(input('Number of foxes ==> '))
print (fPop)


print ('Year 1:', bPop, fPop)
bPop1= int(bunnyPopNext(bPop,fPop))
fPop1 = int(foxPopNext(fPop, bPop))

print ('Year 2:',bPop1 , fPop1 )
bPop2= int(bunnyPopNext(bPop1,fPop1))
fPop2 = int(foxPopNext(fPop1, bPop1))

print ('Year 3:', bPop2, fPop2)

bPop3 = bunnyPopNext(bPop2,fPop2)
fPop3= foxPopNext(fPop2,bPop2)

print ('Year 4:', bPop3, fPop3)
bPop4 = bunnyPopNext(bPop3,fPop3)
fPop4= foxPopNext(fPop3,bPop3)

print ('Year 5:', bPop4, fPop4)
bPop5 = bunnyPopNext(bPop4,fPop4)
fPop5= foxPopNext(fPop4,bPop4)