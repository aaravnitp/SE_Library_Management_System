from django.contrib import admin
from .models import Book, Member, BorrowRecord

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'copies_available')
    search_fields = ('title', 'author', 'isbn')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'membership_date')

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'borrow_date', 'due_date', 'returned')
    list_filter = ('returned', 'due_date')