from django.apps import AppConfig


class EmailSenderConfig(AppConfig):
    name = 'email_sender'
    def ready(self):
        import email_sender.signals
