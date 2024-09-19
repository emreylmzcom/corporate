from .models import Settings


def SettingList(request):
    setting = Settings.objects.first()
    return {
        'setting': setting
    }
    