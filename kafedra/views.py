# -*-coding:utf8-*-
import os
from django.shortcuts import render_to_response
from kafedra.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.db.models import Q


def home(request):
    home = True
    home_c = Content.objects.get(page='home')
    news_list = News.objects.all()[:5]
    return render_to_response("base.html", {'home': home, 'home_c': home_c, 'news_list': news_list})


def directions(request):
    dir = True
    pmi = True
    pmi_c = Content.objects.get(page='pmi')
    return render_to_response("pmi.html", {'dir': dir, 'pmi': pmi, 'pmi_c': pmi_c})


def events(request, event, year):
    ev = True
    if event == 'conf':
        conf = True
        events_c = Content.objects.get(page='conferences')
        conferences = Conference.objects.all()
        context = {'ev': ev, 'conf': conf, 'events_c': events_c, 'conferences': conferences}
    elif event == 'publ':
        publ = True
        events_c = Content.objects.get(page='publications')
        context = {}
        if year == '2013':
            year2013 = year
            public_m_2013 = Publication.objects.filter(section=u"Монографии", year=2013).values('names', 'work_name',
                                                                                                'publisher', 'volume',
                                                                                                'circulation')
            public_sr_2013 = Publication.objects.filter(section=u"Статьи в реферируемых ВАК изданиях",
                                                        year=2013).values('names', 'work_name', 'magazine',
                                                                          'edition_place', 'pages')
            public_st_2013 = Publication.objects.filter(section=u"Статьи и тезисы докладов", year=2013).values('names',
                                                                                                               'work_name',
                                                                                                               'magazine',
                                                                                                               'edition_place',
                                                                                                               'pages')
            context = {'year2013': year2013, 'public_m_2013': public_m_2013,
                       'public_sr_2013': public_sr_2013, 'public_st_2013': public_st_2013}
        elif year == '2012':
            year2012 = year
            public_sr_2012 = Publication.objects.filter(section=u"Статьи в реферируемых ВАК изданиях",
                                                        year=2012).values('names', 'work_name', 'magazine',
                                                                          'edition_place', 'pages')
            public_st_2012 = Publication.objects.filter(section=u"Статьи и тезисы докладов", year=2012).values('names',
                                                                                                               'work_name',
                                                                                                               'magazine',
                                                                                                               'edition_place',
                                                                                                               'pages')
            context = {'year2012': year2012,
                       'public_sr_2012': public_sr_2012, 'public_st_2012': public_st_2012}
        context.update({'ev': ev, 'publ': publ, 'events_c': events_c})
    return render_to_response("events.html", context)


def studentam(request, studentam):
    stud = True

    if studentam == 'rasp':
        rasp = True
        page = 'raspisanie'
        context = {'rasp': rasp}
    elif studentam == 'kurs':
        kurs = True
        page = 'kursovye'
        context = {'kurs': kurs}
    elif studentam == 'dipl':
        dipl = True
        page = 'diplomnye'
        context = {'dipl': dipl}

    stud_c = Content.objects.get(page=page)
    context.update({'stud': stud, 'stud_c': stud_c})
    return render_to_response("studentam.html", context)


def laboratories(request, laboratory):
    lab = True

    if laboratory == 'innov':
        innov = True
        page = 'innovations'
        context = {'innov': innov}
    elif laboratory == 'cisco':
        cisco = True
        page = 'cisco'
        context = {'cisco': cisco}

    lab_c = Content.objects.get(page=page)
    context.update({'lab': lab, 'lab_c': lab_c})
    return render_to_response("laboratories.html", context)


def contacts(request):
    contact = True
    contacts_c = Content.objects.get(page='contacts')
    return render_to_response("contacts.html", {'contact': contact, 'contacts_c': contacts_c})


def collective(request):
    about = True
    col = True
    col_c = Content.objects.get(page='collective')
    col_list = Collective.objects.all()
    paginator = Paginator(col_list, 10)
    page = request.GET.get('page')
    try:
        collective = paginator.page(page)
    except PageNotAnInteger:
        collective = paginator.page(1)
    except EmptyPage:
        collective = paginator.page(paginator.num_pages)
    return render_to_response("collective.html", {'about': about, 'col': col, 'col_c': col_c, 'col_list': col_list,
                                                  'collective': collective})


def news(request, news_id):
    about = True
    news = True
    if not news_id:
        news_c = Content.objects.get(page='news')
        news_list = News.objects.all()
        paginator = Paginator(news_list, 5)
        page = request.GET.get('page')
        try:
            news_l = paginator.page(page)
        except PageNotAnInteger:
            news_l = paginator.page(1)
        except EmptyPage:
            news_l = paginator.page(paginator.num_pages)
        context = {'news_c': news_c, 'news_l': news_l}
    elif news_id:
        try:
            news_id = int(news_id)
        except ValueError:
            raise Http404
        news_t = News.objects.get(id=news_id)
        context = {'news_t': news_t}
    context.update({'about': about, 'news': news})
    return render_to_response("news.html", context)


def info(request):
    about = True
    info = True
    info_c = Content.objects.get(page='info')
    return render_to_response("info.html", {'about': about, 'info': info, 'info_c': info_c})


def sitemap(request):
    sitemap = True
    sitemap_c = Content.objects.get(page='sitemap')
    return render_to_response("sitemap.html", {'sitemap': sitemap, 'sitemap_c': sitemap_c})


def search(request):
    context = {}

    if 'search' in request.GET:
        search = request.GET['search']
        context = {'search': search}
        if not search:
            error = 'Вы не ввели поисковый запрос'
            context.update({'error': error})
        else:
            content = Content.objects.filter(Q(title__icontains=search) | Q(text__icontains=search)).exclude(
                page="sitemap").values('title', 'text', 'url')
            context.update({'content': content})
            news_s = News.objects.filter(Q(title__icontains=search) | (Q(text__icontains=search))).values('id', 'title',
                                                                                                        'text')
            context.update({'news_s': news_s})
            conferences = Conference.objects.filter(desc__icontains=search).values('desc')
            context.update({'conferences': conferences})
            publications = Publication.objects.filter(Q(section__icontains=search) | Q(work_name__icontains=search)).values(
                                                                                                        'section', 'work_name', 'year')
            context.update({'publications': publications})
            collective = Collective.objects.filter(Q(name__icontains=search) | Q(position__icontains=search))
            context.update({'collective': collective})

            if not content and not news_s and not conferences and not publications and not collective:
                error = 'По вашему запросу ничего не найдено'
                context.update({'error': error})
            else:
                result = content.count() + news_s.count() + conferences.count() + publications.count() + collective.count()
                context.update({'result': result})

    return render_to_response("search.html", context)


def gallery(request):
    gallery_c = Content.objects.get(page='gallery')
    path_f = os.path.join(os.path.dirname(__file__), 'static/kafedra/gallery/img/small').replace('\\','/')
    files = os.listdir(path_f)
    return render_to_response("gallery.html", {'gallery_c': gallery_c, 'files': files})








