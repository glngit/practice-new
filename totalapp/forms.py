from django import forms


class Totalvalidations(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    def clean(self):                 # it is not mandatory to be clean
        print('Total form validation...')
        total_cleaned_data=super().clean()
        inputname=total_cleaned_data['name']
        if inputname[0].lower() != 'd':
            raise forms.ValidationError('Name parameter should starts with d')
        inputrollno=total_cleaned_data['rollno']
        if inputrollno <=0:
            raise forms.ValidationError('Rollno should be >0')
