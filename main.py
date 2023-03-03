def earthworm():
    print ("checking earthworm count can determine soil health, being impacted by pH, waterlogging, compaction, tillage, rotation and organic matter management.")
    print (" ")
    
    while True:
        try:
            count1 = (int(input("How many earthworms in quadrat 1: ")))         
            count2 = (int(input("How many earthworms in quadrat 2: ")))
            count3 = (int(input("How many earthworms in quadrat 3: ")))
            count4 = (int(input("How many earthworms in quadrat 4: ")))
            count5 = (int(input("How many earthworms in quadrat 5: ")))
            FullCount = (count1 + count2 + count3 + count4 + count5)
            average = (FullCount / 5)
            break
        except ValueError:
            print("Error occurred , Please enter Number")
            pass
        except UnboundLocalError:
            print("Error occurred , Please enter Number")
            pass
        
    print (average , "equals average earthworm count per quadrat")

    area = (float(input("How many acres of land is this in acres?: ")))

    land = (area * 4046.86)

    total = int(land * average)
    print ("There is approximately", total ,"earthworms in this field")

    if average <= 30:
        print ("Reduce cultivation frequency and intensity. Surface dwelling and deep burrowers (which feed on surface organic matter), are sensitive to soilfrom conventional tillage")
    
    elif 30 < average < 49 :
        print ("Soil quality is high and no aeration methods are needed")
    
    elif average > 50:
        ("too high")

earthworm()

ph = float(input("what is the Ph of your soil: "))
if ph<6:
    print ("Soil is very acidic,To make soils less acidic apply a material that contains some form of lime. Lime soil to increase ph")
    
elif 6<ph<7.5:
    print ("Soil if of a good ph , no methods are needed")
    
elif ph>=7.5:
    print ("Soil ph is too high,Soil pH can be reduced most effectively by adding elemental sulfur, aluminum sulfate or sulfuric acid.")



