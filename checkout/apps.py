from django.apps import AppConfig

# Lesson code used
class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
