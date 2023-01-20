"""

Streaming Process - port 9999

We'll use the hotel reservation data from Kaggle.

We do not need to reserve the order of the rows.

Important! We'll stream forever - or until we 
           read the end of the file. 
           Use use Ctrl-C to stop.
           (Hit Control key and c key at the same time.)

Explore more at 
https://wiki.python.org/moin/UdpCommunication

"""

import csv
import socket
import time

host = "localhost"
port = 9999
address_tuple = (host, port)

# use an enumerated type to set the address family to (IPV4) for internet
socket_family = socket.AF_INET 

# use an enumerated type to set the socket type to UDP (datagram)
socket_type = socket.SOCK_DGRAM 

# use the socket constructor to create a socket object we'll call sock
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# read from a file to get some fake data
input_file = open("Hotel Reservations.csv", "r")

# create a file to write to
output_file = open("out9.txt", "w", newline='')


# use the built0in sorted() function to get them in chronological order - NOT necessary
# reversed = sorted(input_file)

# create a csv reader for our comma delimited data
reader = csv.reader(input_file, delimiter=",")

for row in reader:
    # read a row from the file
    ID, Adults, Children, Weekend_Nights, Week_Nights, Meal_Plan, Parking, Room_Type, Lead_Time, Year, Month, Day, Market, Repeat_Guest, Prevous_Canceled, Previous_Not_Canceled, Avg_Price_Per_Room, Special_Requests, Booking_Status = row

    # use an fstring to create a message from our data
    # notice the f before the opening quote for our string?
    fstring_message = f"{ID}, {Adults}, {Children}, {Weekend_Nights}, {Week_Nights}, {Room_Type}"
    
    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()

    # use the socket sendto() method to send the message
    sock.sendto(MESSAGE, address_tuple)
    text = (f"Sent: {MESSAGE} on port {port}.")
    print(text)

    # decode from binary
    normal_text = MESSAGE.decode()
        
    # use the csv writer to write the message in the output_file
    csvwriter = csv.writer(output_file) 
    csvwriter.writerow([text]) 

    # sleep for a few seconds
    time.sleep(1)