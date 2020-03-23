from django.contrib import messages

# Use standart login and logout
from django.contrib.auth import authenticate, login, logout

# Import our need Mixin for auth
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect  # Redirect
from django.shortcuts import render, redirect  # Basis Render for html
from django.urls import reverse_lazy
# Import basis Viev
from django.views.generic import CreateView, FormView, ListView, DeleteView, TemplateView, View, UpdateView

# Import all our form
from app.forms import RegistrationForm, LoginForm, ProductForm, PurchaseForm
# Import our models
from app.models import Customer, Product, Purchase


# Check for super user
class SuperuserTestMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_superuser:
            return True


#--------------------- Main index-------------------------------#
class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'param_a': 'Guns Shop'})
        return context


#------------------ User Manegment -----------------------------#
class Registration(CreateView):
    form_class = RegistrationForm # Use basis reg form
    template_name = 'registration.html'
    success_url = '/' # If all good send users to /


class Login(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return redirect('/')


class Logout(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect("/")


#--------------------- Purchase section --------------------------------#

#---- list of Products


class ProductListView(ListView):
    model = Product # Use model with our products
    paginate_by = 5 # per list show only 5
    template_name = 'products_list.html'
    queryset = Product.objects.all() # Select all
    ordering = ['title'] # Sort by name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'purchase_form': PurchaseForm,})
        return  context

#--- Product CRUD


class ProductCreateView(SuperuserTestMixin, CreateView):
    model =  Product
    template_name = 'product_create.html'
    form_class =  ProductForm
    success_url =  reverse_lazy('product_create')


class ProductUpdateView(SuperuserTestMixin, CreateView):
    model =  Product # Use model with our products
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')
    fields = ['picture', 'title', 'text', 'price', 'quantity']
    # Show in this order this product fields

# --- Purchase Section


class PurchaseCreateView(LoginRequiredMixin, CreateView):
    http_method_names = ['post', ]
    success_url = reverse_lazy('products_list')
    model = Purchase
    form_class = PurchaseForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.customer = self.request.user
        obj.product = Product.objects.get(pk=self.request.POST.get("product", ""))
        if not obj.check_cnt_available:
            messages.warning(self.request, "Entered quantity of product isn't present in the shop!")
            return HttpResponseRedirect('../products_list')
        if obj.money_not_enough:
            messages.warning(self.request, "You haven't enough money!")
            return HttpResponseRedirect('../products_list')
        obj.customer.from_wallet(obj.cnt*obj.product.price)
        obj.product.minus_prod(obj.cnt)
        self.object = obj.save()
        return super().form_valid(form)


class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    paginate_by = 10 # show only 10
    template_name = 'basket.html'
    queryset = Purchase.objects.all()
    ordering = ['-create_at'] # Sort by created at

    def get_queryset(self):
        return Purchase.objects.filter(customer=self.request.user, returned=False)


class PurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Purchase
    success_url =  reverse_lazy('basket')
    http_method_names = ['post']
    fields = ['to_return']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.to_return = True
        self.object = obj.save()
        return  super().form_valid(form)


class PurchaseReturnListView(SuperuserTestMixin, ListView):
    model = Purchase
    paginate_by = 6
    template_name = 'purchase_return.html'
    queryset = Purchase.objects.all()
    ordering = ['-create_at']

    def get_queryset(self):
        return Purchase.objects.filter(to_return=True, returned=False)


class PurchaseReturnUpdateView(SuperuserTestMixin, UpdateView):
    model = Purchase
    success_url = reverse_lazy('purchase_return')
    http_method_names = ['post', ]
    fields = ['returned', 'product', 'customer']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.returned = True
        obj.product = Product.objects.get(pk=self.request.POST.get("product", ""))
        obj.product.plus_prod(obj.cnt)
        obj.customer = Customer.objects.get(pk=self.request.POST.get("customer", ''))
        obj.customer.to_wallet(obj.cnt*obj.product.price)
        self.object = obj.save()
        return super().form_valid(form)


class PurchaseReturnedListView(SuperuserTestMixin, ListView):
    model = Purchase
    paginate_by = 6
    template_name = 'purchase_deleted.html'
    queryset = Purchase.objects.all()
    ordering = ['-create_at']

    def get_queryset(self):
        return Purchase.objects.filter(returned=True)
