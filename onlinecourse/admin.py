from django.contrib import admin
# <HINT> 在这里导入任何新模型
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission
# <HINT> 在这里注册 QuestionInline 和 ChoiceInline 类
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2
# 在这里注册您的模型。
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
# <HINT> 在这里注册 Question 和 Choice 模型
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)