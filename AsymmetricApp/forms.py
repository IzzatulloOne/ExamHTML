from django import forms
from .models import ServicesForHomePage, WorksForUser, CaseStudiesDatas, CaseStudiesDatas, Company


class ServicesForHomePageForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter title'
        })
    )
    details = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Enter details'
        })
    )


class CaseStudiesDatasForm(forms.Form):
    title = forms.CharField(
        max_length=66,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter case study title'
        })
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })
    )
    details = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Enter case study details'
        })
    )
    service_type = forms.ChoiceField(
        choices=CaseStudiesDatas.SERVICE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )


class WorksForUserForm(forms.Form):
    work = forms.CharField(max_length=230, widget=forms.TextInput(attrs={'placeholder': 'work'}))
    practice = forms.CharField(max_length=66, widget=forms.TextInput(attrs={'placeholder': 'practice'}))


class UserForm(forms.Form):
    f_name = forms.CharField(max_length=44)
    icon_for_user_account = forms.ImageField()
    my_comment_on_this_site = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    phone = forms.CharField(max_length=13)
    work = forms.ModelChoiceField(queryset=WorksForUser.objects.all())
    practice = forms.ModelChoiceField(queryset=WorksForUser.objects.all())


class CompanyForm(forms.Form):
    company_name = forms.CharField(max_length=99, widget=forms.TextInput(attrs={'placeholder': 'Enter company name'}))
    company_image = forms.ImageField(required=False)
    company_phone = forms.CharField(max_length=33, widget=forms.TextInput(attrs={'placeholder': 'Enter company phone'}))
    accepts_workers = forms.BooleanField(required=False)
    company_builded_at = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter year built'}))
    the_company_exists = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'placeholder': 'Enter company history'}))
    CEO_of_the_company = forms.CharField(max_length=66, widget=forms.TextInput(attrs={'placeholder': 'Enter CEO name'}))
    how_many_employees = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter number of employees'}))


class CompanyViewForm(forms.Form):
    about_company = forms.CharField(max_length=99, widget=forms.TextInput(attrs={'placeholder': 'About Company'}))
    detail_of_company = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Detail of Company'}))
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select Company")
    company_image = forms.ImageField()
    company_builded_at = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select Company Build Date")
    accepts_workers = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select Accepts Workers")