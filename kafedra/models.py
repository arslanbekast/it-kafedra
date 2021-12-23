# -*- coding:utf-8 -*-
from django.db import models


class Content(models.Model):
    page = models.CharField('Страница', max_length=30)
    title = models.CharField('Заголовок страницы', max_length=200)
    meta_d = models.CharField('Мета Описание', max_length=500, blank=True)
    meta_k = models.CharField('Ключевые слова', max_length=500, blank=True)
    text = models.TextField('Текст', blank=True)
    url = models.CharField('URL-адрес', max_length=100)

    def __unicode__(self):
        return self.page

    class Meta:
        db_table = 'content'
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'


class News(models.Model):
    title = models.CharField('Заголовок', max_length=300)
    meta_d = models.CharField('Мета описание', max_length=500)
    meta_k = models.CharField('Ключевые слова', max_length=500)
    text = models.TextField('Текст')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Collective(models.Model):
    image = models.CharField('Изображение', max_length=20)
    name = models.CharField('Ф.И.О.', max_length=100)
    position = models.CharField('Должность', max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'collective'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Коллектив'


class Conference(models.Model):
    name = models.CharField('Ф.И.О.', max_length=100)
    desc = models.CharField('Описание', max_length=500)
    place_date = models.CharField('Место и время проведения', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        db_table = 'conferences'
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'


class Publication(models.Model):
    SECTIONS = (
        (u"Монографии", u"Монографии"),
        (u"Статьи в реферируемых ВАК изданиях", u"Статьи в реферируемых ВАК изданиях"),
        (u"Статьи и тезисы докладов", u"Статьи и тезисы докладов"),
    )
    section = models.CharField('Раздел', max_length=200, choices=SECTIONS, default=u"Монографии")
    names = models.CharField('Ф.И.О', max_length=300)
    work_name = models.CharField('Название работы', max_length=500)
    publisher = models.CharField('Издательство', max_length=100, blank=True)
    volume = models.IntegerField('Объем в п.л.', max_length=4, blank=True, null=True)
    circulation = models.IntegerField('Тираж', max_length=6, blank=True, null=True)
    magazine = models.CharField('Журнал', max_length=300, blank=True)
    edition_place = models.CharField('Место издания', max_length=200, blank=True)
    pages = models.CharField('Страницы', max_length=20, blank=True)
    YEAR = (
        (2012, u"2012 г"),
        (2013, u"2013 г"),
        (2014, u"2014 г"),
    )
    year = models.IntegerField('Год', max_length=4, choices=YEAR, default=2012)

    def __unicode__(self):
        return self.work_name

    class Meta:
        ordering = ('-id',)
        db_table = 'publications'
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'