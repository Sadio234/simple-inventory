from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()


class BlogPost(models.Model):
    caisse = models.CharField(max_length=255, verbose_name='Caisse')
    slug = models.SlugField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now=True)
    description_pannes = models.TextField(blank=True, verbose_name='Description des pannes')
    intervention = models.TextField(blank=True, verbose_name='Interventions')
    design_refer = models.TextField(blank=True, verbose_name='Designations et References')
    quantity = models.IntegerField(verbose_name='Quantite')
    agent_dsi = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fonction = models.CharField(max_length=255, verbose_name='Fonction', db_column='function_1')
    agent = models.CharField(max_length=255, verbose_name='Agent')
    Fonct = models.CharField(max_length=255, verbose_name='Fonction', db_column='function_2')

    class Meta:
        ordering = ['-date']
        verbose_name = 'DECHARGES DES SORTIES DES MATERIELS'

    def __str__(self):
        return self.design_refer

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.design_refer)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('app:update')

    def homepage_view(request):
        context = {
            "users": BlogPost.objects.agent_dsi(),
        }
        return render(request=request, template_name='app/blogpost_list3.html', context=context)


class BlogPost2(models.Model):
    caisse = models.CharField(max_length=255, verbose_name='Caisse')
    slug = models.SlugField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now=True)
    description_pannes = models.TextField(blank=True, verbose_name='Description des pannes')
    intervention = models.TextField(blank=True, verbose_name='Interventions')
    design_refer = models.TextField(blank=True, verbose_name='Designations et References')
    quantity = models.IntegerField(verbose_name='Quantite')
    agent_dsi = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fonction = models.CharField(max_length=255, verbose_name='Fonction', db_column='function_3')
    agent = models.CharField(max_length=255, verbose_name='Agent')
    Fonct = models.CharField(max_length=255, verbose_name='Fonction', db_column='function_4')

    class Meta:
        ordering = ['-date']
        verbose_name = 'DECHARGES DES ENTREES DES MATERIELS'

    def __str__(self):
        return self.design_refer

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.design_refer)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('app:det')

