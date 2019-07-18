from django.contrib import admin
from .models import Teacher
class TeacherAdmin(admin.ModelAdmin):
	list_display=("first_name","last_name","regestration_number","email","image")
	search_felds=("teacher_regestration_number","teacher_email","teacher_first_name")
admin.site.register(Teacher,TeacherAdmin)

# class TeacherAdmin(admin.ModelAdmin):
# 	"""docstring for TeacherAdmin"""
# 	readonly_fields=[...,"image"]
# 	def image(self,obj):
# 		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
# 			url = obj.image.url,
#             width=obj.image.width,
#             height=obj.image.height,
#             )
#     )

# Register your models here.
