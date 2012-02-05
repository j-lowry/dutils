"""
A Unix-like user as defined in a the /etc/passwd file
"""

class User:

    def __init__(self):
        self.objectClass= ['inetOrgPerson', 'posixAccount', 'shadowAccount']
        "The following attributes MUST be defined for a posixAccount"
        self.cn = ''
        self.uid = '' #Also required for shadowAccount
        self.uidNumber = ''
        self.gidNumber = ''
        self.homeDirectory = ''
        #The following attributes are optional to define
        self.userPasswd = ''
        self.loginShell = ''
        self.gecos = ''
        #Optonal shadowAccount attributes
        self.shadowLastChange = ''
        self.shadowMin = ''
        self.shadowMax = ''
        self.shadowWarning = ''
        self.shadowInactive = ''
        self.shadowExpire = ''
        self.shadowFlag = ''
        self.description = ''
        #inetOrgPerson optional attibutes
        self.audio = ''
        self.businessCategory = ''
        self.carLicense = ''
        self.departmentNumber = ''
        self.displayName = ''
        self.employeeNumber = ''
        self.employeeType = ''
        self.givenName = ''
        self.homePhone = ''
        self.homePostalAddress = ''
        self.initials = ''
        self.jpegPhoto = '' 
        self.labeledURI = ''
        self.mail = ''
        self.manager = ''
        self.mobile = ''
        self.o = ''
        self.pager = ''
        self.photo = ''
        self.roomNumber = ''
        self.secretary = ''
        self.userCertificate = ''
        self.x500uniqueIdentifier = ''
        self.preferredLanguage = ''
        self.userSMIMECertificate = ''
        self.userPKCS12 = ''


    
#def getNextUID:

__version__ = '0.01'
