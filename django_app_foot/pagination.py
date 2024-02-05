from rest_framework import pagination


class MyPaginationClass(pagination.PageNumberPagination):
    page_size = 50
    max_page_size = 100000000
    page_size_query_param = "size"
