# variables
total_students = 1000
course_rating = 4.5
is_published = True

print(total_students)
print(course_rating)
print(is_published)

# String and slicing
course_name = "Python Programming: Code with Mosh"

print(course_name)
print(len(course_name))
# reverse a String using slicing
print(course_name[::-1])

# detect if a word is palindrome
word = "madam"
if (word == word[::-1]):
    print("Palindrome")
else:
    print("Not a palindrome")

# Escape Sequences /" /' // and /n
print("I'm a student learing \"pyhton\" \n programming language")

# Formatted String
first_name = "Toufiqur"
last_name = "Rahman"
print(f"My full name is {first_name} {last_name}")

# String Methods
course = "  python programming "
print(course.upper())
print(course.strip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("lol" not in course)
