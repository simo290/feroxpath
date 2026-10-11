import aircrack-ng
import platform
import subprocess
import rich
import shutil
from rich.console import Console 
from rich.style importStyle
from rich.prompt import Prompt
from aircrack-ng import airmon-ng
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
    console.print(f"aircrack-ng is installed at: {path}", style=sh, justify="center")
    if system == "linux":
        try:
            subprocess.run(['iwconfig'], check=True)
