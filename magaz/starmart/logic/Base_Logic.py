class BaseLogic:
    @staticmethod
    def user_authenticated(request):
        if request.user.is_authenticated:
            user = request.user
        else:
            user = request.session.session_key
        return user
