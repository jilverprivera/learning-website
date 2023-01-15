from django.urls import path

from .views import *

urlpatterns = [
    path('sections/', SectionListView.as_view(), name='GET_ALL_SECTIONS'),
    path('section/add_new/<uuid:course_uuid>/', CreateSectionView.as_view(), name='CREATE_COURSE_SECTION'),
    path('section/update/<uuid:section_uuid>/', UpdateSectionView.as_view(), name='UPDATE_COURSE_SECTION'),
    path('section/update/section_number/<uuid:section_uuid>/', UpdateSectionNumberView.as_view(), name='UPDATE_COURSE_SECTION_NUMBER'),
    path('section/delete/<uuid:section_uuid>/', DeleteSectionView.as_view(), name='DELETE_COURSE_SECTION'),
]
