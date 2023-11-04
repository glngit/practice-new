from django.shortcuts import render
from . import forms

# Create your views here.
def totalview(request):
    sent=False
    form=forms.Totalvalidations()
    if request.method=='POST':
        form=forms.Totalvalidations(request.POST)
        if form.is_valid():
            print('Form validation success and printing information')
            print('Name:',form.cleaned_data['name'])
            print('Roll No:',form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            sent=True
    return render(request,'totalapp/total.html',{'f':form,'se':sent})
