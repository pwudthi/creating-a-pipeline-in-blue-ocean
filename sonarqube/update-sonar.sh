#!/bin/bash

# Set the path to your sonar-project.properties file
properties_file="sonar-project.properties"

# Set the path to a file containing the new value for sonar.exclusions
new_value_file="new_value_file.txt"

# Read the new value from the file
new_value=$(cat "$new_value_file")

# Use sed to replace the existing sonar.exclusions line with the new value
sed -i "/^sonar\.exclusions=/c sonar.exclusions=$new_value" "$properties_file"
