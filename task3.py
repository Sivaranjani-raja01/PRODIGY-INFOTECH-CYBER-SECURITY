# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:50:10 2024

@author: Dell
"""
import re

def assess_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 12:
        score += 2
        feedback.append("Good length (12 or more characters).")
    elif len(password) >= 8:
        score += 1
        feedback.append("Okay length (8-11 characters). Consider making it longer.")
    else:
        feedback.append("Too short (fewer than 8 characters).")

    # Criteria 2: Uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 2
        feedback.append("Good mix of uppercase and lowercase letters.")
    elif re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Has uppercase letters but lacks lowercase letters.")
    elif re.search(r'[a-z]', password):
        score += 1
        feedback.append("Has lowercase letters but lacks uppercase letters.")
    else:
        feedback.append("No uppercase or lowercase letters found.")

    # Criteria 3: Numbers
    if re.search(r'\d', password):
        score += 2
        feedback.append("Contains numbers.")
    else:
        feedback.append("No numbers found. Consider adding some.")

    # Criteria 4: Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
        feedback.append("Contains special characters.")
    else:
        feedback.append("No special characters found. Consider adding some.")

    # Overall assessment
    if score >= 7:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"

    # Combine feedback into a single message
    feedback_message = "\n".join(feedback)

    return strength, feedback_message

# Example usage
password = input("Enter a password to assess: ")
strength, feedback_message = assess_password_strength(password)
print(f"Password Strength: {strength}")
print("Feedback:")
print(feedback_message)

