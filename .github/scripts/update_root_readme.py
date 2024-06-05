#!/usr/bin/env python

# Takes the generated readme files for each feature, adjusts the markdown headings, and updates the root readme with the new content.

import os
import re

# Get the list of subdirs in src
feature_names = [d for d in os.listdir("src")]

print(f"Found {len(feature_names)} features: {', '.join(feature_names)}")

# Read the root readme
with open("README.md", "r") as f:
    root_readme = f.read()

new_content = ""

# Update the root readme with the new content
for feature_name in feature_names:
    # Read the feature readme
    with open(f"src/{feature_name}/README.md", "r") as f:
        feature_readme = f.read()

    # Adjust the markdown headings
    feature_readme = re.sub(r"^#", "###", feature_readme, flags=re.MULTILINE)

    # Remove everything after the --- to the end of the file
    feature_readme = re.sub(r"\n---.*", "", feature_readme, flags=re.DOTALL)

    new_content += f"\n{feature_readme}"

print(f"New readme content to add: {new_content}")

# Replace the old content with the new content
root_readme = re.sub(
    r"<!-- START_FEATURES -->.*<!-- END_FEATURES -->",
    f"<!-- START_FEATURES -->{new_content}<!-- END_FEATURES -->",
    root_readme,
    flags=re.DOTALL,
)

# Write the updated root readme
with open("README.md", "w") as f:
    f.write(root_readme)
