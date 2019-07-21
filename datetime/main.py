from datetime import datetime
from pytz import timezone
import pytz

#get current time
current_time = datetime.now()

print("Current Time is : ", current_time.time())


#get current date
current_date = datetime.now()

print("Current Date is : ", current_date.date())


#get current hour
current_time = datetime.now()

print("Current Hour is : ", current_time.hour)


#get current minute
current_time = datetime.now()

print("Current Minute is: ", current_time.minute)


#get current second
current_time = datetime.now()

print("Current Second is: ", current_time.second)


#convert string to datetime object
time_in_string = "08-05-2019 11:52:40"
time_in_datetime = datetime.strptime(time_in_string, "%d-%m-%Y %H:%M:%S")

print("-------------------------------------------------")
print("Time in DateTime Format: ", time_in_datetime)
print("-------------------------------------------------")
print("Day in DateTime Format:", time_in_datetime.day)
print("-------------------------------------------------")


#Displaying TimeZone
Time_format = "%Y-%m-%d %H:%M:%S %Z%z"

#get the current time in UTC
now_utc_time = datetime.now(timezone('UTC'))
print('UTC is : ', now_utc_time)
print("-------------------------------------------------")



Time_format = "%Y-%m-%d %H:%M:%S %Z%z"

#get current time in UTC
now_utc_time = datetime.now(timezone('UTC'))
print('UTC:', now_utc_time)

#convert to EST
now_berlin_time = now_utc_time.astimezone(timezone('Europe/Berlin'))
print('Berlin :', now_berlin_time)

now_est_time = now_utc_time.astimezone(timezone('US/Eastern'))
print('EST :', now_est_time)

now_berlin_time = now_utc_time.astimezone(timezone('Europe/Berlin'))
print('Berlin :', now_berlin_time)

now_kolkata_time = now_utc_time.astimezone(timezone('Asia/Kolkata'))
print('Kolkata :', now_kolkata_time)






