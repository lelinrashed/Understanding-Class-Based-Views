from dashboard.forms import BookForm
from dashboard.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.generic.edit import ModelFormMixin
# Create your views here.
from django.views.generic.base import TemplateResponseMixin, ContextMixin


# class MultipleObjectMixin(object):
#     def get_queryset(self, queryset=None, *args, **kwargs):
#         slug = self.kwargs.get("slug")
#         if slug:
#             try:
#                 obj = self.model.objects.get(slug=slug)
#             except self.model.MultipleObjectsReturned:
#                 obj = self.get_queryset().first()
#             except:
#                 obj = Http404
#             return obj
#         raise Http404


class BookCreateView(SuccessMessageMixin, CreateView):
    # model = Book
    template_name = "dashboard/form.html"
    # fields = ['title', 'description']
    form_class = BookForm
    success_message = "%(title)s created successfully %(created_at)s"

    def form_valid(self, form):
        print(form.instance)
        form.instance.added_by = self.request.user
        valid_form = super(BookCreateView, self).form_valid(form)
        # messages.success(self.request, "Book created successfully.")
        return valid_form

    def get_success_url(self):
        return reverse("book_list")

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            created_at=self.object.timestamp,
        )


# def book_detail(request, slug):
#     book = Book.objects.get(slug=slug)
#     return render()


class BookDetail(ModelFormMixin, DetailView):
    model = Book
    form_class = BookForm

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)


class BookListView(ListView):
    model = Book

    # def get_queryset(self, *args, **kwargs):
    #     qs = super(BookListView, self).get_queryset(*args, **kwargs)
    #     print(qs.first())
    #     return qs


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "dashboard/form.html"


class BookDeleteView(DeleteView):
    model = Book

    def get_success_url(self):
        return reverse("book_list")


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)


class DashboardTemplateView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'This is title'
        return context


class MyView(LoginRequiredMixin, ContextMixin, TemplateResponseMixin, View):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = 'Some other title'
        return self.render_to_response(context)

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(MyView, self).dispatch(request, *args, **kwargs)

