from django import forms

class WaitList(forms.Form):
	My_email_is = forms.CharField(max_length=20)