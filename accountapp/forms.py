from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 아래 설정이 없으면 UserCreationForm과 AccountUpdateForm 는 똑같은 기능을 하게 된다.
        self.fields['username'].disabled = True