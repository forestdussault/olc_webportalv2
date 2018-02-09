from django.conf.urls import url
from . import views


urlpatterns = [

    # Index page
    url(r'^$', views.projects, name='projects'),

    # Individual project page
    url(r'^project/(?P<project_id>\d+)/$',
        views.project_detail, name="project_detail"),

    # Download genesippr data url
    url(r'^project/(?P<project_id>\d+)/genesippr_data$',
        views.download_genesippr_files, name="genesippr_data"),

    # Tables for the views.project_detail page
    url(r'^project/(?P<project_id>\d+)/project_table$',
        views.project_table, name="project_table"),

    # GenesipprV2 results tables
    url(r'^project/(?P<project_id>\d+)/genesippr_results_table$',
        views.genesippr_results_table, name="genesippr_results_table"),

    url(r'^project/(?P<project_id>\d+)/gdcs_results_table$',
        views.genesippr_results_table, name="gdcs_results_table$"),

    url(r'^project/(?P<project_id>\d+)/sixteens_results_table$',
        views.genesippr_results_table, name="sixteens_results_table$"),

    url(r'^project/(?P<project_id>\d+)/serosippr_results_table$',
        views.genesippr_results_table, name="serosippr_results_table$"),

    # PDF view of GenesipprV2 results
    # GenesipprV2 results tables
    url(r'^project/(?P<project_id>\d+)/genesippr_report$',
        views.genesippr_report, name="genesippr_report"),

    # Sendsketch results table
    url(r'^project/(?P<project_id>\d+)/sendsketch_results_table$',
        views.sendsketch_results_table, name="sendsketch_results_table"),

    # Overall job status
    url(r'^project/(?P<project_id>\d+)/job_status_table$',
        views.job_status_table, name="job_status_table"),
]
