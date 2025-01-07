from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.contrib import messages
from django.urls import reverse_lazy

from .models import IndexSlider, IndexVideo, About, Product, Category, WhyChooseUs, FAQ, Comment, Blog, Contact

from gallery.models import ImageGallery, VideoGallery

from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["slider"] = IndexSlider.objects.first()
        context["video"] = IndexVideo.objects.first()
        context["about"] = About.objects.first()
        context["products"] = Product.objects.all()[:4]
        context["categories"] = Category.objects.all()
        context["choose_section"] = WhyChooseUs.objects.first()
        context["faqs"] = FAQ.objects.all()
        context["comments"] = Comment.objects.all()
        context["blogs"] = Blog.objects.filter(is_main_page = True)[:2]
        return context
    
class BlogPageView(TemplateView):
    template_name = 'blogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all()
        return context
    
class BlogDetailPageView(DetailView):
    template_name = 'blog-detail.html'
    model = Blog
    context_object_name = "blog"
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetailPageView, self).get_context_data(**kwargs)
        context["last_blogs"] = Blog.objects.exclude(pk = self.get_object().pk).order_by("-created")[:4]
        return context
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()
        return context
    
class ShopPageView(ListView):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 16

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        queryset = Product.objects.all()
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset

class ProductDetailPageView(DetailView):
    template_name = 'product-detail.html'
    model = Product
    context_object_name = "product"
    
class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Mesajınız göndərildi!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryPageView(TemplateView):
    template_name = 'gallery.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["videos"] = VideoGallery.objects.all()
        context["images"] = ImageGallery.objects.all()
        return context