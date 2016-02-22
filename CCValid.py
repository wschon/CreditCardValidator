ccstr = raw_input('Enter the card number you want to check (xxxx-xxxx-xxxx-xxxx): ')[::-1] #reads in string and reverses
#print(ccstr)
ccstr2 = ccstr.translate(None, "-")
check = 0           #checksum
#print(ccstr2)
for i in range(0, len(ccstr2)):
    #print int(ccstr2[i])
    if i%2 == 1:
        if 2*int(ccstr2[i]) >= 10:
            check += 1
            check += (2*int(ccstr2[i])-10)
        else:
            check += 2*int(ccstr2[i])
    else:
        check += int(ccstr2[i])
    #print check
#print check
if check%10 == 0:
    print "Card number is valid"
else:
    print "Card number is not valid"
