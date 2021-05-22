from service.models import Service

def menu_link(request):
    link=Service.objects.all()
    return dict(link=link)
