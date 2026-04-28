import pyfiglet

GREEN = "\033[92m"
WHITE = "\033[0m"

result = pyfiglet.figlet_format("$$$", font="slant")
print(GREEN + result + WHITE)
