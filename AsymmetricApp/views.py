from django.shortcuts import render,redirect,get_object_or_404
from .forms import ServicesForHomePageForm, UserForm, WorksForUserForm, CaseStudiesDatasForm, CompanyForm, CompanyViewForm
from .models import ServicesForHomePage, CaseStudiesDatas, CaseStudiesDatas, WorksForUser, User, Company, CompanyView
from django.http import Http404

# bu yerda html faylarni joylashuvi va saytdan saytga otish uchun yozilgan

def home(request):
    items = ServicesForHomePage.objects.all()
    case_studies = CaseStudiesDatas.objects.all()
    users = User.objects.all()
    company_views = CompanyView.objects.all()  # Получаем данные из CompanyView

    context = {
        'items': items,
        'case_studies': case_studies,
        'users': users,
        'company_views': company_views  # Добавляем их в контекст
    }

    return render(request, 'index-asymmetric-agency.html', context)

def about_us(request):
    return render(request, 'page-asymmetric-agency-about-us.html')

def case_studies(request):
    return render(request, 'page-asymmetric-agency-case-studies.html')

def expertise(request):
    return render(request, 'page-asymmetric-agency-expertise.html')

def our_approach(request):
    return render(request, 'page-asymmetric-agency-our-approach.html')

def page_404(request, exception=None):
    return render(request, 'page-404.html', status=404)

# bu yerda esa service uchun CRUD yozilgan

def services_detail(request, services_id):
    try:
        item = ServicesForHomePage.objects.get(id=services_id)
    except ServicesForHomePage.DoesNotExist:
        return render(request, '404.html', status=404)
    return render(request, 'services_detail.html', {'item': item})  

def add_services(request):
    if request.method == 'POST':
        form = ServicesForHomePageForm(request.POST, request.FILES)
        if form.is_valid():
            item = ServicesForHomePage(
                # icon=form.cleaned_data['icon'],  # Если вы используете иконку, убедитесь, что она обрабатывается корректно
                title=form.cleaned_data['title'],
                details=form.cleaned_data['details']
            )
            item.save()
            return redirect('home')
    else:
        form = ServicesForHomePageForm()
    
        items = ServicesForHomePage.objects.all()
        return render(request, 'add_services.html', {'form': form, 'items': items})
    if request.method == 'POST':
        form = ServicesForHomePageForm(request.POST)
        if form.is_valid():
            item = ServicesForHomePage(
                # icon=form.cleaned_data['icon'],
                title=form.cleaned_data['title'],
                details=form.cleaned_data['details']
            )
            item.save()
            return redirect('home')
    else:
        form = ServicesForHomePageForm()
    
    items = ServicesForHomePage.objects.all()
    return render(request, 'add_services.html', {'form': form, 'items': items})

def edit_service(request, services_id):
    try:
        item = ServicesForHomePage.objects.get(id=services_id)
    except ServicesForHomePage.DoesNotExist:
        return redirect('home')  # Или возвращайте страницу ошибки, если хотите

    if request.method == 'POST':
        form = ServicesForHomePageForm(request.POST)
        if form.is_valid():
            item.title = form.cleaned_data['title']
            item.details = form.cleaned_data['details']
            item.save()
            return redirect('home')  # Переход на главную страницу или другую нужную страницу
    else:
        form = ServicesForHomePageForm(initial={'title': item.title, 'details': item.details})
    return render(request, 'edit_service.html', {'form': form})

def delete_service(request, services_id):
    try:
        item = ServicesForHomePage.objects.get(id=services_id)
    except ServicesForHomePage.DoesNotExist:
        return redirect('home')  # Или возвращайте страницу ошибки, если хотите

    if request.method == 'POST':
        item.delete()
        return redirect('home')  # Переход на главную страницу или другую нужную страницу
    return render(request, 'delete_service.html', {'item': item})

# bu yerda Studies uchun CRUD yozilgan

def study_detail(request, study_id):
    try:
        case_study = CaseStudiesDatas.objects.get(id=study_id)
    except CaseStudiesDatas.DoesNotExist:
        raise Http404("Case study not found")
    
    return render(request, 'case_studies_view.html', {'case_study': case_study})

def add_case_study(request):
    if request.method == 'POST':
        form = CaseStudiesDatasForm(request.POST, request.FILES)
        if form.is_valid():
            case_study = CaseStudiesDatas(
                title=form.cleaned_data['title'],
                image=form.cleaned_data['image'],
                details=form.cleaned_data['details'],
                service_type=form.cleaned_data['service_type']
            )
            case_study.save()
            return redirect('home')
    else:
        form = CaseStudiesDatasForm()
    
    return render(request, 'add_case_study.html', {'form': form})

def edit_case_study(request, case_study_id):
    try:
        case_study = CaseStudiesDatas.objects.get(id=case_study_id)
    except CaseStudiesDatas.DoesNotExist:
        case_study = None

    if request.method == 'POST':
        form = CaseStudiesDatasForm(request.POST, request.FILES)
        if form.is_valid() and case_study:
            case_study.title = form.cleaned_data['title']
            case_study.image = form.cleaned_data['image']
            case_study.details = form.cleaned_data['details']
            case_study.service_type = form.cleaned_data['service_type']
            case_study.save()
            return redirect('home')
    else:
        form = CaseStudiesDatasForm(initial={
            'title': case_study.title,
            'details': case_study.details,
            'service_type': case_study.service_type
        })

    return render(request, 'edit_case_study.html', {'form': form, 'case_study': case_study})

def delete_case_study(request, case_study_id):
    try:
        case_study = CaseStudiesDatas.objects.get(id=case_study_id)
        case_study.delete()
    except CaseStudiesDatas.DoesNotExist:
        pass

    return redirect('home')

