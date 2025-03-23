from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.http import HttpResponse
# from django.core.mail import get_connection, EmailMultiAlternatives
from django.db.models.functions import Length
from django.views.generic import ListView
# from django import template
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import CallbackForm, CallbacktelegramForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .forms import CallbacktelegramForm
# import requests

# from django.core.mail import send_mail
# from .forms import CallbackRequestForm

from django.conf import settings
from home.models import *

# class HomeIndex(ListView):
#     # model = BrieftDraft
#     template_name = 'home/index.html'

def home(request):
    # diamonds = Diamond.objects.filter(is_home=True)
    # models = ModeledFoto.objects.filter(is_home=True)
    # sketches = SketchFoto.objects.filter(is_home=True)
    # weddingrings = Weddingrings.objects.filter(is_home=True)
    context = {
        'title': 'Тамбовская Ювелирная Компания | Ювелирные изделия под заказ',
        'description': 'Тамбовская Ювелирная Компания, Ювелирные изделия под заказ',
        # 'diamonds': diamonds,
        # 'models': models,
        # 'sketches': sketches,
        # 'weddingrings': weddingrings,
        # 'query_about': About.objects.filter(is_home=True).get(pk=1),
        # 'query_result': Video.objects.order_by('time_create')[:9],
        # 'query': Video.objects.get(pk=1), 
    }
    return render(request, "index.html", context)


def chat(request):
    context = {
        'title': 'Чат с искусственным интелектом',
        'description': 'Чат с искусственным интелектом',
        'current_path': request.get_full_path(),
    }
    return render(request, "chat.html", context)


def about(request):
    context = {
        'title': 'Наша команда | Тамбовская Ювелирная Компания',
        'description': 'Сотрудники тамбовской ювелирной компании',
        'team': Team.objects.get(pk=1),
        'q_team': Team.objects.all(),
        'query_about': About.objects.get(pk=1),
        'query_result': Video.objects.order_by('time_create')[:9],
        'query': Video.objects.get(pk=1), 
    }
    return render(request, "about.html", context)

def contacts(request):
    # success = ''
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     success = 'Сообщение отправлено успешно!'
    #     if form.is_valid():
    #         send_message(form.cleaned_data['name'], form.cleaned_data['phone'], form.cleaned_data['phone'], form.cleaned_data['message'])
    #         success = 'Сообщение отправлено успешно!'
    # else:
    #     form = ContactForm()

    context = {
        'title': 'Наши контакты | Тамбовская Ювелирная Компания',
        'description': 'Контакты тамбовской ювелирной компании,тамбов мичуринская 92',
        # 'query_result': Contact_1.objects.order_by('time_create'), 
        'query_result': Contact.objects.get(pk=1), 
        # 'form': form,
        # 'success': success,
    }
    return render(request, "contacts.html", context)


# def send_message(name, email, phone, message):
#     # text = template('message.html')
#     # html = template('message.html')
#     text = 'Text'
#     html = 'Html'
#     context = {'name': name, 'email': email, 'phone': phone, 'message': message}
#     subject = 'Сообщение от пользователя'
#     from_email = 'shop@tropicana-store.ru'
#     text_content = text.render(context)
#     html_content = html.render(context)

#     msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()


def nature(request):
    # count= Nature.objects.all().count()
    published_posts = Nature.objects.filter(is_published=True).count()

    context = {
        'title': 'Экология | Тамбовская Ювелирная Компания',
        'description': 'Экология. Тамбовская Ювелирная компания. Тамбов.',
        'query_result': Nature.objects.order_by('time_create'),
        'published_posts': published_posts,
    }
    return render(request, "nature.html", context)


def single_nature(request, post_id):
    post = get_object_or_404(Nature, pk=post_id)
    list_post =  Nature.objects.order_by('time_create')[:10]
    right = 'order-md-2'

    context = {
        'title': post.title + ' ' + '| Тамбовская Ювелирная Компания',
        'description': post.title + ' ' + 'Экология. Тамбовская Ювелирная компания. Тамбов.',
        'post': post,
        'list_post': list_post,
        'right': right,
    }
    return render(request, "single-nature.html", context)


def policy(request):
    context = {
        'title': 'Политика обработки персональных данных',
        'description': 'Политика обработки персональных данных',
    }
    return render(request, "policy.html", context)



