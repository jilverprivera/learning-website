from django.urls import path
from ..views import CategoryListView, LatestCategoriesView, CategoryView, SubCategoriesListView, SubCategoryView, SubCategoryByPrincipalView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('category/<str:pk>/', CategoryView.as_view()),
    path('categories/latest/', LatestCategoriesView.as_view()),

    path('sub-categories/', SubCategoriesListView.as_view()),
    path('sub-category/<str:pk>/', SubCategoryView.as_view()),
    path('category/<str:principal>/sub-categories/', SubCategoryByPrincipalView.as_view()),
    
]
