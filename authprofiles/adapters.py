
from allauth.account.adapter import DefaultAccountAdapter



class PassportAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=true):
        print("FooAppAccountAdapter.save_user")

        return super(PassportAccountAdapter, self).save_user(
            request, user, form, commit
        )