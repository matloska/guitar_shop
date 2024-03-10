from django.contrib.auth.mixins import UserPassesTestMixin

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        return self.request.user.is_superuser