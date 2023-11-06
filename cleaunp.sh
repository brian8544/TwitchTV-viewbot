#!/bin/bash

# Define the path to the Chrome driver executable
driver_path="$(dirname "$(readlink -f "$0")")/chromedriver"

# Get the list of running processes
for pid in $(pgrep chrome); do
  # Check if the process is associated with the Selenium-driven Chrome instances
  ps -p $pid -o cmd= | grep -qi "$driver_path"
  if [ $? -ne 0 ]; then
    # Close the Chrome process
    kill -9 $pid
  fi
done

read -p "Press Enter to exit"
