from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Product, Comment
from .forms import CommentForm


class ProductsListView(generic.ListView):
    queryset = Product.objects.filter(availability=True)
    context_object_name = 'products'
    template_name = 'products/products_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'products/product_detail.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        pk = int(self.kwargs['pk'])
        product = get_object_or_404(Product, id=pk)
        obj.product = product
        return super().form_valid(form)
