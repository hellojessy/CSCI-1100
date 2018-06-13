months = [(7, 72.7), (8, 70.0), (9, 64.4), (10, 55.4), (11, 38.6), (12, 32.8)]
sumUp = 0
for month in months:
    sumUp += month[1]
print('sum: {}/avg: {:.1f}'.format(sumUp, sumUp/6))

sumPair = (months[0][1] + months[1][1] + months[2][1]) + (months[3][1] + months[4][1] + months[5][1])
print('sum: {}/avg: {:.1f}'.format(sumPair, sumPair/6))