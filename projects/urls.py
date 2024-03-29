from django.urls import path
from .views import *


urlpatterns = [
    path("", projects, name="projects"),
    path("projects/", projects, name="projects"),
    path("projects/<uuid:id>", project, name="project"),
    path("project_add/", project_add, name="project_add"),
    path("project_edit/<uuid:id>", project_edit, name="project_edit"),
    path("project_delete/<uuid:id>", project_delete, name="project_delete"),
    path("add_comment/", add_comment, name="add_comment"),
    path("view_comments/", view_comments, name="view_comments"),

]