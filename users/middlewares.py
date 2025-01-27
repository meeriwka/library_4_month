from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class OpytRabotyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = int(request.POST.get('experience'))
            wares_junior = 1000
            wares_senior = 2000
            wares_master = 5000
            if experience >=1 and experience <3:
                request.experience = wares_junior
            elif experience >=3 and experience <5:
                request.experience = wares_senior
            elif experience >=5 and experience <7:
                request.experience = wares_master
            else:
                return HttpResponseBadRequest('Experience must be greater than 1')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request,'grade', 'Поле обязательно для заполнения')



