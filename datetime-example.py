from datetime import datetime

birthday = "1-May-12"
date_format = "%d-%B-%y"

#parses the string raw_date into variable parsed_date
parsed_date = datetime.strptime(birthday, date_format)


#converts variable parsed_date into 
date_str = parsed_date.strftime("%-m/%-d/%Y") # 01/11/17
print(date_str)
