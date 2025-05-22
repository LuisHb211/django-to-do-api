from rest_framework import permissions


# This class should verify if the user logged is the created/author of the object and return true or false
class IsOwner(permissions.BasePermission):
    # def has_object_permission(self, request, view, obj):
    #     return obj.author == request.user

    def has_permission(self, request, view):
        return super().has_permission(request, view)