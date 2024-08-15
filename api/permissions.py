from rest_framework import permissions

class isAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:

            return True
        else:
            return request.user.is_superuser
        
class isOwnerorAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.method not in permissions.SAFE_METHODS:

            return request.user==obj.user
        
        else:

            if request.user==obj.user:

                return True
            
            else:

                return request.user.is_superuser