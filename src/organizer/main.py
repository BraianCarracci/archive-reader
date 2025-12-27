import pathlib
import os
import sys

p = pathlib.Path ('C:/Users/braia/Downloads/instaladores') #find the dir

for item in p.iterdir(): 
    if item.is_file():
        print("pasta:",item.name)

    elif item.is_dir():
        print(f"arquivo: {item.name}")

        for subitem in item.iterdir():
            if subitem.is_file():
                print(f"  arquivo dentro de {item.name}: {subitem.name}")

            if subitem is item.iterdir():
                print(f"  pasta dentro de {item.name}: {subitem.name}")  

