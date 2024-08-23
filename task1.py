# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:43:10 2024

@author: Dell
"""
import re

def assess_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Additional checks for common weaknesses
    if len(password) > 12:
        score += 1
    if re.search(r'(.)\1\1', password):
        score -= 1
        feedback.append("Password should not contain three consecutive identical characters.")
    
    # Determine the strength
    if score >= 5:
        strength = "Strong"
        feedback.insert(0, "Your password is strong.")
    elif score >= 3:
        strength = "Moderate"
        feedback.insert(0, "Your password is moderate. Consider improving it.")
    else:
        strength = "Weak"
        feedback.insert(0, "Your password is weak. You should change it.")

    return strength, feedback

# Example usage
password = "Pa$$w0rd123!"
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength}")
for comment in feedback:
    print(f"- {comment}")

