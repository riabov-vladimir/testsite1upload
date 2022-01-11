import datetime
from django.shortcuts import render


def index_view(request):
    now = datetime.datetime.now()
    return render(request,
                  'indexpage/index.html',
                  context={'current_date': now})
