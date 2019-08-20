import requests


class NetworkAdapter:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_feed(self):
        host_link = r'http://{}:{}/get_json_images/'.format(self.host, self.port)
        try:
            return requests.get(host_link).json()
        except:
            return 'Network error'

    def login(self, login, password):
        pass

    def signup(self, login, email, password, password2):
        pass

    def get_user_profile(self, base64_token):
        pass

    def get_my_posts(self, base64_token):
        pass

    def get_my_followers(self, base64_token):
        pass

    def get_my_favorites(self, base64_token):
        pass

    def get_my_messages(self, base64_token):
        pass

    def send_email(self, base64_token, user_name):
        pass
