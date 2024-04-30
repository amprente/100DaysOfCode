class Job:
  def __init__(self, name, salary, hours_worked):
      self.name = name
      self.salary = salary
      self.hours_worked = hours_worked

  def print_details(self):
      print(f"\n🌟Jobs Jobs Jobs!🌟\n\nJob type: {self.name}\nSalary: {self.salary}\nHours worked: {self.hours_worked}")


class Doctor(Job):
    def __init__(self, name, salary, hours_worked, speciality, years_of_experience):
        super().__init__(name, salary, hours_worked)
        self.speciality = speciality
        self.years_of_experience = years_of_experience

    def print_details(self):
        super().print_details()
        print(f"Speciality: {self.speciality}\nYears of Experience: {self.years_of_experience}")

class Teacher(Job):
    def __init__(self, name, salary, hours_worked, subject, position):
        super().__init__(name, salary, hours_worked)
        self.subject = subject
        self.position = position

    def print_details(self):
        super().print_details()
        print(f"Subject: {self.subject}\nPosition: {self.position}")


# Creating instances
lawyer = Job("Lawyer", "$ Squillions", 60)
cs_teacher = Teacher("Teacher", "$ Nowhere near enough", "All of them", "Computer Science", "Classroom Teacher")
pediatric_doctor = Doctor("Doctor", "$ Doing very nicely thank you", 50, "Pediatric Consultant", 7)

# Printing details
lawyer.print_details()
cs_teacher.print_details()
pediatric_doctor.print_details()
