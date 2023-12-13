from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsCustomerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'customer'

class IsCourierUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'courier'

class IsCompanyUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'company')