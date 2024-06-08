from rolepermissions.roles import AbstractUserRole




class CustomUser(AbstractUserRole):
    avaible_permissions = {'create_event': False}

class PrivilegedUser(AbstractUserRole):
    avaible_permissions = {'create_event': True}
