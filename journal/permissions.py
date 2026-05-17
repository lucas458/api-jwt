from rest_framework import permissions

class IsOwnerOrEditorReadOnly(permissions.BasePermission):
    """
    Permite acesso total ao dono do objeto.
    Permite leitura a membros do grupo Editor.
    """
    
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        
        if request.method in permissions.SAFE_METHODS:
            return request.user.groups.filter(name='Editor').exists()
            
        return False