def diamonds(request):
    posts_list = Diamond.objects.filter(is_published=True).order_by('-time_create')
    paginator = Paginator(posts_list, 1)  # Показывать 10 записей на странице

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, показываем первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если страница выходит за пределы диапазона, показываем последнюю страницу
        posts = paginator.page(paginator.num_pages)

    return render(request, 'category/diamonds.html', {'posts': posts})


    # diamonds = Diamond.objects.filter(is_published=True)

    # context = {
    #     'title': 'Продажа брилиантов | Тамбовская Ювелирная компания',
    #     'description': 'Продажа брилиантов, продажа брилиантов в тамбове, 3D модель кольца с бриллиантом, тамбовская ювелирная компания',
    #     'diamonds': diamonds,
    # }
    # return render(request, "category/diamonds.html", context)


def clips(request):
    clips = Clip.objects.filter(is_published=True)[:50]

    context = {
        'title': 'Изготовление запонок и зажимов из драгоценных металлов | Тамбовская Ювелирная компания',
        'description': 'Продажа запонок, зажимов, изготовление запонок на заказ в тамбове, с драгоценными камнями',
        'clips': clips,
    }
    return render(request, "category/clips.html", context)


def weddingrings(request):
    weddingrings = Weddingrings.objects.filter(is_published=True)[:50]

    context = {
        'title': 'Изготовление обручальных колец на заказ | Тамбовская Ювелирная компания',
        'description': 'Продажа обручальных колец на заказ, обручальные, изготовление обручальных колец в тамбове, с драгоценными камнями',
        'weddingrings': weddingrings,
    }
    return render(request, "category/weddingrings.html", context)



def earrings(request):
    earrings = Earring.objects.filter(is_published=True)[:50]

    context = {
        'title': 'Серьги, подвески, кулоны на заказ | Тамбовская Ювелирная компания',
        'description': 'Изготовление ювелирных изделий в тамбове, продажа кулонов, подвесок, сережек, на заказ, с драгоценными камнями',
        'earrings': earrings,
    }
    return render(request, "category/earrings.html", context)



def amulets(request):
    amulets = Amulets.objects.filter(is_published=True)[:50]

    context = {
        'title': 'Украшения - славянские обереги | Тамбовская Ювелирная компания',
        'description': 'Изготовление украшений славянских оберегов в тамбове на заказ, с драгоценными камнями',
        'amulets': amulets,
    }
    return render(request, "category/amulets.html", context)



def rings(request):
    rings = Ring.objects.filter(is_published=True)[:50]
 
    context = {
        'title': 'Кольца, перстни, печатки | Тамбовская Ювелирная компания',
        'description': 'Ювелирные кольца, перстни, печатки на заказ, с драгоценными камнями',
        'rings': rings,
    }
    return render(request, "category/rings.html", context)


@require_http_methods(["POST"])
def callback_request(request):
    form = CallbackForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success', 'message': 'Ваше сообщение отправлено. Наш специалист ответит вам в ближайшее время.'})
    return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)


def send_telegram_message(message):
    bot_token = '7652070722:AAEoSRkGcTkelEwYT2m7P3xI7wQu4fCu3pA'
    chat_id = '-1002270506445'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message,
    }
    response = requests.post(url, data=payload)
    return response.ok


def callbacktelegram_form(request):
    if request.method == 'POST':
        form = CallbacktelegramForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = f"Новая заявка на обратный звонок:\nИмя: {name}\nТелефон: {phone}"
            if send_telegram_message(message):
                # return HttpResponse("<h3><center>Спасибо! Мы скоро вам перезвоним.</h3></center>")
                return render(request, 'callbacktelegram.html', {'form': form})
            else:
                return HttpResponse("Ошибка при отправке заявки.")
    else:
        form = CallbacktelegramForm()
    return render(request, 'callbacktelegram.html', {'form': form})


def badges(request):
    badges_one = Badge.objects.get(pk=1)
    badges_foto = BadgeFoto.objects.filter(is_published=True)
    context = {
        'title': 'Изготовление нагрудных знаков из драгоценных металлов',
        'description': 'Изготовление значков, медалей, нагрудных знаков из драгоценных металлов',
        'badges': badges,
        'badges_one': badges_one,
        'badges_foto': badges_foto,
    }
    return render(request, "services/badges.html", context)


