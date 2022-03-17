## BC Pham
## 3/16/22
## Hackbright homework

# 1) Correct what is repeated from the report
# 2) Add comments to show your understanding

#This section opens a text file for Day 1
print("Day 1")
the_file = open("um-deliveries-day-1.txt")

#This loop will iterate thru each line and modify...
for line in the_file:
    line = line.rstrip()    #... removing the white space on the right side
    words = line.split('|') #... splitting by looking for the "|" as a delimiter

    melon = words[0]        #assign melon as the index 0 of list called words
    count = words[1]        #assign count as the index 1 of list called words
    amount = words[2]       #assign count as the index 2 of list called words

    #The output will print a line that is string to tell the user selected information
    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()

#This section opens a test file for Day 2
print("Day 2")
the_file = open("um-deliveries-day-2.txt")

#This loop will iterate thru each line and modify...
for line in the_file:
    line = line.rstrip()    #... removing the white space on the right side
    words = line.split('|') #... splitting by looking for the "|" as a delimiter

    melon = words[0]        #assign melon as the index 0 of list called words
    count = words[1]        #assign count as the index 1 of list called words
    amount = words[2]       #assign count as the index 2 of list called words

    #The output will print a line that is string to tell the user selected information
    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()

#This section opens a test file for Day3
print("Day 3")
the_file = open("um-deliveries-day-3.txt")

#This loop will iterate thru each line and modify...
for line in the_file:
    line = line.rstrip()    #... removing the white space on the right side
    words = line.split('|') #... splitting by looking for the "|" as a delimiter

    melon = words[0]        #assign melon as the index 0 of list called words
    count = words[1]        #assign count as the index 1 of list called words
    amount = words[2]       #assign count as the index 2 of list called words

    #The output will print a line that is string to tell the user selected information
    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
