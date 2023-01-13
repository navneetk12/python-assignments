
#In the loop, write the name of each vegetable and the color into a CSV called vegetables.csv
#The CSV should look like this:
#Bonus: add the length of the name of the vegtable as separate column

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#Loops through each vegetable
#for veg in vegetables:
   # print(veg)

#writes csvs to a file
import csv

with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)

    #write header row 
    writer.writerow(["item_name", "item_color"])

    #Loops through each vegetable
    for item in vegetables:
        writer.writerow([item['name'], item['color']])
        
        

  

