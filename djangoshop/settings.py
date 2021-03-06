"""
Django settings for djangoshop project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'. 在项目内创建路径就像示例的这样，这里提供了初始路径
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! 密钥要保密
SECRET_KEY = '+a&@i=wsr6*4%4gye$=h#nc()w!b=kashh%$!fzw%v)0eqqq#y' 

# SECURITY WARNING: don't run with debug turned on in production! 发布生产时需要关闭调试模式
DEBUG = True
# 这里还可以设置允许的地址，当debug为False时，那允许的范围必须填写，如果想要全部访问直接写'*' 当debug开启这里为空的时候，那么只允许本地访问
ALLOWED_HOSTS = []


# Application definition 加载的应用列表

INSTALLED_APPS = [
    'django.contrib.admin',         # 后台管理
    'django.contrib.auth',          # 认证系统
    'django.contrib.contenttypes',  # 项目所有的model元数据
    'django.contrib.sessions',      # 会话功能可以标记当前访问的用户信息
    'django.contrib.messages',      # 消息提示功能
    'django.contrib.staticfiles',   # 查找静态资源路径
    # 自己的应用
    'index',
    'shopper',
    'showware',
]

# 中间件，用来处理django请求和响应的框架全局范围改变输入和输出
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',            # 安全中间件
    'django.contrib.sessions.middleware.SessionMiddleware',     # 会话中间件
    # 如果你只是想要用本地语言来运行Django,并且该语言的语言文件存在,只需要简单地设置 LANGUAGE_CODE 即可，如果要让每一个使用者各自指定语言偏好,就需要使用 LocaleMiddleware
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',                # 处理请求，规范化请求内容
    'django.middleware.csrf.CsrfViewMiddleware',                # 开启csrf防护
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 开启内置用户认证系统
    'django.contrib.messages.middleware.MessageMiddleware',     # 开启信息提示
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # 防止恶意程序单机劫持
]

# url的入口设置 告诉django从哪个文件来查找路由的配置信息，所谓路由也就是请求路径和处理方法的对应关系
ROOT_URLCONF = 'djangoshop.urls'

# 模板配置 配置模板的解析引擎，模板的存放路径，以及django的内置模板使用配置信息
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',   # 定义识别模板的引擎
        'DIRS': [os.path.join(BASE_DIR,'templates'),],                  # 定义去哪个路径下去寻找模板
        'APP_DIRS': True,                                               # 是否去app中去查找模板
        'OPTIONS': {                                                    # 用于填充在requestcontext上下文，也就是模板中的指令比如{% load static %}
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# wsgi配置 告诉django如何去启动wsgi的协议处理
WSGI_APPLICATION = 'djangoshop.wsgi.application'


# Database 数据库配置 默认支持的数据库是：postgresql，mysql（mariadb）,sqlite3,oracle 如果别的，那么需要插件，需要了在看
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoshop',
        'USER': 'root',
        'PASSWORD': 'Abcd_1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}


# Password validation 内置的密码认证功能配置
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization 国际化的一些配置设置网站语言，时区等一些配置
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) 静态资源路径的配置 一般都需要三个属性  STATIC_URL    STATICFILES_DIRS    STATIC_ROOT
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# 配置公共静态资源目录
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'common_static'),
)

# 配置静态文件统一目录
STATIC_ROOT=os.path.join(BASE_DIR,'allstatic')

# 增加媒体资源的路径配置 MEDIA_URL    MEDIA_ROOT
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')