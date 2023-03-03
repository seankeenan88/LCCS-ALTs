count1 = int(input("How many earthworms in quadrat 1: "))
count2 = int(input("How many earthworms in quadrat 2: "))
count3 = int(input("How many earthworms in quadrat 3: "))
count4 = int(input("How many earthworms in quadrat 4: "))
count5 = int(input("How many earthworms in quadrat 5: "))

FullCount = (count1 + count2 + count3 + count4 + count5)
average = (FullCount / 5 )

area = (int(input("How many acres of land is this in metres²?: ")))

total = int(area * average)
print ("There is approximately", total ,"earthworms in this field")         
