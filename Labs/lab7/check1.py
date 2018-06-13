def parse_line(x):
    if x.count('/') >= 2:
        blist = []
        b2 = x.split('/')
        b5 = len(b2)
        #b2, b3, b4 = int(b2), int(b3), int(b4)
        if (b2[-1].isdigit() == True) and b2[-2].isdigit() == True and b2[-3].isdigit() == True: 
            blist.append(b2[-3])
            blist.append(b2[-2])
            blist.append(b2[-1])
            
            count = 0
            while b5 != len(blist):
                
                blist.append(b2[count])
                count += 1    
            print(tuple(blist))
        else:
            print('None')
        
parse_line("Here is some random text, like 5/4=3./12/3/4")
parse_line("Here is some random text, like 5/4=3./12/3/4as")
parse_line("Here is some random text, like 5/4=3./12/412/a/3/4")
parse_line(" Here is some spaces 12/32/4")
parse_line(" Again some spaces\n/12/12/12")