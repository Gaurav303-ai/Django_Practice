from django import forms

class Registration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    city=forms.CharField()
    roll=forms.IntegerField()

class detail(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

class Address(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    city=forms.CharField()
    street=forms.IntegerField()