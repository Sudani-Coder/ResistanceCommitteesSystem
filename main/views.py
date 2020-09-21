from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from main.models import *

def index(request):
    """View function for home page of site."""

    try:
        User_Area = get_object_or_404(Profile)
        projects = Project.objects.filter(Area__Area_Name = User_Area.Area).order_by("-Created")[:5]
    
    except:
        projects = Project.objects.all().order_by("-Created")[:5]

    # Generate counts of some of the main objects
    num_areas = Area.objects.all().count()
    num_familys = Family.objects.all().count()
    num_projects = Project.objects.all().count()
    num_tasks = Task.objects.all().count()

    num_projects_completed = Project.objects.filter(Complete__exact="True").count()
    num_projects_not_completed = Project.objects.filter(Complete__exact="False").count()
    num_tasks_completed = Task.objects.filter(Complete__exact="True").count()
    num_tasks_not_completed = Task.objects.filter(Complete__exact="False").count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    template = "main/index.html"
    context = {
        "projects": projects,
        "num_areas": num_areas,
        "num_familys": num_familys,
        "num_projects": num_projects,
        "num_tasks": num_tasks,
        "num_projects_completed": num_projects_completed,
        "num_projects_not_completed": num_projects_not_completed,
        "num_tasks_completed": num_tasks_completed,
        "num_tasks_not_completed": num_tasks_not_completed,
        "num_visits": num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, template, context)

class AreaListView(generic.ListView):
    model = Area
    paginate_by = 10

class AreaDetailView(generic.DetailView):
    model = Area

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['area_familys'] = Family.objects.all().filter(Area = self.kwargs['pk']).count()
        context['area_projects'] = Project.objects.all().filter(Area = self.kwargs['pk']).count()
        return context

class FamilyListView(generic.ListView):
    model = Family
    paginate_by = 10

    def get_queryset(self):
        User_Area = get_object_or_404(Profile)
        return Family.objects.all().filter(Area__Area_Name = User_Area.Area)

class FamilyDetailView(generic.DetailView):
    model = Family

class FamilyCreateView(LoginRequiredMixin, generic.CreateView):
    model = Family
    fields = "__all__"

class FamilyUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Family
    fields = "__all__"

class FamilyDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Family
    success_url = reverse_lazy("family-list")

class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 10

    def get_queryset(self):
        User_Area = get_object_or_404(Profile)
        return Project.objects.all().filter(Area__Area_Name = User_Area.Area)

class ProjectDetailView(generic.DetailView):
    model = Project

class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = "__all__"

class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = "__all__"

class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("projects-list")

class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10
