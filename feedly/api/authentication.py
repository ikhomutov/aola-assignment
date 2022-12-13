from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from feedly.core.models import SiteUser


class QueryAuthentication(BaseAuthentication):
    """Authenticate user based on a query parameter"""
    QUERY_PARAM_NAME = 'user_id'

    def authenticate(self, request):
        user_id = request.GET.get(self.QUERY_PARAM_NAME)

        if user_id is None:
            raise exceptions.AuthenticationFailed(
                'User ID is not provided in request'
            )

        try:
            user = SiteUser.objects.get(pk=int(user_id))
        except ValueError:
            raise exceptions.AuthenticationFailed('User ID is not valid')
        except SiteUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('No user found')

        return user, None
