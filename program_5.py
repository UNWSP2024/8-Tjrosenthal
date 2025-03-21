# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.


#Tanner Rosenthal
#3/21/25
#Course Finder

def function():
    courses = {}

    while True:
        course_id = input("Enter course ID or type 'done' to finish: ")
        if course_id.lower() == 'done':
            break
        course_name = input(f"Enter the course name: ")
        courses[course_id] = course_name
    return courses 
courses = function()        

subject = input("What subject are you searching for?")

print(f"Courses in {subject}")
found = False 
for course_id, course_name in courses.items():
    if course_id.startswith(subject):
        print(f"{course_id} {course_name}")
        found = True
        
if found == False:
    print("No courses were found")
        
        
