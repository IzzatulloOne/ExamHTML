from django.urls import path
from . import views

urlpatterns = [
    # bu yerda faqat sayddan sayga oyish uchun urllar

    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('case_studies/', views.case_studies, name='studies'),  
    path('expertise/', views.expertise, name='expertise'),
    path('our_approach/', views.our_approach, name='our_approach'),
    path('notfound404/', views.page_404, name='404'),

    # bu yerda study uchin urllar 

    path('studies/<int:study_id>/', views.study_detail, name='study_detail'),
    path('case_studies/add/', views.add_case_study, name='add_case_study'),
    path('case_studies/edit/<int:case_study_id>/', views.edit_case_study, name='edit_case_study'),
    path('case_studies/delete/<int:case_study_id>/', views.delete_case_study, name='delete_case_study'),

    # bu yerda service uchun urllar

    path('item/<int:services_id>/', views.services_detail, name='services_detail'),
    path('item/<int:services_id>/edit/', views.edit_service, name='edit_service'),
    path('item/<int:services_id>/delete/', views.delete_service, name='delete_service'),
    path('add_services/', views.add_services, name='add_services'),

    # bu yerda user uchun urllar

    path('users/create/', views.create_user, name='create_user'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add_works_for_user/', views.add_works_for_user, name='add_works_for_user'),
    path('user/<int:id>/', views.user_detail, name='user_detail'),

    # bu yerda Company uchun url yozilgan

    path('add_company/', views.add_company, name='add_company'),
    path('edit_company/<int:pk>/', views.edit_company, name='edit_company'),
    path('delete_company/<int:pk>/', views.delete_company, name='delete_company'),
    path('company_detail/<int:pk>/', views.company_detail, name='company_detail'),

    # bu yerda CompanyView uchun url yozilgan 

    path('add_company_view/', views.add_company_view, name='add_company_view'),
    path('edit_company_view/<int:pk>/', views.edit_company_view, name='edit_company_view'),
    path('delete_company_view/<int:pk>/', views.delete_company_view, name='delete_company_view'),
    path('company_view_detail/<int:pk>/', views.company_view_detail, name='company_view_detail'),

]
