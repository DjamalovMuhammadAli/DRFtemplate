# env Modules
from rest_framework import permissions
from rest_framework.permissions import BasePermission
from django.conf.global_settings import PASSWORD_HASHERS


class IsAdminOrReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True

    return bool(request.user and request.user.is_staff)


class IsUserOrReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    return super().has_permission(request, view)
 

class IsDevise(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    return super().has_object_permission(request, view, obj)



# class EmployeeOnly(BasePermission):
#   def has_permission(self, request, view):
#     return request.user.is_authenticated and hasattr(request.user, "employee")

# class CompanyManagerOnly(BasePermission):
#   def has_permission(self, request, view):
#     return (
#       request.user.is_authenticated
#       and hasattr(request.user, "member")
#       and request.user.member.is_active
#       and request.user.member.is_manager
#     )


# class EmployeeAndCompanyManagerOnly(BasePermission):
#   def has_permission(self, request, view):
#     return request.user.is_authenticated and (
#       hasattr(request.user, "employee") 
#       or (
#         hasattr(request.user, "member")
#         and request.user.member.is_active
#         and request.user.member.is_manager
#       )
#     )



# class IsOwnerOrReadOnly(permissions.BasePermission):
#   """
#   Object-level permission to only allow owners of an object to edit it.
#   Assumes the model instance has an `owner` attribute.
#   """

#   def has_object_permission(self, request, view, obj):
#     # Read permissions are allowed to any request,
#     # so we'll always allow GET, HEAD or OPTIONS requests.
#     if request.method in permissions.SAFE_METHODS:
#       return True

#     # Instance must have an attribute named `owner`.
#     return obj.owner == request.user
