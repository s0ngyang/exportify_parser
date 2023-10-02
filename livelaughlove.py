"""
A simple program to parse an exportify csv file.

Authored by Kee Song Yang, September 2023

"""

import csv

while True:
    try:
        filename = input(
            "Note: File must be in the same folder as the program\nEnter file name (without file extension): ")
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
        print("oi cannot type properly ah, cannot find the file la")
        continue
