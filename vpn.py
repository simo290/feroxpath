
import platform
import subprocess
import shutil

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
                ["iwconfig"],
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
                    "Do you want to switch to monitor mode? (y/n)",
                    choices=["y", "n"],
                    style=rs
                )

                if res == "y":
                    console.print(
                        "Use the correct wireless interface and "
                        "authorize any system changes through sudo."
                    )
                else:
                    console.print("Exiting the program.", style=rm)

            else:
                console.print(
                    "Managed mode was not detected.",
                    style=sh
                )

        except FileNotFoundError:
            console.print("iwconfig was not found.")

        except subprocess.CalledProcessError:
            console.print("Could not run iwconfig. Try again.")

else:
    console.print(
        "aircrack-ng is not installed or not in PATH.",
        style=rm
    )
