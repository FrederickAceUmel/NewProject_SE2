from django.urls import path
from . import views

app_name = 'ui'

urlpatterns = [
    path('alert', views.alert, name='alert'),
    path('avatar', views.avatar, name='avatar'),
    path('badge', views.badge, name='badge'),
    path('breadcrumb', views.breadcrumb, name='breadcrumb'),
    path('button', views.button, name='button'),
    path('card', views.card, name='card'),
    path('carousel', views.carousel, name='carousel'),
    path('checkbox', views.checkbox, name='checkbox'),
    path('collapse', views.collapse, name='collapse'),
    path('comments', views.comment, name='comment'),
    path('dashboard-base', views.dashboard_base, name='dashboard_base'),
    path('datepicker', views.datepicker, name='datepicker'),
    path('drawer', views.drawer, name='drawer'),
    path('drag-drop', views.drag_drop, name='drag_drop'),
    path('dropdown', views.dropdown, name='dropdown'),
    path('empty', views.empty, name='empty'),
    path('grid', views.grid, name='grid'),
    path('input', views.input, name='input'),
    path('list', views.list, name='list'),
    path('menu', views.menu, name='menu'),
    path('message', views.message, name='message'),
    path('modals', views.modals, name='modals'),
    path('notifications', views.notifications, name='notifications'),
    path('page-header', views.pageHeader, name='page_header'),
    path('paginations', views.paginations, name='paginations'),
    path('progress', views.progress, name='progress'),
    path('radio', views.radio, name='radio'),
    path('rate', views.rate, name='rate'),
    path('result', views.result, name='result'),
    path('select', views.select, name='select'),
    path('skeleton', views.skeleton, name='skeleton'),
    path('slider', views.slider, name='slider'),
    path('spinner', views.spinner, name='spinner'),
    path('statistic', views.statistic, name='statistic'),
    path('steps', views.steps, name='steps'),
    path('switch', views.switch, name='switch'),
    path('tabs', views.tabs, name='tabs'),
    path('tag', views.tag, name='tag'),
    path('timeline', views.timeline, name='timeline'),
    path('timeline2', views.timeline2, name='timeline2'),
    path('timeline3', views.timeline3, name='timeline3'),
    path('timepicker', views.timepicker, name='timepicker'),
    path('upload', views.upload, name='upload'),
]