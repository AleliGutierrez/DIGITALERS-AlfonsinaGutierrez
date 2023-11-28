from user_manager.models import Profile
from catalog.forms import SearchForm


def search_form(request):
    return {'search_form': SearchForm()}



def avatar(request):
    avatar = None

    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            avatar = profile.avatar.url
        except Profile.DoesNotExist:
            pass

    return {'avatar': avatar}

