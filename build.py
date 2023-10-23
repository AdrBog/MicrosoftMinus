import os
from datetime import datetime

with open("mm.txt", 'w') as file:
    file.write("! Title: Microsoft Minus - uBlock filter list\n")
    file.write("! Last modified: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
    file.write("! Description: List of uBlock filters to debloat Microsoft's websites.\n")
    file.write("! Homepage: https://github.com/AdrBog/MicrosoftMinus\n")
    file.write("! License: https://github.com/AdrBog/MicrosoftMinus/blob/main/LICENSE\n")
    file.write("! Credits: Adrian Bogdan - https://github.com/AdrBog\n")
    for i in sorted(os.listdir("generate")):
        with open(f'generate/{i}', 'r') as output:
            file.write(output.read())
            file.write("\n")