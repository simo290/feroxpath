
import platform
import subprocess
import shutil
import os

from rich.console import Console
from rich.style import Style
from rich.prompt import Prompt

system = platform.system()
console = Console()

sh = Style(color="green", bold=True, italic=True)
rm = Style(color="red", bold=True, italic=True)
rs = Style(color="cyan", bold=True, italic=True)

path = shutil.which("aircrack-ng")

if path:
    console.print(
        f"aircrack-ng is installed at: {path}",
        style=sh,
        justify="center"
    )

    if system == "Linux":
        try:
            iw = subprocess.run(
                ['iwconfig'],
                capture_output=True,
                text=True,
                check=True
            )

            with open("iwconfig.txt", "w", encoding="utf-8") as f:
                f.write(iw.stdout)

            con = iw.stdout

            if "Mode:Managed" in con:
                console.print(
                    "Your wireless card is in Managed mode.",
                    style=rm,
                    justify="center"
                )

                res = Prompt.ask(
                    "[cyan bold italic]Do you want to switch to monitor mode?[/]",
                    choices=["y", "n"],    
                )
                if res == "y":
                    console.print(
                        "you can't use this program without root",
                        style = rm,
                        justify = "left"
                    )
                    if os.geteuid() == 0:
                        console.print(" you're root, you can continue.", style = sh, justify = "center")
                        subprocess.run(['airmon-ng', 'start', 'wlan0'])

                    else :
                        console.print("You need to run it as root to continue.", style = rm, justify= "center")
                        subprocess.run(
                            ['sudo', 'airmon-ng', 'start', 'wlan0'],
                            check = True,
                            capture_output = True,
                            text = True
                            )
                        dr = 10
                        try:
                            ai = subprocess.run(
                                ['sudo', 'timeout',f'{dr}s', 'airodump-ng', 'wlan0mon'],
                                capture_output = True,
                                check = False,
                                text = True
                            )
                            console.print("finish")
                            with open("airodump.cap", "w") as a:
                                a.write(ai.returncode)
                        except KeyboardInterrupt:
                            console.print(
                                "Programme interrputed by user",
                                style = rm
                            )
                elif res.lower() == "n":
                    console.print("Exiting the program.", style=rm)
                    exit()
                else:
                    console.print(
                        "Please select one of the available options", 
                        style = rm
                        )
            else:
                console.print(
                    "Managed mode was not detected.",
                    style=sh
                )

        except FileNotFoundError:
            console.print("iwconfig was not found.")

        except subprocess.CalledProcessError as e:
            console.print(
                f"Command file : {e.cmd}",
                style = rm
            )
            console.print(
                f"Error: {e.stderr}",
                style = rm
            )
            console.print(
                f"Exite code : {e.returncode}",
                style = rm
            )
            console.print(
                f"Output : {e.stdout}",
                style = rm
            )

else:
    console.print(
        "aircrack-ng is not installed or not in PATH.",
        style=rm
    )
