def main():
	print('')
	print('Please enter the following information to create your ID Card.')
	input('Press enter to continue.')
	ask_student_info()
	display_student_info()

def ask_student_info():
	global first_name,Last_name,Email_Adress,Student_ID,FPT_class,Graduation_year,Favorite_subject,Extracurricular
	first_name = input("what is your first name?: ")
	Last_name = input("what is your last name?: ")
	Email_Adress = input("What is your email?: ")
	Student_ID = input("Student ID?: ")
	FPT_class = input("What is your FPT?: ")
	Graduation_year = input("Graduation year?: ")
	Favorite_subject = input("What is your favorite subject?: ")
	Extracurricular = input("Do you have extracurricular activities (yes or no)?")
	
def display_student_info():
	global first_name,Last_name,Email_Adress,Student_ID,FPT_class,Graduation_year,Favorite_subject,Extracurricular
	print(f"\nYour ID Card is: \n{"-" * 40}\n{first_name.capitalize().strip()}, {Last_name.capitalize().strip()}")
	print(f"ID: {Student_ID.strip()}\n\n{Email_Adress.strip()}\n")
	print(F"FPT Class: {FPT_class.strip()}\t\tFavorite Subject: {Favorite_subject}")
	print(f"Expected Graduation: {Graduation_year}\tYears Left: {int(Graduation_year) - 2025}")
	print(f"Extracurricular Activities: {Extracurricular}\n{"-" * 40}")

main()