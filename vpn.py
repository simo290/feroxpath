import platform
import subprocess
import rich
import shutil
from rich.console import Console 
from rich.style import Style
from rich.prompt import Prompt
system = platform.system()
console = Console()
style = rich.Style()
path = shutil.which("aircrack-ng")
if path:
    sh = style(
        color="green",
        bold=True,
        italic=True
    )
    rm = style(
        color="red",
        bold = True,
        italic = True
    )
    rs = style(
        color="cyan",
        bold = True,
        italic =True
    )
    console.print(f"aircrack-ng is installed at: {path}", style=sh, justify="center")
    if system == "linux":
        try:
            iw = subprocess.run(['iwconfig'], check=True)
            with open("iwconfig.txt", "w") as f:
                f.write(iw.stdout)
                with open("iwconfig.txt", "r") as f :
                    con=f.read()
                    if "Mode:Managed" in con:
                        console.print("Your wireless card is in Managed mode. Please switch to monitor mode ", style=rm, justify="center")
                        res = Prompt.ask("Do you want to switch to monitor mode? (y/n)", style=rs)
                        if res.lower() == "y":
                            subprocess.run(['sudo', 'airmon-ng', 'start', 'wlan0'], check=True)
                            root = Prompt.ask("PLeas Enter your root password to continue:")
                            subprocess.run([root], check=True)
                        elif res.lower() == "n":
                            rs1 = Prompt.ask("you can't use this program without monitor mode. you want exit (y/n): ") 
                            if rs1.lower() == "y":
                                console.print("Exiting the program...", style = rm, justify = center)
                                exit()
                            elif rs1.lower() == "n":
                                 subprocess.run(['sudo', 'airmon-ng', 'star', 'wlan0'], check=True)
                                 root = Prompt.ask("PLeas Enter your root password to continue:")
                                 subprocess.run([root], check=True)
                            else:
                                console.print("Invalid value")
                        else:
                            console.print("Invalid value")
        except subprocess.CalledProcessError as e:
