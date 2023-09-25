"""
A simple program to parse an exportify csv file. For use by Unkers Exco.

Authored by Kee Song Yang, September 2023

"""

import csv

while True:
  try:
    filename = input("Enter file name (without file extension): ")
    data = ()
    with open(filename + ".csv") as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            name = row[2]
            artist = row[4]
            if (name == "Track Name" and artist == "Artist Name(s)"):
                continue
            data += ((name, artist),)

    with open("output.txt", "w") as txtfile:
        for name, artist  in data:
            txtfile.write("• " + name + " - " + artist + "\n")
            print("• " + name + " - " + artist)
        break
  except FileNotFoundError:
    print("oi cannot type properly ah, cannot find the file la")
    continue

