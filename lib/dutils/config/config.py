import re,ConfigParser, ldap, os

config = ConfigParser.ConfigParser()
try:
    config.readfp(open(os.path.expanduser('~/.dutils/conf')))
except IOError:
###Create the file, close it, then read it###
    print "Creating config file."
    f = open(os.path.expanduser('~/.dutils/conf'),'w')
    f.close()
    config.readfp(open(os.path.expanduser('~/.dutils/conf')))
except ConfigParser.MissingSectionHeaderError:
    print "Error in conf file. Missing section header."


def set_URI():
    try:
    ###Get the first section in the conf file###
        uri = config.get('default', 'uri')
    except AttributeError:
        uri = ldap.OPT_URI 
    return uri

def set_BASE():
    try:
        base = config.get('default', 'base')
        return base
    except:
        print "Error: base is not configured."
        exit(1)
        
def set_BINDDN():
    try:
        binddn = config.get('default', 'binddn')
        return binddn
    except:
        print "Error: binddn is not configured."
        exit(1)

myconfig = {}
defFile = '/etc/login.defs'

f = open(defFile)
for line in f:
    line = str.strip(line)
    if re.match('(?!^#|^$)', line):
        myline = str.split(line)
        myconfig[myline[0]] = myline[1]

def getMaxUID():
    return myconfig['UID_MAX']

def getMailDIR():
    return myconfig['MAIL_DIR']

def getCHFN_RISTRICT():
    return myconfig['CHFN_RESTRICT']

def getCONSOLE_GROUPS():
    return myconfig['CONSOLE_GROUPS']

def getCREATE_HOME():
    """Returns Boolean. Indicate if a home directory should be created by default for\
 new users. 
Default is no."""
    try:
        myconfig['CREATE_HOME']
    except KeyError:
        myconfig['CREATE_HOME'] = False

    if myconfig['CREATE_HOME'] == 'no':
        return False
    elif myconfig['CREATE_HOME'] == False:
        return False
    elif myconfig['CREATE_HOME'] == 'yes':
        return True

def getDEFAULT_HOME():
    """Returns Boolean. Indicate if login is allowed if we cant cd to the home directory.
Default in no.
If set to yes, the user will login in the root (/) directory if it is not\
 possible to cd to her home directory."""
    try:
        myconfig['DEFAULT_HOME']
    except KeyError:
        myconfig['DEFAULT_HOME'] = False

    if myconfig['DEFAULT_HOME'] == 'no':
        return False
    elif myconfig['DEFAULT_HOME'] == False:
        return False
    elif myconfig['DEFAULT_HOME'] == 'yes':
        return True

def getENCRYPT_METHOD():
    """Returns String. This defines the system default encryption algorithm for encrypting\
 group passwords (if no algorithm are specified on the command line).
It can take one of these values:\

    -   DES (default)\

    -   MD5\

    -   SHA256\

    -   SHA512 """

    try:    
        myconfig['ENCRYPT_METHOD']
    except KeyError:
        myconfig['ENCRYPT_METHOD'] = ''

    if myconfig['ENCRYPT_METHOD'] == 'DES':
        return myconfig['ENCRYPT_METHOD']
    elif myconfig['ENCRYPT_METHOD'] == 'MD5':
        return myconfig['ENCRYPT_METHOD']
    elif myconfig['ENCRYPT_METHOD'] == 'SHA256':
        return myconfig['ENCRYPT_METHOD']
    elif myconfig['ENCRYPT_METHOD'] == 'SHA512':
        return myconfig['ENCRYPT_METHOD']
    else:
        return ''

def getENV_HZ():
    """Returns String. If set, it will be used to define the HZ environment variable when a user\
login. The value must be preceded by HZ=. A common value on Linux is HZ=100.
The HZ environment variable is only set when the user (the superuser) logs in\
with sulogin. """

    try:
        myconfig['ENV_HZ']
    except KeyError:
        myconfig['ENV_HZ'] = ''

    return myconfig['ENV_HZ']

def getENV_PATH():
    """Returns String. If set, it will be used to define the PATH environment\
 variable when a regular user login. The value can be preceded by PATH=, or a\
 colon separated list of paths (for example /bin:/usr/bin).
 The default value is PATH=/bin:/usr/bin."""

    try:
        myconfig['ENV_PATH']
    except KeyError:
        myconfig['ENV_PATH'] = ''
        
    return myconfig['ENV_PATH']

def getENV_SUPATH():
    """Returns String. If set, it will be used to define the PATH environment\
 variable when the superuser login. The value can be preceded by PATH=, or a\
 colon separated list of paths (for example /sbin:/bin:/usr/sbin:/usr/bin). 
The default value is PATH=/bin:/usr/bin.
"""

    try:
        myconfig['ENV_SUPATH']
    except KeyError:
        myconfig['ENV_SUPATH'] = ''

    return myconfig['ENV_SUPATH']

def getERASECHAR():
    """Returns Int. Terminal ERASE character (010 = backspace, 0177 = DEL).\
 The value can be prefixed "0" for an octal value, or "0x" for an hexadecimal\
 value."""

    try:
        myconfig['ERASECHAR']
    except KeyError:
        myconfig['ERASECHAR'] = '010'

    return int(myconfig['ERASECHAR'])

def getFAIL_DELAY():
    """Returns Int. Delay in seconds before being allowed another attempt\
 after a login failure."""

    try:
        myconfig['FAIL_DELAY']
    except KeyError:
        myconfig['FAIL_DELAY'] = '120'

    return int(myconfig['FAIL_DELAY'])

def getFAKE_SHELL():
    """Return String. If set, login will execute this shell instead of the\
 users shell specified in /etc/passwd."""

    try:
        myconfig['FAKE_SHELL']
    except KeyError:
        myconfig['FAKE_SHELL'] = '120'

    return myconfig['FAKE_SHELL']

def getGID_MAX():
    """Returns Int. Max of group IDs used for the creation of regular groups\
."""

    try:
        myconfig['GID_MAX']
    except KeyError:
        myconfig['GID_MAX'] = '120'

    return int(myconfig['GID_MAX'])

def getGID_MIN():
    """Returns Int. Min of group IDs used for the creation of regular groups\
."""

    try:
        myconfig['GID_MIN']
    except KeyError:
        myconfig['GID_MIN'] = '120'

    return int(myconfig['GID_MIN'])

def getHUSHLOGIN_FILE():
    """Returns String. If defined, this file can inhibit all the usual chatter\
 during the login sequence. If a full pathname is specified, then hushed mode\
 will be enabled if the users name or shell are found in the file. If not a\
 full pathname, then hushed mode will be enabled if the file exists in the\
 users home directory."""

    try:
        myconfig['HUSHLOGIN_FILE']
    except KeyError:
        myconfig['HUSHLOGIN_FILE'] = ''

    return myconfig['HUSHLOGIN_FILE']
