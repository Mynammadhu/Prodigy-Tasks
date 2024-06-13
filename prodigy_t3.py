# -*- coding: utf-8 -*-
"""prodigy-T3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-_48ZbEc9Dgf5VI-Av1Xga6f1HEQYKzs
"""

import re

def assess_password_strength(password):
    # Initialize strength variables
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_character_criteria = re.search(r'[\W_]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_character_criteria])

    # Determine the strength of the password
    if criteria_met == 5:
        strength = 'Very Strong'
    elif criteria_met == 4:
        strength = 'Strong'
    elif criteria_met == 3:
        strength = 'Moderate'
    elif criteria_met == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    # Provide feedback to the user
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_character_criteria:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, $, etc.).")

    return strength, feedback

# Example usage
password = input("Enter a password to assess: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for tip in feedback:
        print(f"- {tip}")