def price(request):
    prices = Price.objects.filter(is_published=True)
    context = {
        'title': 'Прейскурант на ремонт ювелирных изделий',
        'description': 'Прейскурант на ремонт ювелирных изделий',
        'prices': prices,
    }
    return render(request, "services/price.html", context)


def cast(request):
    cast_one = Cast.objects.get(pk=1)
    cast_foto = CastFoto.objects.filter(is_published=True)
    context = {
        'title': 'Услуга литья драгоценных и цветных металлов',
        'description': 'Услуга литья драгоценных и цветных металлов',
        'cast_one': cast_one,
        'cast_foto': cast_foto,
    }
    return render(request, "services/cast.html", context)


def electroplating(request):
    electroplating = Electroplating.objects.get(pk=1)
    electroplating_foto = ElectroplatingFoto.objects.filter(is_published=True)
    context = {
        'title': 'Гальванизация изделий из драгоценных и цветных металлов',
        'description': 'Гальванизация изделий из драгоценных и цветных металлов.. Тамбовская Ювелирная компания.',
        'electroplating': electroplating,
        'electroplating_foto': electroplating_foto,
    }
    return render(request, "services/electroplating.html", context)


def sketches(request):
    sketches = Sketch.objects.get(pk=1)
    sketches_foto = SketchFoto.objects.filter(is_published=True)
    context = {
        'title': 'Разработка эскизов ювелирных изделий, нагрудных знаков, значков, медалей и сувенирной продукции.',
        'description': 'Разработка эскизов ювелирных изделий, нагрудных знаков, значков, медалей и сувенирной продукции.',
        'sketches': sketches,
        'sketches_foto': sketches_foto,
    }
    return render(request, "services/sketches.html", context)


def models(request):
    models = Modeled.objects.get(pk=1)
    models_foto = ModeledFoto.objects.filter(is_published=True)
    models_video = ModeledVideo.objects.filter(is_published=True)
    context = {
        'title': '3D - моделирование ювелирных изделий',
        'description': '3D - моделирование ювелирных изделий .. Тамбовская Ювелирная Компания',
        'models': models,
        'models_foto': models_foto,
        'models_video': models_video,
    }
    return render(request, "services/models.html", context)


def culc(request):
    context = {
        'title': 'Калькулятор',
    }
    return render(request, "culc.html", context)



# def search(request):
#     search_query = request.GET.get('search', None)
#     if search_query:
#         search_result = Diamond.objects.filter(
#             Q(title__icontains=search_query)
#             |
#             Q(content__icontains=search_query)
#         )

#     context = {
#         'title': 'Поиск по сайту | Тамбовская Ювелирная компания',
#         'description': 'Поиск по сайту, тамбовская ювелирная компания',
#         'search_query': search_query,
#         'search_result': search_result,
#     }
#     return render(request, "search.html", context)


def search(request, *args, **kwargs):
    # er_q = "Короткий запрос не менее 3 сммволов"
    # q = request.GET['q']
    q = request.GET.get('q')
    if q:
        obj = Diamond.objects.filter(Q(title__icontains=q) | Q(content__icontains=q), is_published=True)
        obj2 = Nature.objects.filter(Q(title__icontains=q) | Q(content__icontains=q), is_published=True)
        obj3 = Earring.objects.filter(Q(title__icontains=q) | Q(content__icontains=q), is_published=True)
        obj4 = Amulets.objects.filter(Q(title__icontains=q) | Q(content__icontains=q), is_published=True)

    context = {
        'title': 'Поиск по сайту | Тамбовская Ювелирная компания',
        'description': 'Поиск по сайту, тамбовская ювелирная компания',
        'obj': obj,
        'obj2': obj2,
        'obj3': obj3,
        'obj4': obj4,
        'q': q,
        'sum': len(obj)+len(obj2)+len(obj3)+len(obj4),
    }

    return render(request, 'search.html', context)


def categories(request, catid):
    print(request.GET)
    return HttpResponse(f"<h1>Hello, Category!</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2024:
        # raise Http404()
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Archive, Category!</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found. Error 404!</h1>")


