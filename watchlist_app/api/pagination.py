from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class WatchlistPagination(PageNumberPagination):
    page_size = 2
    # page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 5 
    # last_page_strings = 'end'
    
class WatchlistLimitOffsetPAgination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'start '