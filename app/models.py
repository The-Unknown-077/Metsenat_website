from django.db import models

class Sponsor(models.Model):
    class choices(models.TextChoices):
        NEW = "new", "yangi"
        MODERNATION = "modernation", "modernation"
        APPROVED = "approved", "approved"
        CANCELLED = "cancelled", "cancelled"
    class choices2(models.TextChoices):
        KARTA_ORQALI = "karta_orqali", "karta_orqali"
        NAQD = "naqd", "naqd"
    class choices3(models.TextChoices):
        PERSONAL = "personal", "personal"
        LEGAL = "legal", "legal"
    full_name = models.CharField(max_length=32)
    phone_number = models.IntegerField()
    donation_amout = models.IntegerField()
    org_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=choices3)
    status = models.CharField(max_length=255, choices=choices, default=choices.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=200, choices=choices2, null=True)

    def __str__(self):
        return self.full_name

class University(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    class a(models.TextChoices):
        NEW = "new", "yangi"
        OLD = "old", "eski"
        RECENT = "recent", "yaqinda"

    full_name = models.CharField(max_length=32)
    student_type = models.CharField(max_length=50, choices=a)
    OTM = models.ForeignKey(University, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

class StudentSponsor(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    amount = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.sponsor.full_name} - {self.student.full_name}"



 







