"""
Prints out the list of songs given the name of the CSV file.

Found a bug or have any suggestions? Feel free to contribute at github.com/s0ngyang/exportify_parser

Authored by Kee Song Yang, RH Unplugged Vice-Head 2023
"""

import csv

print("Note: File must be in the same folder as the program")

while True:
    try:
        filename = input(
            "Enter file name (without file extension): ")
        data = ()
        with open(filename + ".csv", "r", encoding="utf8") as csvfile:
            file_reader = csv.reader(csvfile)
            for row in file_reader:
                name = row[2]
                artist = row[4]
                if (name == "Track Name" and artist == "Artist Name(s)"):
                    continue
                data += ((name, artist),)

        with open("output.txt", "w", encoding="utf8") as txtfile:
            for name, artist in data:
                txtfile.write("• " + name + " - " + artist + "\n")
                print("• " + name + " - " + artist)
            break
    except FileNotFoundError:
        print("eh type properly la, cannot find the file")
        continue
