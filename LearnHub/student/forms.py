from django import forms
from .models import Student 
from course.models import Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'study_year', 'enrollment_date', 'image', 'courses']  # ← ضيف courses هنا
        widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # تخصيص عرض الكورسات كـ checkbox
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

