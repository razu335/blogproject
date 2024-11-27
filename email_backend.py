import ssl
from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def _starttls(self):
        """
        Override the default _starttls method to use a custom SSLContext.
        """
        context = ssl.create_default_context()  # デフォルトのSSLコンテキストを作成
        self.connection.starttls(context=context)
