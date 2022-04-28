from django.contrib import admin
from courses.models import course, student, teacher

# Register your models here.
class courseAdmin(admin.ModelAdmin):
    pass

class studentAdmin(admin.ModelAdmin):
    pass

class teacherAdmin(admin.ModelAdmin):
    pass

admin.site.register(course, courseAdmin)
admin.site.register(student, studentAdmin)
admin.site.register(teacher, teacherAdmin)