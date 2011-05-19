import re

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
    return myconfig['CREATE_HOME']

def getDEFAULT_HOME():
    return myconfig['DEFAULT_HOME']

def getENCRYPT_METHOD():
    return myconfig['ENCRYPT_METHOD']

def getENV_HZ():
    return myconfig['ENV_HZ']

def getENV_PATH():
    return myconfig['ENV_PATH']

def getENV_SUPATH():
    return myconfig['ENV_SUPATH']

def getERASECHAR():
    return myconfig['ERASECHAR'

def getFAIL_DELAY():
    return myconfig['FAIL_DELAY']

def getFAKE_SHELL():
    return myconfig['FAKE_SHELL']

def getGID_MAX():
    return myconfig['GID_MAX']

def getGID_MIN():
    return myconfig['GID_MIN']


