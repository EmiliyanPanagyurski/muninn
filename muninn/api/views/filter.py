from django_filters.rest_framework import DjangoFilterBackend


class CaseInsensitiveFilter(DjangoFilterBackend):
    """ Filter that allows url params to be case insensitive """

    def filter_queryset(self, request, queryset, view):
        url_param = list(request.query_params.keys())
        value = [request.query_params[value] for value in url_param]

        if 'status' in url_param:
            return queryset.filter(status__iexact=value[0])

        if 'inudstry' in url_param:
            return queryset.filter(industry__iexact=value[0])

        if 'developer' in url_param:
            return queryset.filter(developer__name__iexact=value[0])

        if 'publisher' in url_param:
            return queryset.filter(publisher__name__iexact=value[0])

        if 'engine' in url_param:
            return queryset.filter(engine__name__iexact=value[0])

        if'series' in url_param:
            return queryset.filter(series__iexact=value[0])

        if 'genre' in url_param:
            return queryset.filter(genre__iexact=value[0])

        if 'platforms' in url_param:
            return queryset.filter(platforms__contains=value[0])

        return queryset
