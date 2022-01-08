from django import forms

class SendEmail(forms.Form):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Name', 'id' : 'name', 'label':"Name"}))
    email = forms.EmailField(max_length=40, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Your Email', 'id' : 'email', 'label':"Email"}))
    phone = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Phone', 'id' : 'phone', 'label':"Phone"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Write A Message', 'id' : 'message', 'label':"Message"}))
            
