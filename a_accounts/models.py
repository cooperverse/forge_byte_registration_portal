from django.db import models

# Create your models here.

class Register(models.Model):
    email = models.EmailField()
    roll = models.IntegerField()
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    fathers_name = models.CharField(max_length=266)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=11)
    
    #Gender Choices
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="Male")
    
    # Department Choices
    DEPARTMENT_CHOICES = [
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
        ('ECE', 'ECE'),
        ('CIVIL', 'Civil'),
        ('MECH', 'Mechanical'),
    ]
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES, default="CSE")
    
    # Course choices
    COURSE_CHOICES = [
        ('BSc', 'BSc'),
        ('MSc', 'MSc'),
        ('DIPLOMA', 'Diploma'),
        ('CERT', 'Certificate'),
    ]
    course = models.CharField(max_length=11, choices=COURSE_CHOICES, default="BSc")
    student_photo = models.ImageField(upload_to='images/')
    city = models.CharField(max_length=50)
    address = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class AcademicQualification(models.Model):
    register = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='qualifications')
    exam_name = models.CharField(max_length=50)
    institute_name = models.CharField(max_length=150)
    group_subject = models.CharField(max_length=100, blank=True, null=True)
    board_university = models.CharField(max_length=150, blank=True, null=True)
    passing_year = models.CharField(max_length=10, blank=True, null=True)
    gpa = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.register.first_name} {self.register.last_name} - {self.exam_name}"