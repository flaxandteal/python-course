# -*- coding: utf-8 -*-
"""Less Antipythonic Example

This is an improved version of the bad_python.py
idea, with the same functionality but should be
much more readable and a bit more Pythonic!

Created on Sat Dec 24 14:20:13 18

@author: The Ghost of Coding Future (E Scrooge)
"""
# pylint: disable-msg=C0103

import logging
import numpy as np

# Indicates whether to output both cos and sin (rounded) [True]
# or just sin [False]
newversion = False

# Set this to None, for STDOUT only, or a filename to send output there
log_filename = None

# We want to set an output log location and be able use stdout - logging is
# well set up for this usage. We set the logger's name in case we ever want
# to import this code into another module
logging.basicConfig(
    format="%(line_number)d:%(message)s",
    filename=log_filename,
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# I would rather not use this approach, but keeping track of the output line
# number is not a common logging module (or print) use
class Outputter:
    """
    This is a class for providing output with additional functionality beyond
    the basic logging library system.
    """
    line_number = 1

    def write(self, line):
        """This wraps the logger, printing incrementing line numbers beside output"""
        # Supply additional fields for logging format as a dict
        logger.info(line, extra={"line_number": self.line_number})
        self.line_number += 1

# Object for managing output - can keep track of its own variables (say we want
# to add more output-specific functionality, this walls it off)
output = Outputter()

# Range of values to output
max_x = 9
x_array = np.arange(1, max_x + 1)

# Most numpy functions can take an array and act on each member
sin_values = np.sin(x_array)

# Start output followed by a line break
# TODO: add a more constructive title
if newversion:
    task = "SIN AND COS"
else:
    task = "SIN"

header = """
PRINTING VALUES OF {task} FOR x IN 1, 2,..., {max_x}
""".format(
    task=task,
    max_x=max_x
)

# Print the header (without initial newline)
output.write(header.lstrip())

if newversion:
    # FIXME: TO BE IMPLEMENTED ASAP - REPLACE THIS ERROR MESSAGE
    raise NotImplementedError("""
        The cos and sin version is still to be implemented
    """)

# NOTE: the output starts with the line number, not x
# (bad idea - only for compatibility)
for sinx in sin_values:
    message = "%.16lf" % sinx
    output.write(message)
