from django import forms
from.models import Student1
class DepartmentForm(forms.ModelForm):
    class Meta:
        model =Student1
        fields = '__all__'
class StudentForm(forms.ModelForm):
    class Meta:
        model =Student1
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        photo = cleaned_data.get('photo')
        marksheet = cleaned_data.get('marksheet')

        if photo and marksheet:
            if photo.size > 5242880:
                raise forms.ValidationError('Photo size may not exceed 5 MB')

            if not (photo.image.format == 'JPEG' or photo.image.format == 'PNG'):
                raise forms.ValidationError('Photo format must be JPEG or PNG')

            if marksheet.name.split('.')[-1] != 'pdf':
                raise forms.ValidationError('Marksheet format must be PDF')

        return cleaned_data