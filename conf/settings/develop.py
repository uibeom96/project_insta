from conf.settings.base_setting import *

with open("secret.json", "r", encoding="UTF-8") as file:
    secret_list = json.loads(file.read())

def get_secret_key(key, secret_list=secret_list):
    try:
        return secret_list[key]
    except KeyError:
       raise ImproperlyConfigured("{}의 키 오류 입니다. ".format(key))


SECRET_KEY = get_secret_key("secret_DJANGO")


DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     get_secret_key("secret_develop_NAME"),
        "USER":     get_secret_key("secret_develop_USER"),
        "PASSWORD": get_secret_key("secret_develop_PASSWORD"),
        "HOST":     get_secret_key("secret_develop_HOST"),
        "PORT":     get_secret_key("secret_develop_PORT"),
    }
}