from allauth.account.adapter import DefaultAccountAdapter

class MemberAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.username = data.get('username')
        user.age = data.get('age')
        user.gender = data.get('gender')
        user.address = data.get('address')
        user.save()

        return user
