import glob
import subprocess
import os

ipynbs = glob.glob("*ipynb")


for ipynb in ipynbs:
    tex = ipynb[:-6] + ".tex"
    subprocess.call(["jupyter-nbconvert", "--to", "latex", ipynb])
    subprocess.call(["latexmk", "--xelatex", tex])
    subprocess.call(["latexmk", "-c"])

subprocess.call("mv *.tex Material\ in\ pdf/", shell=True)
subprocess.call("mv *.pdf Material\ in\ pdf/", shell=True)

extensions = ["xdv", "out", "fls", "fdb_latexmk", "aux", "log"]
for extension in extensions:
    subprocess.call(f"rm *{extension}", shell=True)