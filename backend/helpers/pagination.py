from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class MediumPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class LargePagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20
