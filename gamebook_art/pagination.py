from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pagination(request, data, num=10):
    paginator = Paginator(data, num)
    page = request.GET.get('data')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number -1
    max_index = len(paginator.page_range)
    start_index = index - 11 if index >= 11 else 0
    end_index = index + 11 if index <= max_index - 11 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return items, page_range
