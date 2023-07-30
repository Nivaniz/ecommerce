from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserProfileForm, UserForm
from .models import Account, UserProfile
from orders.models import Order
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from carts.views import _cart_id
from carts.models import Cart, CartItem
import requests


# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]  # FALTA PHONE NUMBEEEEEEEEEEEEEEEER
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            profile = UserProfile()
            profile.user_id = user.id
            profile.profile_picture = 'default/default-user.png'
            profile.save()


            current_site = get_current_site(request)
            mail_subject = 'Activa tu cuenta en ByteShop para continuar'
            body = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode( force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()


            # messages.success(request, 'Te has registrado exitosamente')
            return redirect('/accounts/login/?command=verification&email='+email)



    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exist = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exist:
                    cart_item = CartItem.objects.filter(cart=cart)

                    product_variation = []

                    for item in cart_item:
                        variation = item.variation.all()  #variations en realidad
                        product_variation.append(list(variation))

                    cart_item = CartItem.objects.filter(user=user)
                    ex_var_list = []
                    id = []

                    for item in cart_item:
                        existing_variation = item.variation.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)

                    for pr in product_variation:
                        if pr in ex_var_list:
                            index = ex_var_list.index(pr)
                            item_id = id[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantity +=1
                            item.user = user
                            item.save()
                        else:
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()
            except:
                pass


            auth.login(request, user)
            messages.success(request, 'Has iniciado sesión exitosamente')

            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')

        else:
            messages.error(request, 'Los datos son incorrectos')
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Has salido de sesión')

    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Felicidades, tu cuenta está activa!')
        return redirect('login')
    else:
        messages.error(request, 'No se pudo completar la activación de la cuenta')
        return redirect('register')


@login_required(login_url='login')
def dashboard(request):

    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()

    userprofile = UserProfile.objects.get(user_id=request.user.id)

    context = {
        'orders_count': orders_count,
        'userprofile': userprofile,
    }


    return render(request, 'accounts/dashboard.html', context)


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            current_site = get_current_site(request)
            mail_subject = 'Recupera tu Contraseña'
            body = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()

            messages.success(request, 'Un email fue enviado a tu bandeja de entrada para recuperar tu contraseña')
            return redirect('login')
        else:
            messages.error(request, 'La cuenta de usuario no existe o surgió un problema')
            return redirect('forgotPassword')

    return render(request, 'accounts/forgotPassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user=None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Por favor escribe tu nueva contraseña')
        return redirect('resetPassword')
    else:
        messages.error(request, 'El link ha caducado')
        return redirect('login')


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'La contraseña se actualizó correctamente')
            return redirect('login')
        else:
            messages.error(request, 'La contraseña de confirmación no concuerda')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')


def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders': orders,
    }

    return render(request, 'accounts/my_orders.html', context)


@login_required(login_url='login')
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Su información fue guardada con exito')
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }

    return render(request, 'accounts/edit_profile.html', context)


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(username__exact=request.user.username)

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()

                messages.success(request, 'La contraseña se actualizó correctamente')
                return redirect('change_password')
            else:
                messages.error(request, 'Los datos no son válidos, ingresa una contraseña correcta')
                return redirect('change_password')
        else:
            messages.error(request, 'La contraseña no coincide con la confirmación')
            return redirect('change_password')

    return render(request, 'accounts/change_password.html')
