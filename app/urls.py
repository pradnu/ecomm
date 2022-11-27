
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .form import LoginForm,MyPasswordChange,MyPasswordReset,MySetPassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base),
    path('',views.ProductView.as_view(),name='home'),
    #path('',views.home),
    path('productdetails/<int:pk>',views.ProductDetail.as_view(),name='product-details'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('cart/',views.show_cart,name='showcart'),
    path('buy/',views.buy_now,name='buy-now'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('orders/',views.orders,name='orders'),
    path('mobile/',views.mobile,name='mobile'),
    path('mobile/<slug:data>',views.mobile,name='mobiledata'),
    path('checkout/',views.checkout,name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form = LoginForm),
         name='login'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('paswordchange/',auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html',
         form_class=MyPasswordChange,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),
         name='passwordchangedone'),
    path('registration/',views.customerregistration.as_view(),name='customer-registration'),

    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordReset),
         name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPassword),
         name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),
         name='password_reset_complete')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
