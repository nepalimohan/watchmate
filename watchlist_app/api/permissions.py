from rest_framework import permissions

class IsAdminorReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        # admin_permission = super().has_permission(request, view)  
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
    
#safe_methods - GET method
class IsReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff
            #only the admin or review_user has access to edit or delete the review