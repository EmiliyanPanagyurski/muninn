from django_filters.rest_framework import DjangoFilterBackend


class CaseInsensitiveFilter(DjangoFilterBackend):
    """ Filter that allows url params to be case insensitive """

    def filter_queryset(self, request, queryset, view):
        # import pdb; pdb.set_trace()
        param = request.query_params.get('status', None)
        if param is not None:
            data = queryset.filter(status__iexact=param)
            return data
        param = request.query_params.get('industry', None)
        if param is not None:
            data = queryset.filter(industry__iexact=param)
            return data
        param = request.query_params.get('developer', None)
        if param is not None:
            data = queryset.filter(developer__name__iexact=param)
            return data
        param = request.query_params.get('publisher', None)
        if param is not None:
            data = queryset.filter(publisher__name__iexact=param)
            return data
        param = request.query_params.get('engine', None)
        if param is not None:
            data = queryset.filter(engine__name__iexact=param)
            return data
        param = request.query_params.get('series', None)
        if param is not None:
            data = queryset.filter(series__iexact=param)
            return data
        param = request.query_params.get('genre', None)
        if param is not None:
            data = queryset.filter(genre__iexact=param)
            return data
        param = request.query_params.get('platforms', None)
        if param is not None:
            data = queryset.filter(platforms__contains=param)
            return data

        return queryset
