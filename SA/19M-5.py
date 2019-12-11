icearea = 1000000
openarea = 1000000
year = 2019
while icearea>=10000:
    total = icearea+openarea
    avealbedo = (icearea*0.6+openarea*0.1)/(icearea+openarea)
    decrease = 0.3/avealbedo**2
    icearea = icearea*(1-0.01*decrease)
    openarea= total-icearea
    year+=2
print(year)






