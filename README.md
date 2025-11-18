# Grade-Generator-Calculator
An interactive Python application that calculates a student's final grade by prompting the user for assignment details.

# Files
.grade-generator.py - Python grade calculator<br>
.organizer.sh - Bash file organizer<br>
.archive/ - Stores archived CSV files (auto-created)<br>
.organizer.log - Activity log (auto-created)<br>

# Quick Start
# 1. Grade Calculator

python3 grade-generator.py

.Enter assignment details interactively<br>
.Calculates weighted grades and GPA<br>
.Generates grades.csv with all data

# 2. File Organizer

chmod +x organizer.sh<br>
./organizer.sh<br>

.Moves CSV files to archive/ folder<br>
.Adds timestamps to filenames<br>
.Logs all actions to organizer.log<br>

# Example Flow
.Run grade-generator.py → creates grades.csv<br>
.Run organizer.sh → moves grades.csv to archive/grades-20251105-143022.csv<br>
.Check organizer.log for details<br>