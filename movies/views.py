from django.shortcuts import render
from .models import Movie, Serie, Espo, Aio
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q
from itertools import chain
from django.views.generic import ListView
from django.db.models import OuterRef, Subquery
from operator import attrgetter




def home(request):
    movi = Movie.objects.all().order_by('-created')[:10]
    sear = Serie.objects.all().order_by('-created')[:10]
    ress = sorted(chain(movi, sear), key=attrgetter('created'))

    name = request.GET.get('movaname')
    print(ress)
    return render(request, 'base/index.html',{'movies':ress, 'movin':movi, 'series':sear})
def homes(request):
    movi = Movie.objects.all()
    # mova = Movie.objects.get_or_create(pk)
    # q = request.GET.get('q') if request.GET.get('q') != None else ''

    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json
    
    if is_ajax_request:
        fer = request.POST.get('result')
        print(fer)
        sear = Movie.objects.filter(
            Q(title__contains=fer)
        ).distinct()
        sear2 = Serie.objects.filter(Q(title__contains=fer)).distinct()
        rez = sorted(chain(sear, sear2), key=lambda car: car.title, reverse=True)
        print(rez)
        if len(rez) > 0 and len(fer) > 0:
            data=[]
            for ps in rez:
                movie = {
                    'pk':ps.pk,
                    'title':ps.title,
                    'poster':ps.poster.url,
                    'year':ps.year,
                    'movieid':ps.movieid
                    
                }
                print(ps)
                data.append(movie)
            res = data
        else:
            res = 'Not Found'
        # html = render_to_string(
        #     template_name="base/index.html", 
        #     context={"reser": sear}
        # )

        # data_dict = {"html_from_view": html}
        # print(html)

        return JsonResponse({'data':res}, safe=False)
    else:
        print('fuuuuuuuuu')
    return JsonResponse({})
def watch(request, movieid):
    request.encoding = 'utf-8'
    # mova = Movie.objects.get_or_create(title)
    if ('فيلم') in movieid:
        name = Movie.objects.get_or_create(movieid=movieid)
    else:
        name = Serie.objects.get_or_create(movieid=movieid)

    return render(request, 'base/watch.html' ,{'movie':name})
def moviesAr(request):
    movies_ar = Movie.objects.filter(label='افلام_عربي')
    return render(request, 'base/movies_ar.html', {'movies':movies_ar})
def moviesEn(request):
    movies_en = Movie.objects.filter(label='افلام_اجنبي')
    return render(request, 'base/movies_en.html', {'movies':movies_en})
def bol(request):
    bol = Movie.objects.filter(label='بوليوود')
    return render(request, 'base/movies_en.html', {'movies':bol})

def serie(request, movieid):
    sers = Espo.objects.all()
    ser = Espo.objects.all().filter(serie_id=movieid)
    # print(str(sera))
    # ser = Espo.objects.get_or_create(title=str(sera))
    return render(request, 'base/series.html', {'serie':ser, 'sers':sers})
def series(request):
    ser = Serie.objects.all()
    # print(str(sera))
    # ser = Espo.objects.get_or_create(title=str(sera))
    return render(request, 'base/series.html', {'ser':ser})
def view(request, movieid):
    request.encoding = 'utf-8'
    if ('فيلم') in movieid:
        name = Movie.objects.get(movieid=movieid)
    else:
        name = Serie.objects.get(movieid=movieid, season=season, numbera=numbera)
        # print(name[-1])
    return render(request, 'base/view.html',{'movie':name})
def viewser(request, movieid, season,numbera):
    request.encoding = 'utf-8'
    if ('فيلم') in movieid:
        name = Movie.objects.get(movieid=movieid)
    else:
        # movieid = Serie.objects.all().filter(movieid=movieid)
        sera = Serie.objects.get(movieid=movieid)
        espo = Espo.objects.all().filter(serie_id=movieid, season=season, numbera=numbera)
        espose = Espo.objects.all().filter(serie_id=movieid, season=season)
    return render(request, 'base/view.html',{'movie':sera, 'espo':espo,'espas':espose})
def viewsers(request,movieid,season):
    request.encoding = 'utf-8'
    if ('فيلم') in movieid:
        name = Movie.objects.get(movieid=movieid)
    else:
        # movieid = Serie.objects.all().filter(movieid=movieid)
        sera = Serie.objects.get(movieid=movieid)
        espo = Espo.objects.all().filter(serie_id=movieid, season=season)
        espose = Espo.objects.all().filter(serie_id=movieid, season=season)
    return render(request, 'base/view.html',{'movie':sera, 'espo':espo,'espas':espose})
class Geners(ListView):
    template_name = 'base/series.html'
    def get_queryset(self):
        self.category = self.kwargs['category']
        return Serie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(Geners, self).get_context_data(**kwargs)
        context["seras"] = self.category
        return context
class Label(ListView):
    template_name = 'base/series.html'
    def get_queryset(self):
        self.category = self.kwargs['label']
        if 'مسلسلات' in self.kwargs['label']:
            print(self.kwargs['label'])
            return Serie.objects.filter(label=self.category)
        elif 'افلام' in self.kwargs['label']:
            return Movie.objects.filter(label=self.category)

    def get_context_data(self, **kwargs):
        context = super(Label, self).get_context_data(**kwargs)
        context["seras"] = self.category
        return context

    # sera = Serie.objects.filter(category='comedy')
    # # name = Movie.objects.all().filter(category=category)
    # # print(name)
    # return render(request, 'base/series.html', {'seras':sera})