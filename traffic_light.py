signal = input("Enter signal : [Red , Green, Yellow]: ").upper()

if signal == "RED":
    print ("Stop")
elif signal == "GREEN" :
    print ("Go")
elif signal == "YELLOW" :
    print ("Get Ready")
else :
    print ("Invalid signal")