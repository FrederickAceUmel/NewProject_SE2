from django import forms

class VerifyForm(forms.Form):
    proofOfIncome = forms.FileField()
    governmentId = forms.FileField()