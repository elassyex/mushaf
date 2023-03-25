from django.db import models
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField



LANG = (
    ('AR','arabic'),
    ('EN','english')
    )
STAT = (
    ('TOP RATED','TOP RATED'),
    ('MOST WATCHED','MOST WATCHED'),
    ('NEW','NEW')
)
CATE=(
    ('دراما','دراما'),
    ('اكشن','اكشن'),
    ('كوميدي','كوميدي'),
    ('رومانسي','رومانسي'),
    ('حربي','حربي'),
    ('تشويق','تشويق'),
    ('رعب','رعب'),
    ('خيال علمي','خيال علمي'),
    ('وثائقي','وثائقي'),
    ('واقعي','واقعي'),
)
LAB=(
    ('مسلسلات_عربي','مسلسلات عربي'),
    ('افلام_عربي','افلام عربي'),
    ('مسلسلات_عربي','مسلسلات اجنبي'),
    ('افلام_اجنبي','افلام اجنبي'),
    ('مسلسلات_تركي','مسلسلات تركي'),
    ('مسلسلات_كوري','مسلسلات كوري'),
    ('بوليوود','بوليوود'),
)
class Movie(models.Model):
    series = models.ManyToManyField("Serie", through='Aio')
    movieid = models.CharField(max_length=265,primary_key=True, unique=True)
    title = models.CharField(max_length=1500)
    year = models.CharField(max_length=4)
    lent = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    category = models.CharField(choices=CATE, max_length=100)
    watchl1 = models.CharField(max_length=1500, default='', null=True)
    watchl2 = models.CharField(max_length=1500, default='', null=True)
    watchl3 = models.CharField(max_length=1500, default='', null=True)
    watchl4 = models.CharField(max_length=1500, default='', null=True)
    made=models.CharField(choices=LANG, max_length=2)
    description = models.TextField(max_length=500, null=True)
    created = models.DateField(auto_now_add=True, null=True)
    label = models.CharField(max_length=100, choices=LAB)
    status=models.CharField(choices=STAT, max_length=100)
    poster=models.ImageField(upload_to='movies')
    country = CountryField(blank=True)
    def __str__(self):
        return self.movieid + '|' + self.title

    @staticmethod
    def get_name():
        return 'movie'
class Actor(models.Model):
    actorid = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=30)
    photo = models.URLField()

    def __str__(self):
        return self.actorid + '|' + self.name

    @staticmethod
    def get_name():
        return 'actor'

class Serie(models.Model):
    movieid = models.CharField(max_length=265,primary_key=True, unique=True)
    title = models.CharField(max_length=1500)
    year = models.CharField(max_length=4)
    lent = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    label = models.CharField(max_length=100, choices=LAB)
    description = models.TextField(max_length=500, null=True)
    views_count = models.IntegerField()
    category = models.CharField(choices=CATE, max_length=100)
    poster=models.ImageField(upload_to='series')
    country = CountryField(blank=True)
    made=models.CharField(choices=LANG, max_length=2)
    status=models.CharField(choices=STAT, max_length=100, blank=True)
    created = models.DateField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title
class Espo(models.Model):
    serie = models.ForeignKey(Serie, related_name='serie_espo', on_delete=models.CASCADE)
    title = models.CharField(max_length=1500)
    numbera = models.IntegerField(default=1)
    season = models.IntegerField(default=1)
    rate = models.IntegerField(default=0)
    watchl1 = models.CharField(max_length=1500, default='', null=True)
    watchl2 = models.CharField(max_length=1500, default='', null=True)
    watchl3 = models.CharField(max_length=1500, default='', null=True)
    watchl4 = models.CharField(max_length=1500, default='', null=True)
    created = models.DateField(auto_now_add=True, null=True)
    

    def __str__(self):
        return (str(self.numbera)+ ' | ' + self.title)
class Aio(models.Model):
    movies = models.ForeignKey("Movie", models.DO_NOTHING)
    series = models.ForeignKey("Serie", models.DO_NOTHING)
# class Esp(models.model):
#     seriename = models.ForeignKey("Serie", verbose_name=(""), on_delete=models.CASCADE)
#     title = models.CharField(max_length=1500)
#     watchl1 = models.CharField()
#     watchl2 = models.CharField()
#     watchl3 = models.CharField()
#     watchl4 = models.CharField()
