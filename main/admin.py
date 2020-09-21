from django.contrib import admin
from main.models import *

class FamilyMemberAdmin(admin.ModelAdmin):
    list_filter = ["Age", "Gender"]
    list_display = ("Name", "Age", "Gender", "Relative_Relation", "Family")
    search_fields = ["Name"]

class ProfileAdmin(admin.ModelAdmin):
    list_filter = ["Area"]
    list_display = ("user", "Phone_Number", "Area")
    search_fields = ["user"]

class ProjectAdmin(admin.ModelAdmin):
    list_filter = ["Complete", "Created"]
    list_display = ("Title", "Description", "Complete", "Created", "Area")
    search_fields = ["Title"]

class AreaAdmin(admin.ModelAdmin):
    search_fields = ["Area_Name"]

class TaskAdmin(admin.ModelAdmin):
    list_filter = ["Complete", "Created"]
    list_display = ("Title", "Description", "Price", "Quantity", "Complete", "Created", "Family")
    search_fields = ["Title"]

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember
    extra = 1

class FamilyAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Family Member",
            {
                "fields": [
                    "Id_Number",
                    "Id_Type",
                    "Full_Name",
                    "Age",
                    "Place_Of_Birth",
                    "Gender",
                    "Social_Status",
                    "Education_Level",
                    "Job_Title",
                    "Phone_Number",
                    "Address",
                ]
            }
        ),
        (
            "Family Info",
            {
                "fields": [
                    "House_Number",
                    "Family_Members_Number",
                    "Area",
                ]
            }
        )
    ]
    inlines = [FamilyMemberInline, TaskInline]
    list_filter = ["Id_Type", "Social_Status", "Age", "Gender", "Family_Members_Number", "Area"]
    list_display = ("Full_Name", "Phone_Number", "Gender", "Address", "House_Number", "Family_Members_Number", "Area")
    search_fields = ["Full_Name"]

# Register your models here.
admin.site.register(Family, FamilyAdmin)
admin.site.register(FamilyMember, FamilyMemberAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile, ProfileAdmin)
