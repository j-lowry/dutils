#!/usr/bin/env python
import getopt,sys


def main():
    try:
        opts,args = getopt.gnu_getopt(sys.argv[1:],
        "b:c:d:De:f:g:G:hk:K:lmMNop:rs:u",
        ["base-dir=","comment=","home=","defaults","expiredate=","inactive=","gid=","groups=","help","skel=","key=","no-log-init","create-home","no-user-group","non-unique","password=","system","shell=","uid=","user-group"])
    except getopt.GetoptError, err:
    # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        #usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif o in ("-b", "--base-dir"):
            baseDir = o
        elif o in ("-c","--comment"):
            comment = o
        elif o in ("-d","--home-dir"):
            homeDir = o
        elif o in ("-D", "--defaults"):
            defaults = True
        elif o in ("e", "expiredate"):
            expireDate = o
        elif o in ("-f", "--inactive"):
            inactive = o
        elif o in ("-g", "--gid"):
            gid = o
        elif o in ("-G", "--groups"):
            groups = 0
        elif o in ("-k", "--skel"):
            skel = o
        elif o in ("-K", "--key"):
            key = o
        elif o in ("-l", "--no-log-init"):
            log = False
        elif o in ("-m", "--create-home"):
            createHome = True
        elif o in ("-M", "--no-create-home"):
            createHome = False
        elif o in ("-N", "--no-user-group"):
            createUserGroup = False
        elif o in ("-o", "--non-unique"):
            nonUnique = False
        elif o in ("-p", "--password"):
            password = o
        elif o in ("-r", "--system"):
            system = True
        elif o in ("-u", "--uid"):
            uid = o
        elif o in ("-U", "--user-group"):
            createUserGroup = True
        else:
            usage()
            sys.exit(2)
    
def usage():
    print """Usage: duseradd [options] LOGIN

Options:
    -b, --base-dir BASE_DIR       base directory for the home directory of the new account
    -c, --comment COMMENT         GECOS field of the new account
    -d, --home-dir HOME_DIR       home directory of the new account
    -D, --defaults                print or change default useradd configuration
    -e, --expiredate EXPIRE_DATE  expiration date of the new account
    -f, --inactive INACTIVE       password inactivity period of the new account
    -g, --gid GROUP               name or ID of the primary group of the new account
    -G, --groups GROUPS           list of supplementary groups of the new account
    -h, --help                    display this help message and exit
    -k, --skel SKEL_DIR           use this alternative skeleton directory
    -K, --key KEY=VALUE           override /etc/login.defs defaults
    -l, --no-log-init             do not add the user to the lastlog and faillog databases
    -m, --create-home             create the user's home directory
    -M, --no-create-home          do not create the user's home directory
    -N, --no-user-group           do not create a group with the same name as the user
    -o, --non-unique              allow to create users with duplicate (non-unique) UID
    -p, --password PASSWORD       encrypted password of the new account
    -r, --system                  create a system account
    -s, --shell SHELL             login shell of the new account
    -u, --uid UID                 user ID of the new account
    -U, --user-group              create a group with the same name as the user"""

if __name__ == "__main__":
    main()

