import datetime as dt
import numpy

day1 = dt.date(1902, 9, 20)

yesterday = dt.date.today() - dt.timedelta(days=1)
yesterdayDate = dt.date(yesterday.year, yesterday.month, yesterday.day)

yesterdaySince = yesterdayDate - day1
intYesterdaySince = numpy.int64(yesterdaySince.days)
hexYesterdaySince = hex(intYesterdaySince)
mdYesterdaySince = hexYesterdaySince[4:] + hexYesterdaySince[2:4]
#print(yesterday)
#print(yesterdayDate)
#print(yesterdaySince)
#print(intYesterdaySince)
#print(hexYesterdaySince)
#print(mdYesterdaySince)

mdSinceHex = '{}c3a82faa'.format(mdYesterdaySince)

with open('C:\\bclogs\\reportDates.txt', 'r') as f:
    for line in f:
        useline = line.split(',')
        rDate = dt.date(int(useline[0]), int(useline[1]), int(useline[2].rstrip('\n')))
        rSince = rDate - day1
        rSinceInt = numpy.int64(rSince.days)
        rSinceHex = hex(rSinceInt)
        rSinceMD = rSinceHex[4:] + rSinceHex[2:4]
        mdHexSince = '{}c3a82faa'.format(rSinceMD)
        #print(rDate)
        #print(rSince)
        #print(rSinceInt)
        #print(rSinceHex)
        #print(rSinceMD)

        with open('C:\\bclogs\\file012.dat', 'rb') as f12:
            f12Binary = f12.read()
            f12Hex = f12Binary.hex()
            new_f12Hex = f12Hex.replace(mdSinceHex, mdHexSince)
            new_f12Binary = bytes.fromhex(new_f12Hex)
            path = 'C:\\bclogs\\dateReportConvert\\file012_NEW\\file012_{}.dat'.format(str(rDate))
            with open(path, 'wb') as new_f:
                new_f.write(new_f12Binary)


#save as file_01242016.dat