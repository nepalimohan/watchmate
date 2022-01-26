from rest_framework import permissions

class AdminorReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        # admin_permission = super().has_permission(request, view)  
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
    
#safe_methods - GET method
class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user