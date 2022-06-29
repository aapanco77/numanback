import pytest


# @pytest.mark.django_db
def addrecord(request):
    companyName = request.POST['company']
    progress = request.POST['progress']

    assert companyName == 'Company'