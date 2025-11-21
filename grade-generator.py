#!/usr/bin/env python3

"""Grade Calculator"""

import csv

def main():
    assignments = []
    
    print("=== Grade Calculator ===")
    
    while True:
        # Get assignment details
        name = input("\nAssignment name: ").strip()
        
        category = input("Category (FA/SA): ").upper()
        while category not in ['FA', 'SA']:
            print("Must be FA or SA")
            category = input("Category (FA/SA): ").upper()
        
        grade = float(input("Grade (0-100): "))
        while grade < 0 or grade > 100:
            print("Grade must be 0-100")
            grade = float(input("Grade (0-100): "))
        
        weight = float(input("Weight: "))
        while weight <= 0:
            print("Weight must be positive")
            weight = float(input("Weight: "))
        
        # Store assignment
        assignments.append({
            'name': name,
            'category': category,
            'grade': grade,
            'weight': weight
        })
        
        # Continue?
        if input("\nAdd another? (y/n): ").lower() != 'y':
            break
    
    # Calculate totals
    fa_total = sa_total = 0
    
    print("\n=== RESULTS ===")
    for a in assignments:
        weighted = (a['grade'] / 100) * a['weight']
        print(f"{a['name']}: {weighted:.1f} points")
        
        if a['category'] == 'FA':
            fa_total += weighted
        else:
            sa_total += weighted
    
    final_grade = fa_total + sa_total
    gpa = (final_grade / 100) * 5.0
    
    print(f"\Formative: {fa_total:.1f}")
    print(f"Summative: {sa_total:.1f}")
    print(f"Final Grade: {final_grade:.1f}/100")
    print(f"GPA: {gpa:.1f}/5.0")
    
    # Save to CSV
    with open('grades.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Assignment', 'Category', 'Grade', 'Weight'])
        for a in assignments:
            writer.writerow([a['name'], a['category'], a['grade'], a['weight']])
    
    print("\nSaved to grades.csv")

if __name__ == "__main__":
    main()