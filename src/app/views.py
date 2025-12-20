from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator
from app.models import BlogPost, BlogPost2


class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'app'


class BlogHome1(ListView):
    model = BlogPost
    paginate_by = 6
    template_name = 'app/blogpost_list2.html'
    context_object_name = 'apps'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_objects'] = BlogPost.objects.count()
        context['num_users'] = User.objects.count()
        context['enters'] = BlogPost2.objects.count()
        context['total_inter'] = BlogPost.objects.values('intervention').distinct().count()
        return context


    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        context['total_inter'] = BlogPost.objects.values('intervention').distinct().count()
        return self.render_to_response(context)


    def render_to_response(self, context, **response_kwargs):
        context['enters'] = BlogPost2.objects.count()
        return super().render_to_response(context, **response_kwargs)


class BlogHome2(ListView):
    model = BlogPost2
    paginate_by = 6
    template_name = 'app/blogpost_list3.html'
    context_object_name = 'aps'

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['num_users'] = User.objects.count()
        #return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_objects'] = BlogPost2.objects.count()
        context['num_users'] = User.objects.count()
        return context

    extra_context = {}

    #def get_queryset(self):
        #queryset = super().get_queryset()
        #b = queryset.values('intervention').distinct().count() - 1
        #self.extra_context = {
            #'total_inter': b
        #}
        #return queryset

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        context['total_inter'] = BlogPost2.objects.values('intervention').distinct().count()
        return self.render_to_response(context)


    def render_to_response(self, context, **response_kwargs):
        context['out'] = BlogPost.objects.count()
        return super().render_to_response(context, **response_kwargs)



class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = 'app/blogpost_detail.html'
    context_object_name = 'asps'


class BlogPostView(DetailView):
    model = BlogPost2
    template_name = 'app/blogpost_view.html'
    context_object_name = 'asp'


@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost2
    template_name = 'app/blogpost_create.html'
    fields = ['caisse', 'description_pannes', 'intervention', 'design_refer', 'quantity', 'agent_dsi', 'fonction', 'agent', 'Fonct',]


class BlogPostDelete(DeleteView):
    model = BlogPost2
    success_url = reverse_lazy('app:det')


class BlogPostUpdate(UpdateView):
    model = BlogPost2
    template_name = 'app/blogpost_edit.html'
    fields = ['caisse', 'description_pannes', 'intervention', 'design_refer', 'quantity', 'agent_dsi', 'fonction', 'agent', 'Fonct', ]


@method_decorator(login_required, name='dispatch')
class BlogPostCreate1(CreateView):
    model = BlogPost
    template_name = 'app/blogpost_create1.html'
    fields = ['caisse', 'description_pannes', 'intervention', 'design_refer', 'quantity', 'agent_dsi', 'fonction', 'agent', 'Fonct',]


class BlogPostUpdate1(UpdateView):
    model = BlogPost
    template_name = 'app/blogpost_edit1.html'
    fields = ['caisse', 'description_pannes', 'intervention', 'design_refer', 'quantity', 'agent_dsi', 'fonction', 'agent', 'Fonct', ]


class BlogPostDelete1(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('app:update')


def admin_count(request):
    number_of_admins = User.objects.filter(is_staff=True, is_superuser=True).count()
    return render(request, 'admin_count.html', {'number_of_admins': number_of_admins})
