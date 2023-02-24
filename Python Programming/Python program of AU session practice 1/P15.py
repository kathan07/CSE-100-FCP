import time
 
current_hour = time.strptime(time.ctime(time.time())).tm_hour
 
if current_hour < 12 :
    print ("Good Morning!")
elif current_hour == 12 :
    print ("Good Noon!")
elif current_hour > 12 and current_hour < 18 :
    print ("Good AfterNoon!")
elif current_hour >= 18 :
    print ("Good Evening!")