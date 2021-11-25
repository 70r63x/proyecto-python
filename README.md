# proyecto-python
Proyecto de practica Python

#Comandos de ejecución

Microsoft Windows [Versión 10.0.19042.1237]
(c) Microsoft Corporation. Todos los derechos reservados.

C:\Users\57312>cd C:\U

C:\U>cd proyectos_django1

C:\U\proyectos_django1>dir
 El volumen de la unidad C es Windows
 El número de serie del volumen es: F451-FC4A

 Directorio de C:\U\proyectos_django1

23/11/2021  11:56 p. m.    <DIR>          .
23/11/2021  11:56 p. m.    <DIR>          ..
24/11/2021  12:01 a. m.    <DIR>          tutorial1
               0 archivos              0 bytes
               3 dirs  152.137.728.000 bytes libres

C:\U\proyectos_django1>django-admin startproject proyecto1

C:\U\proyectos_django1>cd proyecto1

C:\U\proyectos_django1\proyecto1>python manage.py startapp todo

C:\U\proyectos_django1\proyecto1>python manage.py makemigrations
Migrations for 'todo':
  todo\migrations\0001_initial.py
    - Create model Tarea

C:\U\proyectos_django1\proyecto1>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, todo
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying todo.0001_initial... OK

C:\U\proyectos_django1\proyecto1>python manage.py createsuperuser
Username (leave blank to use '57312'): tony
Email address:
Password: 123
Password (again): 123
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

