
class Group:

    def __init__(self):
        self.objectClass= ['posixGroup']
        #required
        self.cn = ''
        self.gidNoumber = ''
        #optional
        self.userPassword = ''
        self.memberUid = ''
        self.description = ''

__version__ = '0.01'
