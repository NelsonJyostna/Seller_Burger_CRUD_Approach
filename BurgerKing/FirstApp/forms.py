from .models import Seller
from django import forms
import datetime
from django.core import validators



class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields= '__all__'
    #
    # def starts_with_caps(value):  # custom validator
    #     if value[0].upper() :
    #         raise forms.ValidationError('First letter of ur username should be starts with capital letter')
    #
    # uname = forms.CharField(max_length=50, validators=[starts_with_caps])
    # mobno = forms.CharField(max_length=10, validators=[validators.MaxLengthValidator(10)])
    # email = forms.EmailField()
    #
    # burg_type = forms.CharField(max_length=50)
    # burg_image=forms.ImageField()
    # gender = forms.CharField(max_length=30)
    # order_date = forms.DateField()
    #
    # def clean_email(self):
    #     email_passed = self.cleaned_data['email']
    #     email_req = "gmail.com"
    #     if not email_req in email_passed:
    #         raise forms.ValidationError('please enter valid email address')
    #     return email_passed