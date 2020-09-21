from django.urls import path
from main import views


urlpatterns = [
    path("", views.index, name = "index"),
    path("areas/", views.AreaListView.as_view(), name = "areas-list"),
    path("area/<int:pk>/", views.AreaDetailView.as_view(), name = "area-detail"),
    path("familys/", views.FamilyListView.as_view(), name = "family-list"),
    path("family/<str:pk>/", views.FamilyDetailView.as_view(), name = "family-detail"),
    path("family/create", views.FamilyCreateView.as_view(), name = "family-create"),
    path("family/<str:pk>/update", views.FamilyUpdateView.as_view(), name = "family-update"),
    path("family/<str:pk>/delete", views.FamilyDeleteView.as_view(), name = "family-delete"),
    path("projects/", views.ProjectListView.as_view(), name = "projects-list"),
    path("project/<int:pk>", views.ProjectDetailView.as_view(), name = "project-detail"),
    path("project/create/", views.ProjectCreateView.as_view(), name = "project-create"),
    path("project/<int:pk>/update/", views.ProjectUpdateView.as_view(), name = "project-update"),
    path("project/<int:pk>/delete/", views.ProjectDeleteView.as_view(), name = "project-delete"),
    path("tasks/", views.TaskListView.as_view(), name = "task-list")
]
