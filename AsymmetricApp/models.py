from django.db import models

# Create your models here.
class ServicesForHomePage(models.Model):
    # icon = models.ImageField(upload_to='ServiceHome/')
    title = models.CharField(max_length=20)
    details = models.TextField()
     
    def __str__(self) -> str:
        return self.title
    
class CaseStudiesDatas(models.Model):
    SERVICE_CHOICES = [
        ('Branding', 'Branding'),
        ('Digital', 'Digital'),
        ('Ecommerce', 'Ecommerce'),
        ('Print', 'Print'),
    ]
    title = models.CharField(max_length=66)
    image = models.ImageField(upload_to='case_studies/')
    details = models.TextField()
    service_type = models.CharField(max_length=10, choices=SERVICE_CHOICES, default='Branding')

    def __str__(self):
        return self.title
    

class WorksForUser(models.Model):
    work = models.CharField(max_length=230)
    practice = models.CharField(max_length=66)

    def __str__(self):
        return f"{self.work} - {self.practice}"


class User(models.Model):
    f_name = models.CharField(max_length=44)
    icon_for_user_account = models.ImageField(upload_to='icons_for_acc/')
    my_comment_on_this_site = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    work = models.ForeignKey(WorksForUser, related_name='user_work', on_delete=models.CASCADE)
    practice = models.ForeignKey(WorksForUser, related_name='user_practice', on_delete=models.CASCADE)


class Company(models.Model):
    company_name = models.CharField(max_length=99)
    company_image = models.ImageField(upload_to='company_images/')
    company_phone = models.CharField(max_length=33)
    accepts_workers = models.BooleanField(default=False)
    company_builded_at = models.CharField(max_length=255)
    the_company_exists = models.CharField(max_length=300)
    CEO_of_the_company = models.CharField(max_length=66)
    how_many_employees = models.IntegerField()


class CompanyView(models.Model):
    about_company = models.CharField(max_length=99)
    detail_of_company = models.TextField()
    company = models.ForeignKey(Company, related_name='company_views', on_delete=models.CASCADE)  
    company_image = models.ImageField(upload_to='aaaa')  
    company_builded_at = models.ForeignKey(Company, related_name='company_build_dates_views', on_delete=models.CASCADE) 
    accepts_workers = models.ForeignKey(Company, related_name='accepts_workers_views', on_delete=models.CASCADE)  

    
    