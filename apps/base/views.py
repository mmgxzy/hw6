from django.shortcuts import render, redirect
from apps.base.models import Index, Icon, Foto, Trips, Application, Blog, Workers, MnogoFoto
from apps.telegram_bot.views import get_text

# Create your views here.
def index(request):
    index_id = Index.objects.latest('id')
    icon = Icon.objects.all()
    foto = Foto.objects.all()
    iconkii = Foto.objects.all()
    blog = Blog.objects.all()
    mini_foto = MnogoFoto.objects.all()
    workers = Workers.objects.all()
    trips_all = Trips.objects.all()
    trips2_all = Trips.objects.all().order_by("?")[:2]
    return render(request, "base/index.html", locals())

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        cause = request.POST.get('cause')
        message = request.POST.get('message')
        Application.objects.create(name=name, number=number, email=email, cause=cause, message=message )
        get_text(f"""Поступила новая заявка
                 
                от пользователя: {name}
                {number}
                {email}
                {cause}
                {message}
""")
        return redirect("contact")
    return render(request, "base/contact.html")

