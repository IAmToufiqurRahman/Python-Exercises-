# Python program that determines wheather an applicant is eligible for loan
# Conditions : not a student, have a full time job, age should be 22 to 32

student = input("Are u a student?")
job_status = input("Do u have a full-time job?")
age = int(input("How old are u?"))

if student.lower() == "no" and job_status.lower() == "yes" and (age >= 22 and age <= 32):
    print("Eligible for loan")
else:
    print("Not eligible")

# for else loop
successful = False
for n in range(1, 4):
    print("Attempt", n, n * ".")
    if successful:
        break
else:
    print("Attemped ", n, "times but failed")

count = 0
for n in range(1, 10):
    if n % 2 == 0:
        print(n)
        count += 1
print(f"we have {count} even numbers")
