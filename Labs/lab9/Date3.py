from Date import *

#d = Date()
bdaylist = 0
def birthdays(bdaylist):
    bList = []
    d = 0
    for bday in open('birthdays.txt'):
        bd = bday.replace(' ', ', ')
        b1, b2, b3 = bd.split(',')
        d = Date(int(b1), int(b2), int(b3))
        bList.append(d)
        
    return bList
    

if __name__ == "__main__":
    d = []
    monthL = dict()
    for month in month_names:
        monthL[month] = 0
    

    d = birthdays(bdaylist)
    
    #earliest = Date(3000, 1, 1)
    earliest = d[0]
    latest = d[0]
    
    for value in d:
        if value.__lt__(earliest):
            earliest = value
            
        if latest.__lt__(value):
            latest = value
       
        month = str(value).split('/')[1]
        #print(month_names[int(month)])
        monthL[month_names[int(month)]] += 1
    
    #print(monthL)
    #sorted_values = sorted(monthL.values())
    months = []
    for key in monthL.keys():
        months.append([monthL[key], key])
    months.sort(reverse = True)
                   
    print('earliest birthday is', earliest)
    print('latest birthday is', latest)
    print('month with most birthdays is', months[0][1])