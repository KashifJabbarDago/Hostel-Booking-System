from django.contrib import admin
from .models import BookVacancy,RegisterHostel,SignUp,ContactUs
# Register your models here.
admin.site.register(BookVacancy)
admin.site.register(RegisterHostel)
admin.site.register(SignUp)
admin.site.register(ContactUs)