from django import forms
from .models import Opportunity

class OpportunityModelForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ["name", "email"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_provider = email.split("@")[1]
        if email_provider != "gmail.com":
            raise forms.ValidationError("Please, enter an Google email.")
        return email
    
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name and " " not in name:
            raise forms.ValidationError("Please, enter first and last name separated by space.")
        return name

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
