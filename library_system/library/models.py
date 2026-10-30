from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    copies_available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=date.today() + timedelta(days=14))
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} - {self.member.user.username}"