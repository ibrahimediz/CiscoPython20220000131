from django.shortcuts import render


def iletisimlist(request):
    return render(request, 'iletisim/iletisimlist.html',{})