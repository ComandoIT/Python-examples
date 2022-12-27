#How to calculate what day today in format day with library datatime
from datetime import datetime, timedelta

#Obtain date today
today = datetime.datetime.now()

# Rest a day today
yesterday = today - timedelta(days=1)

# Print values 
print("Today is", today.strftime("%d/%m/%Y"))
print("Yesterday was", yesterday.strftime("%d/%m/%Y"))


#Output

#Today is 27/12/2022
#Yesterday was 26/12/2022
