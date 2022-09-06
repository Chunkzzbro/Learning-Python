final = ""
random = ""
word = ""
while random != "\end":
    random = input("Say something : ")
    if random == "\end":
        break
    end = ""
    temp = random + " "
    interrogatives = ("how","when","why")
    if temp.startswith(interrogatives):
        end = "?"
    else:
        end = "."
        



          
    final = final + random[0].upper() +random[1:] + end + " "

print (final)


    

