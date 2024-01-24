from .models import *
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from .forms import OrderReviewForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.

class OrderByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    fields = ['vehicle', 'return_due', 'order_status']
    success_url = '/autoservice/orders/'
    template_name = 'new_user_order.html'

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class OrderByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Order
    template_name = 'new_user_order.html'
    fields = ['vehicle', 'return_due', 'order_status']
    success_url = '/autoservice/orders/'

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.get_object().client == self.request.user


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)


def index(request):
    service_num = Service.objects.all().count()
    orders_done = Order.objects.filter(order_status__exact='co').count()
    vehicle_amount = Vehicle.objects.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'service_num': service_num,
        'orders_done': orders_done,
        'vehicle_amount': vehicle_amount,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


def vehicles(request):
    paginator = Paginator(Vehicle.objects.all(), 8)
    page_number = request.GET.get('page')
    paged_vehicles = paginator.get_page(page_number)
    context = {
        'vehicles': paged_vehicles
    }
    return render(request, 'vehicles.html', context=context)


def vehicle(request, vehicle_id):
    single_vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'vehicle.html', {'vehicle': single_vehicle, })


def services(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services.html', context=context)


def service(request, service_id):
    single_service = get_object_or_404(Service, pk=service_id)
    return render(request, 'service.html', {'service': single_service, })


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 2
    template_name = 'order_list.html'


class OrderDetailView(FormMixin, generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
    form_class = OrderReviewForm

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.order = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(OrderDetailView, self).form_valid(form)


def search(request):
    query = request.GET.get('query')
    search_results = Vehicle.objects.filter(
        Q(client__icontains=query) | Q(model__make__icontains=query) | Q(model__model__icontains=query) | Q(
            plate__icontains=query) | Q(vin__icontains=query))
    return render(request, 'search.html', {'vehicles': search_results, 'query': query})


class VehiclesByClientListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'my_orders.html'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} is taken!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with the following email: {email} already exists!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} registered!')
                    return redirect('login')
        else:
            messages.error(request, "Passwords don't match!")
            return redirect('register')
    return render(request, 'registration/register.html')