C:\U\proyectos_django1\proyecto1>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 00:40:04
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[24/Nov/2021 00:42:04] "GET / HTTP/1.1" 200 10697
[24/Nov/2021 00:42:15] "GET /admin/ HTTP/1.1" 302 0
[24/Nov/2021 00:42:16] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2214
[24/Nov/2021 00:42:21] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[24/Nov/2021 00:42:21] "GET /admin/ HTTP/1.1" 200 3325
[24/Nov/2021 00:42:22] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 380
[24/Nov/2021 00:42:22] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[24/Nov/2021 00:42:22] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
C:\U\proyectos_django1\proyecto1\todo\admin.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 00:43:37
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[24/Nov/2021 00:43:53] "GET /admin/ HTTP/1.1" 200 3954
[24/Nov/2021 00:44:01] "GET /admin/todo/tarea/ HTTP/1.1" 200 4905
[24/Nov/2021 00:44:01] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[24/Nov/2021 00:44:01] "GET /static/admin/js/core.js HTTP/1.1" 200 5698
[24/Nov/2021 00:44:01] "GET /static/admin/js/actions.js HTTP/1.1" 200 7867
[24/Nov/2021 00:44:01] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[24/Nov/2021 00:44:01] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6874
[24/Nov/2021 00:44:01] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 5984
[24/Nov/2021 00:44:01] "GET /static/admin/js/urlify.js HTTP/1.1" 200 7902
[24/Nov/2021 00:44:01] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[24/Nov/2021 00:44:01] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 287630
[24/Nov/2021 00:44:01] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 232381
[24/Nov/2021 00:44:01] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[24/Nov/2021 00:44:03] "GET /admin/todo/tarea/add/ HTTP/1.1" 200 5584
[24/Nov/2021 00:44:04] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[24/Nov/2021 00:44:04] "GET /static/admin/css/forms.css HTTP/1.1" 200 8804
[24/Nov/2021 00:44:04] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 492
[24/Nov/2021 00:44:04] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
[24/Nov/2021 00:44:04] "GET /static/admin/css/widgets.css HTTP/1.1" 200 11097
[24/Nov/2021 00:44:11] "POST /admin/todo/tarea/add/ HTTP/1.1" 302 0
[24/Nov/2021 00:44:11] "GET /admin/todo/tarea/add/ HTTP/1.1" 200 5812
[24/Nov/2021 00:44:12] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[24/Nov/2021 00:44:12] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[24/Nov/2021 00:44:18] "POST /admin/todo/tarea/add/ HTTP/1.1" 302 0
[24/Nov/2021 00:44:18] "GET /admin/todo/tarea/add/ HTTP/1.1" 200 5812
[24/Nov/2021 00:44:18] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[24/Nov/2021 00:44:23] "POST /admin/todo/tarea/add/ HTTP/1.1" 302 0
[24/Nov/2021 00:44:23] "GET /admin/todo/tarea/add/ HTTP/1.1" 200 5812
[24/Nov/2021 00:44:23] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
C:\U\proyectos_django1\proyecto1\todo\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 00:47:18
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 00:51:14
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[24/Nov/2021 00:53:10] "GET / HTTP/1.1" 200 177
[24/Nov/2021 00:54:36] "GET / HTTP/1.1" 200 177
[24/Nov/2021 00:54:53] "GET / HTTP/1.1" 200 177
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 01:07:29
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[24/Nov/2021 01:07:33] "GET / HTTP/1.1" 200 291
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 01:30:27
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\U\proyectos_django1\proyecto1\todo\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 01:36:34
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\threading.py", line 1009, in _bootstrap_inner
    self.run()
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\threading.py", line 946, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\management\commands\runserver.py", line 118, in inner_run
    self.check(display_num_errors=True)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\management\base.py", line 419, in check
    all_issues = checks.run_checks(
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\checks\registry.py", line 76, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\checks\urls.py", line 13, in check_url_config
    return check_resolver(resolver)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\checks\urls.py", line 23, in check_resolver
    return check_method()
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\urls\resolvers.py", line 412, in check
    for pattern in self.url_patterns:
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\urls\resolvers.py", line 598, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\urls\resolvers.py", line 591, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\U\proyectos_django1\proyecto1\proyecto1\urls.py", line 22, in <module>
    path("", include("todo.urls")),
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\urls\conf.py", line 34, in include
    urlconf_module = import_module(urlconf_module)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\U\proyectos_django1\proyecto1\todo\urls.py", line 3, in <module>
    from . import views
  File "C:\U\proyectos_django1\proyecto1\todo\views.py", line 17
    return redirect('home')
IndentationError: unexpected indent
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 01:48:09
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[24/Nov/2021 01:48:13] "GET / HTTP/1.1" 200 127
[24/Nov/2021 01:48:24] "GET /agregar/ HTTP/1.1" 200 127
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 01:48:57
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[24/Nov/2021 01:50:22] "GET /agregar/ HTTP/1.1" 200 449
[24/Nov/2021 02:11:07] "POST /agregar/ HTTP/1.1" 200 465
[24/Nov/2021 02:11:12] "GET / HTTP/1.1" 200 339
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 02:12:05
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[24/Nov/2021 02:12:14] "GET /agregar/ HTTP/1.1" 200 449
[24/Nov/2021 02:12:26] "POST /agregar/ HTTP/1.1" 302 0
[24/Nov/2021 02:12:26] "GET / HTTP/1.1" 200 377
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 02:14:46
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\U\proyectos_django1\proyecto1\todo\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\threading.py", line 1009, in _bootstrap_inner
    self.run()
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\threading.py", line 946, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\management\commands\runserver.py", line 118, in inner_run
    self.check(display_num_errors=True)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\management\base.py", line 419, in check
    all_issues = checks.run_checks(
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\checks\registry.py", line 76, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\checks\urls.py", line 13, in check_url_config
    return check_resolver(resolver)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\checks\urls.py", line 23, in check_resolver
    return check_method()
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\urls\resolvers.py", line 412, in check
    for pattern in self.url_patterns:
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\urls\resolvers.py", line 598, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\urls\resolvers.py", line 591, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\U\proyectos_django1\proyecto1\proyecto1\urls.py", line 22, in <module>
    path("", include("todo.urls")),
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\urls\conf.py", line 34, in include
    urlconf_module = import_module(urlconf_module)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\U\proyectos_django1\proyecto1\todo\urls.py", line 8, in <module>
    path("eliminar/<int:tarea_id>/")
TypeError: _path() missing 1 required positional argument: 'view'
C:\U\proyectos_django1\proyecto1\todo\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 02:15:50
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\U\proyectos_django1\proyecto1\todo\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 02:15:54
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[24/Nov/2021 02:17:50] "GET / HTTP/1.1" 200 702
[24/Nov/2021 02:17:53] "GET /eliminar/5/ HTTP/1.1" 302 0
[24/Nov/2021 02:17:53] "GET / HTTP/1.1" 200 599
[24/Nov/2021 02:18:03] "GET /agregar/ HTTP/1.1" 200 449
[24/Nov/2021 02:18:09] "POST /agregar/ HTTP/1.1" 302 0
[24/Nov/2021 02:18:09] "GET / HTTP/1.1" 200 702
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 02:21:08
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 02:21:22
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 02:22:03
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 02:22:33
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\U\proyectos_django1\proyecto1\todo\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 02:23:27
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\U\proyectos_django1\proyecto1\todo\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 02:23:30
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[24/Nov/2021 02:24:53] "GET / HTTP/1.1" 200 1007
[24/Nov/2021 02:24:55] "GET /editar/6/ HTTP/1.1" 200 464
[24/Nov/2021 02:24:59] "POST /editar/6/ HTTP/1.1" 302 0
[24/Nov/2021 02:24:59] "GET / HTTP/1.1" 200 1007
[24/Nov/2021 02:25:01] "GET /editar/6/ HTTP/1.1" 200 464
[24/Nov/2021 02:25:05] "POST /editar/6/ HTTP/1.1" 302 0
[24/Nov/2021 02:25:05] "GET / HTTP/1.1" 200 1007
[24/Nov/2021 08:53:14] "GET / HTTP/1.1" 200 1007
[24/Nov/2021 08:56:36] "GET / HTTP/1.1" 200 2558
[24/Nov/2021 08:56:39] "GET / HTTP/1.1" 200 2558
[24/Nov/2021 08:56:55] "GET / HTTP/1.1" 200 2558
[24/Nov/2021 08:56:57] "GET / HTTP/1.1" 200 2558
[24/Nov/2021 09:38:32] "GET / HTTP/1.1" 200 2558
[24/Nov/2021 09:38:41] "GET / HTTP/1.1" 200 2558
[24/Nov/2021 10:12:45] "GET / HTTP/1.1" 200 3438
Internal Server Error: /
Traceback (most recent call last):
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\handlers\exception.py", line 47, in inner
    response = get_response(request)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\U\proyectos_django1\proyecto1\todo\views.py", line 10, in home
    return render(request, 'todo/home.html', context)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\shortcuts.py", line 19, in render
    content = loader.render_to_string(template_name, context, request, using=using)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\loader.py", line 62, in render_to_string
    return template.render(context, request)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\backends\django.py", line 61, in render
    return self.template.render(context)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\base.py", line 170, in render
    return self._render(context)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\base.py", line 162, in _render
    return self.nodelist.render(context)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\base.py", line 938, in render
    bit = node.render_annotated(context)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\base.py", line 905, in render_annotated
    return self.render(context)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\loader_tags.py", line 150, in render
    return compiled_parent._render(context)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\base.py", line 162, in _render
    return self.nodelist.render(context)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\base.py", line 938, in render
    bit = node.render_annotated(context)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\base.py", line 905, in render_annotated
    return self.render(context)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\template\defaulttags.py", line 446, in render
    url = reverse(view_name, args=args, kwargs=kwargs, current_app=current_app)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\urls\base.py", line 86, in reverse
    return resolver._reverse_with_prefix(view, prefix, *args, **kwargs)
  File "C:\Users\57312\AppData\Local\Programs\Python\Python310\lib\site-packages\django\urls\resolvers.py", line 694, in _reverse_with_prefix
    raise NoReverseMatch(msg)
django.urls.exceptions.NoReverseMatch: Reverse for 'editar' with no arguments not found. 1 pattern(s) tried: ['editar/(?P<tarea_id>[0-9]+)/$']
[24/Nov/2021 10:15:27] "GET / HTTP/1.1" 500 135212
[24/Nov/2021 10:16:18] "GET / HTTP/1.1" 200 3260
[24/Nov/2021 10:17:25] "GET / HTTP/1.1" 200 3464
[24/Nov/2021 10:22:50] "GET / HTTP/1.1" 200 3831
[24/Nov/2021 10:24:35] "GET / HTTP/1.1" 200 4146
C:\U\proyectos_django1\proyecto1\todo\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 10:27:01
Django version 3.2.9, using settings 'proyecto1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[24/Nov/2021 10:27:22] "GET / HTTP/1.1" 200 4542
[24/Nov/2021 10:27:33] "GET /agregar/ HTTP/1.1" 200 2962
[24/Nov/2021 10:27:37] "GET / HTTP/1.1" 200 4542
[24/Nov/2021 10:27:39] "GET /editar/1/ HTTP/1.1" 200 2977
[24/Nov/2021 10:27:42] "GET / HTTP/1.1" 200 4542
[24/Nov/2021 10:28:18] "GET / HTTP/1.1" 200 4554
[24/Nov/2021 10:31:59] "GET / HTTP/1.1" 200 4554
[24/Nov/2021 10:32:00] "GET /agregar/ HTTP/1.1" 200 3165
[24/Nov/2021 10:32:38] "GET /agregar/ HTTP/1.1" 200 3115
[24/Nov/2021 10:32:41] "GET / HTTP/1.1" 200 4554
[24/Nov/2021 10:32:43] "GET /editar/1/ HTTP/1.1" 200 2977
[24/Nov/2021 10:32:47] "GET / HTTP/1.1" 200 4554
[24/Nov/2021 10:33:28] "GET / HTTP/1.1" 200 4554
[24/Nov/2021 10:33:32] "GET /editar/6/ HTTP/1.1" 200 3130
[24/Nov/2021 10:33:35] "POST /editar/6/ HTTP/1.1" 302 0
[24/Nov/2021 10:33:35] "GET / HTTP/1.1" 200 4554
[24/Nov/2021 10:35:49] "GET /agregar/ HTTP/1.1" 200 3115
[24/Nov/2021 10:35:54] "POST /agregar/ HTTP/1.1" 302 0
[24/Nov/2021 10:35:54] "GET / HTTP/1.1" 200 4884
[24/Nov/2021 10:36:00] "GET /eliminar/7/ HTTP/1.1" 302 0
[24/Nov/2021 10:36:00] "GET / HTTP/1.1" 200 4554
[24/Nov/2021 10:36:03] "GET /editar/6/ HTTP/1.1" 200 3130
[24/Nov/2021 10:36:09] "POST /editar/6/ HTTP/1.1" 302 0
[24/Nov/2021 10:36:09] "GET / HTTP/1.1" 200 4554
[24/Nov/2021 10:45:04] "GET /admin/ HTTP/1.1" 200 4830
[24/Nov/2021 10:45:04] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[24/Nov/2021 10:45:04] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[24/Nov/2021 10:45:04] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[24/Nov/2021 10:45:04] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[24/Nov/2021 10:45:04] "GET /static/admin/css/dashboard.css HTTP/1.1" 304 0
[24/Nov/2021 10:45:04] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
[24/Nov/2021 10:45:04] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 304 0
[24/Nov/2021 10:45:04] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 304 0
[24/Nov/2021 10:45:04] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0
[24/Nov/2021 10:45:04] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 304 0
[24/Nov/2021 10:45:04] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0
[24/Nov/2021 10:53:50] "GET /admin/todo/ HTTP/1.1" 200 2719
[24/Nov/2021 10:53:53] "GET /admin/todo/tarea/ HTTP/1.1" 200 6864
[24/Nov/2021 10:53:53] "GET /static/admin/css/changelists.css HTTP/1.1" 304 0
[24/Nov/2021 10:53:53] "GET /static/admin/js/actions.js HTTP/1.1" 304 0
[24/Nov/2021 10:53:53] "GET /static/admin/js/urlify.js HTTP/1.1" 304 0
[24/Nov/2021 10:53:54] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 304 0
[24/Nov/2021 10:53:54] "GET /static/admin/js/jquery.init.js HTTP/1.1" 304 0
[24/Nov/2021 10:53:54] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[24/Nov/2021 10:53:54] "GET /static/admin/js/prepopulate.js HTTP/1.1" 304 0
[24/Nov/2021 10:53:54] "GET /static/admin/js/core.js HTTP/1.1" 304 0
[24/Nov/2021 10:53:54] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 304 0
[24/Nov/2021 10:53:54] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 304 0
[24/Nov/2021 10:53:54] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 304 0
[24/Nov/2021 10:54:46] "GET /admin/todo/ HTTP/1.1" 200 2719
[24/Nov/2021 10:54:52] "GET /admin/todo/tarea/ HTTP/1.1" 200 6864
[24/Nov/2021 10:54:52] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[24/Nov/2021 10:54:59] "GET /admin/todo/ HTTP/1.1" 200 2719
[24/Nov/2021 10:55:03] "GET /admin/ HTTP/1.1" 200 4830
[24/Nov/2021 11:27:52] "GET /admin/todo/tarea/ HTTP/1.1" 200 6864
[24/Nov/2021 11:27:52] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[24/Nov/2021 11:44:10] "GET / HTTP/1.1" 200 4559
[24/Nov/2021 11:46:22] "GET /agregar/ HTTP/1.1" 200 3120
[24/Nov/2021 11:46:31] "POST /agregar/ HTTP/1.1" 302 0
[24/Nov/2021 11:46:31] "GET / HTTP/1.1" 200 4889
[24/Nov/2021 11:46:34] "GET /editar/8/ HTTP/1.1" 200 3135
[24/Nov/2021 11:46:38] "POST /editar/8/ HTTP/1.1" 302 0
[24/Nov/2021 11:46:38] "GET / HTTP/1.1" 200 4889
[24/Nov/2021 11:46:41] "GET /eliminar/8/ HTTP/1.1" 302 0
[24/Nov/2021 11:46:41] "GET / HTTP/1.1" 200 4559
[24/Nov/2021 11:46:49] "GET /admin/ HTTP/1.1" 200 4830
[24/Nov/2021 11:46:51] "GET /admin/ HTTP/1.1" 200 4830
[24/Nov/2021 11:46:54] "GET /admin/todo/tarea/ HTTP/1.1" 200 6864
[24/Nov/2021 11:46:54] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
[24/Nov/2021 11:48:01] "GET /admin/todo/tarea/ HTTP/1.1" 200 6864
[24/Nov/2021 11:48:01] "GET /admin/jsi18n/ HTTP/1.1" 200 3195
