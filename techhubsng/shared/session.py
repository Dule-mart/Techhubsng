from django.contrib.auth import authenticate


class AuthModel:
       
    
    def check_session(self, session_id, user):

        login_check = authenticate(session_id)
        if login_check is not None:
            return True
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            return False