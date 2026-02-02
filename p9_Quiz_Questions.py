python_interview = {
    "1. Python kya hai?": "High-level language",
    "2. Python interpreted hai?": "Yes",
    "3. Python dynamically typed hai?": "Yes",
    "4. Mutable objects ka example?": "List",
    "5. Immutable objects ka example?": "Tuple",
    "6. List vs Tuple?": "Mutability",
    "7. == vs is?": "Value vs reference",
    "8. Shallow copy kya hai?": "Reference copy",
    "9. Deep copy kya hai?": "Independent copy",
    "10. Function kya hota hai?": "Reusable block",

    "11. Lambda function kya hai?": "Anonymous function",
    "12. *args ka use?": "Multiple arguments",
    "13. **kwargs ka use?": "Keyword arguments",
    "14. Global keyword ka use?": "Global variable",
    "15. Recursion kya hai?": "Self calling",

    "16. Exception kya hota hai?": "Runtime error",
    "17. try-except ka use?": "Error handling",
    "18. finally block?": "Always executes",
    "19. File modes?": "r w a",
    "20. with statement?": "Auto close",

    "21. OOP kya hai?": "Programming paradigm",
    "22. Class kya hoti hai?": "Blueprint",
    "23. Object kya hota hai?": "Instance",
    "24. Constructor?": "Initializer",
    "25. Inheritance?": "Code reuse",

    "26. Polymorphism?": "Multiple behavior",
    "27. Encapsulation?": "Data hiding",
    "28. Abstraction?": "Implementation hiding",
    "29. Method overloading?": "Same name",
    "30. Method overriding?": "Runtime binding",

    "31. Module kya hota hai?": "Python file",
    "32. Package kya hota hai?": "Module collection",
    "33. Virtual environment?": "Isolated setup",
    "34. PIP kya hai?": "Package manager",
    "35. Generator?": "Yield function",

    "36. Iterator?": "Sequential access",
    "37. List comprehension?": "Compact syntax",
    "38. Decorator?": "Function modifier",
    "39. GIL kya hai?": "Thread lock",
    "40. Python fast hai?": "No"
}
correct_score = wrong_score = 0

for r in python_interview:
    print(f"{r}")
    user = input("Answer :")
    print()
    if user == python_interview.get(r):
        print("Correct answer\n")
        correct_score+=1
    else:
        print("Wrong answer\n")
        wrong_score-=1
    continue
score = correct_score - wrong_score
print(f"Correct score : {correct_score}")
print(f"wrong score : {wrong_score}")
print(f"Total score : {score}\n")
