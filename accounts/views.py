from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom


class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "index.html"


class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:index")

def form_valid(self, form):
    response = super().form_valid(form)
    user = form.save()  # フォームのデータを保存してユーザーを作成
    login(self.request, user)  # 作成したユーザーでログイン
    return response


class LoginView(BaseLoginView):
    """ログイン用ビュー"""
    form_class = LoginFrom
    template_name = "accounts/login.html"


class LogoutView(BaseLogoutView):
    """ログアウト用ビュー"""
    next_page = reverse_lazy('blog_app:index')
    http_method_names = ["get", "post"]


class CustomPasswordResetForm(PasswordResetForm):
    """カスタムパスワードリセットフォーム"""
    def save(self, *args, **kwargs):
        # カスタムテンプレートを設定
        kwargs['subject_template_name'] = 'custom_templates/reset_subject.txt'
        kwargs['email_template_name'] = 'custom_templates/reset_email.txt'
        kwargs['html_email_template_name'] = 'custom_templates/reset_email.html'
        super().save(*args, **kwargs)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    subject_template_name = 'accounts/mail_template/reset/subject.txt'
    email_template_name = 'accounts/mail_template/reset/message.txt'
    html_email_template_name = 'accounts/mail_template/reset/message.html'
    success_url = reverse_lazy('accounts:password_reset_done')  # 名前空間付きに修正


class PasswordResetDone(PasswordResetDoneView):
    """パスワード変更用URLを送りましたページ"""
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    success_url = reverse_lazy('accounts:password_reset_complete')
    template_name = 'accounts/password_reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    """新パスワード設定しましたページ"""
    template_name = 'accounts/password_reset_complete.html'
