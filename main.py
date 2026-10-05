import rich 
import pyfiglet
import requests
from rich.console import Console
from rich.prompt import Prompt
from pyfiglet import figlet_format
from rich.style import Style 
from pathlib import Path

console = Console()
f = figlet_format
ask = Prompt.ask
banner = f("feroxpath", font="ogre", justify="center")
my = Style(
    color="green",
    bold=True,
    italic=True,
    dim=True
)
console.print(banner, style=my)
pro = Style(
    color="magenta",
    bold=False,
    italic=True
)
console.print("programmed by 'vegevara'", style=pro, justify="left")
tar = Style(
    color="cyan",
    italic=True
)
console.print("Enter the target URL :", style=tar, justify="left")
target = ask("", default="https://exemple.com", show_default=True)
response = requests.get(target)
while True:
    if response.status_code == 200:
        w = Style(
            color="cyan",
            italic=True
        )
        while True:
            console.print("Enter the wordlist path :", style=w, justify="left")
            wordlist = ask("", default="wordlist.txt", show_default=True)
            if wordlist is not None and Path.exists(Path(wordlist)) and Path.is_file(Path(wordlist)):
                with open(wordlist, "r") as f:
                    for line in f:
                        url = target + "/" + line.strip()
                        r = requests.get(url)
                        if r.status_code == 200:
                            u2 = Style(
                                color="green",
                                bold=True,
                                italic=True
                            )
                            console.print(f"{url} [+] found {r.status_code}" , style=u2, justify="center")
                            with open("/home/demo/Bureau/found", "w")as fil:
                                fil.write(f"{url}: {r.status_code}" )
                        else:
                            uo = Style(
                                color="red",
                                bold=True,
                                italic=True
                            )
                            console.print(f"{url} [-] not found {r.status_code}", style=uo,justify="center")
                            with open("/home/demo/Bureau/not_found", "w") as file:
                                file.write(f"{url} : {r.status_code}")
                break
            break
    else:
        za = Style(
            color = "red",
            bolod = False,
            italic = True
        )
        console.print("entre a valid Url  :", style=za, justify="left")
        
