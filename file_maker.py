try:
  import csv
  import  os
except Exception as e:
  print("Errow While importing pkg")

save_path = '' # Give  your path where  you want to save all bulk files

with open("input_files.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    file_name = row[0]+'.'+'js' # Change extension on your need basis like .py .cs ,html .text. json etc
    complete_name = os.path.join(save_path, file_name)
    print(complete_name)
    file_create = open(complete_name, "w")
    file_create.close()
