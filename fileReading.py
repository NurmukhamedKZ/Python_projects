import json
import csv

file_path = "stuff/text1.csv"

try:
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for i in reader:
            print(i)
        
        
except FileNotFoundError:
    print(f"'{file_path}' wasn't found")
    
except PermissionError:
    print(f"you don't have permission to read this file")
    
    
# with open(file_path, "r") as f:
#     content = json.load(f)
#     for i,j in content.items():
#         print(f"{i}: {j}")