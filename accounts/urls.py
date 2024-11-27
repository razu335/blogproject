from django.urls import path, reverse_lazy
from .views import SignupView, LoginView, LogoutView, IndexView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
 # パスワードリセットフォーム表示
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html',
        subject_template_name='accounts/mail_template/reset/subject.txt',
        email_template_name='accounts/mail_template/reset/message.txt',
        html_email_template_name='accounts/mail_template/reset/message.html',
        success_url='done/'  # 確実に正しいパスを指定
    ), name='password_reset'),

 # メール送信完了ページ
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    
# 確認URL（Djangoが生成するリンク用）
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'
    ), name='password_reset_confirm'),

 # 完了通知ページ
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),]
