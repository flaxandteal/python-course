#!/usr/bin/env python3

import os
import inflect

pluralizer = inflect.engine()

# Loop through files
for filename in os.listdir():
    # Skip irrelevant files
    if not filename.endswith('txt'):
        continue

    # Divide into important parts and find category name
    institution_type, institution = filename.split('_')
    category = pluralizer.plural(institution_type)

    if not os.path.exists(category):
        os.mkdir(category)

    final_location = os.path.join(category, institution)
    os.rename(filename, final_location)
