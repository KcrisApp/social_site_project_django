from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login

class StafMixing(UserPassesTestMixin):
    # Lo scopo di questo mixin e fare in modo che solo lo staff possa crear una sezione

    # def per rischriver redirect
    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())  
    
    # Se la funzione restituisce true il test passa
    def test_func(self):
        return self.request.user.is_staff