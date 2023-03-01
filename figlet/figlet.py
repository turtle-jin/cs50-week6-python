from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid Usage")
    else:
        font = sys.argv[2]
        if font not in font_list:
            sys.exit("Invalid Usage")
elif len(sys.argv) == 1:
    font = random.choice(font_list)
else:
    sys.exit(" Incorrect number of arguments. Provide either 0 or 2 arguments")

text = input("Input: ")
figlet.setFont(font=font)
print(figlet.renderText(text))
