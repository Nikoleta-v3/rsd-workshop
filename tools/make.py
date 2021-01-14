import glob
import subprocess
import shutil
import shlex
import logging
import sys
logging.basicConfig(level=logging.INFO)

import os

ipynbs = glob.glob("*ipynb")
if len(ipynbs) < 1:
    logging.warning("No notebooks found.")
    sys.exit(1)
else:
    logging.info("Found %d notebooks.", len(ipynbs))


for ipynb in ipynbs:
    logging.info("Processing %s.", ipynb)
    # Get pure filename, no parend dirs.
    pdf = os.path.basename(ipynb)
    # Strip extension
    pdf = ".".join(pdf.split(".")[:-1])
    
    # Append pdf extension
    pdf += ".pdf"

    # Prepend directory for output.
    pdf = os.path.join("Material in pdf", pdf)

    logging.info("\tWill save generated pdf to %s.", pdf)
    
    # Setup the pandoc command.
    command = 'pandoc -t pdf -f ipynb -o "{}" "{}"'.format(pdf, ipynb)
    logging.info("Assembled pandoc command: %s.", command)
    
    # Split into tokens.
    cmd_list = shlex.split(command)

    # Run as subprocess, use pipe to gather stdin,stderr.
    with subprocess.Popen(
            cmd_list,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
            ) as proc:
        logging.info(proc.stdout.read())

logging.info("All done.")
