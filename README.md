# Grade-Generator-Calculator
An interactive Python application that calculates a student's final grade by prompting the user for assignment details.

# Files
grade-generator.py - Python grade calculator
organizer.sh - Bash file organizer
archive/ - Stores archived CSV files (auto-created)
organizer.log - Activity log (auto-created)

# Quick Start
1. Grade Calculator

python3 grade-generator.py

.Enter assignment details interactively
.Calculates weighted grades and GPA
.Generates grades.csv with all data

2. File Organizer

chmod +x organizer.sh
./organizer.sh

.Moves CSV files to archive/ folder
.Adds timestamps to filenames
.Logs all actions to organizer.log

# Example Flow
.Run grade-generator.py → creates grades.csv
.Run organizer.sh → moves grades.csv to archive/grades-20251105-143022.csv
.Check organizer.log for details