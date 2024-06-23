from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Custom permissions for UserViewSet to only allow users to edit their own profile. Otherwise, GET and POST only.
    """

    # only called for two API methods GET and POST
    def has_permission(self, request, view):
        return True
    
    # only called when has_permission True, if false -> never called
    # relates to specific instance of an object - e.g. user/1, user/2 etc.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user == obj
        
        return False