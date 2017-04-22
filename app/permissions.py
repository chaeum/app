from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)
logger.error('test')

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner_id == request.user.id

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        logger.error(request.user)
        print request.user
        return obj.owner == request.user