# bu yerda User uchun CRUD yozilgan 

def add_works_for_user(request):
    if request.method == 'POST':
        form = WorksForUserForm(request.POST)
        if form.is_valid():
            work = form.cleaned_data['work']
            practice = form.cleaned_data['practice']
            WorksForUser.objects.create(work=work, practice=practice)
            
            return redirect('home')
    else:
        form = WorksForUserForm()
    return render(request, 'ForUser/add_works_for_user.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('some_success_url') 
    
    return render(request, 'ForUser/delete_user.html', {'user': user})

def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'ForUser/user_detail.html', {'user': user})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            User.objects.create(
                f_name=form.cleaned_data['f_name'],
                icon_for_user_account=form.cleaned_data['icon_for_user_account'],
                my_comment_on_this_site=form.cleaned_data['my_comment_on_this_site'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                work=form.cleaned_data['work'],
                practice=form.cleaned_data['practice']
            )
            return redirect('home') 
    else:
        form = UserForm()
    return render(request, 'ForUser/create_user.html', {'form': form})

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.f_name = form.cleaned_data['f_name']
            user.icon_for_user_account = form.cleaned_data['icon_for_user_account']
            user.my_comment_on_this_site = form.cleaned_data['my_comment_on_this_site']
            user.email = form.cleaned_data['email']
            user.phone = form.cleaned_data['phone']
            user.work = form.cleaned_data['work']
            user.practice = form.cleaned_data['practice']
            user.save()
            return redirect('home')  
    else:
        form = UserForm(initial={
            'f_name': user.f_name,
            'icon_for_user_account': user.icon_for_user_account,
            'my_comment_on_this_site': user.my_comment_on_this_site,
            'email': user.email,
            'phone': user.phone,
            'work': user.work,
            'practice': user.practice
        })
    return render(request, 'ForUser/edit_user.html', {'form': form, 'user': user})

# bu yerda company uchun views yozilgan

def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = Company(
                company_name=form.cleaned_data['company_name'],
                company_image=form.cleaned_data['company_image'],
                company_phone=form.cleaned_data['company_phone'], 
                accepts_workers=form.cleaned_data['accepts_workers'],
                company_builded_at=form.cleaned_data['company_builded_at'],
                the_company_exists=form.cleaned_data['the_company_exists'],
                CEO_of_the_company=form.cleaned_data['CEO_of_the_company'],
                how_many_employees=form.cleaned_data['how_many_employees']
            )
            company.save()
    else:
        form = CompanyForm()

    return render(request, 'ForCompany/add_company.html', {'form': form})

def edit_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, initial={
            'company_name': company.company_name,
            'company_image': company.company_image,
            'copmany_phone': company.copmany_phone,
            'accepts_workers': company.accepts_workers,
            'company_builded_at': company.company_builded_at,
            'the_company_exists': company.the_company_exists,
            'CEO_of_the_company': company.CEO_of_the_company,
            'how_many_employees': company.how_many_employees
        })
        if form.is_valid():
            company.company_name = form.cleaned_data['company_name']
            company.company_image = form.cleaned_data['company_image']
            company.copmany_phone = form.cleaned_data['copmany_phone']
            company.accepts_workers = form.cleaned_data['accepts_workers']
            company.company_builded_at = form.cleaned_data['company_builded_at']
            company.the_company_exists = form.cleaned_data['the_company_exists']
            company.CEO_of_the_company = form.cleaned_data['CEO_of_the_company']
            company.how_many_employees = form.cleaned_data['how_many_employees']
            company.save()
            return redirect('home') 
    else:
        form = CompanyForm(initial={
            'company_name': company.company_name,
            'company_image': company.company_image,
            'copmany_phone': company.copmany_phone,
            'accepts_workers': company.accepts_workers,
            'company_builded_at': company.company_builded_at,
            'the_company_exists': company.the_company_exists,
            'CEO_of_the_company': company.CEO_of_the_company,
            'how_many_employees': company.how_many_employees
        })
    return render(request, 'ForCompany/edit_company.html', {'form': form})

def delete_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('home')  
    return render(request, 'ForCompany/delete_company.html', {'company': company})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'ForCompany/company_detail.html', {'company': company})

# bu yerda CompanyView uchun CRUD yozilgan

def add_company_view(request):
    if request.method == 'POST':
        form = CompanyViewForm(request.POST)
        if form.is_valid():
            company_view = CompanyView(
                about_company=form.cleaned_data['about_company'],
                detail_of_company=form.cleaned_data['detail_of_company'],
                company=form.cleaned_data['company'],
                company_image=form.cleaned_data['company_image'],
                company_builded_at=form.cleaned_data['company_builded_at'],
                accepts_workers=form.cleaned_data['accepts_workers']
            )
            company_view.save()
            return redirect('home')
    else:
        form = CompanyViewForm()
    return render(request, 'ForCompanyView/add_company_view.html', {'form': form})

def edit_company_view(request, pk):
    company_view = get_object_or_404(CompanyView, pk=pk)
    if request.method == 'POST':
        form = CompanyViewForm(request.POST, instance=company_view)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CompanyViewForm(instance=company_view)
    return render(request, 'ForCompanyView/edit_company_view.html', {'form': form})

def delete_company_view(request, pk):
    company_view = get_object_or_404(CompanyView, pk=pk)
    if request.method == 'POST':
        company_view.delete()
        return redirect('home')
    return render(request, 'ForCompanyView/delete_company_view.html', {'company_view': company_view})

def company_view_detail(request, pk):
    company_view = get_object_or_404(CompanyView, pk=pk)
    return render(request, 'ForCompanyView/company_view_detail.html', {'company_view': company_view})