import os
from datetime import datetime

with open("mm.txt", 'w') as file:
    file.write("! Microsoft Minus\n")
    file.write("! uBlock filter list\n")
    file.write("! Updated: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
    for i in sorted(os.listdir("generate")):
        with open(f'generate/{i}', 'r') as output:
            file.write(output.read())
            file.write("\n")