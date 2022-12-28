import csv

with open("pb.csv", "a") as file:
    name = input("Name: ")
    number = input("Number: ")
    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"number": number, "name": name})
