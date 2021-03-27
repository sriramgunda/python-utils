import csv
import os


def clear_csv(csvfile):
    try:
        if os.path.exists(csvfile):
            print("File {} already exists. Removing the file".format(csvfile))
            os.remove(csvfile)
        else:
            print("The file {} does not exist".format(csvfile))
    except PermissionError as pe:
        print("ERROR: unable to remove file {}. {}".format(csvfile, pe))

def read_csv(csvfile):
    data = []
    with open(csvfile, newline='') as rc:
        reader = csv.DictReader(rc)
        for row in reader:
            data.append(dict(row))
    return data
            

def write_csv(csvfile, data=[], columns=[], delimiter=','):
    clear_csv(csvfile)
    try:
        with open(csvfile, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for entity in data:
                writer.writerow(entity)
    except:
        print("[ERROR] unable to write csv.")

