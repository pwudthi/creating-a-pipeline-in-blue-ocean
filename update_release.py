import sys
import getopt
import json

def update_release(argv):
    arg_service = ""
    arg_release = ""
    arg_branch = ""
    arg_help = "{0} -s <service> -r <release> -b <branch>".format(argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hs:r:b:", ["help", "service=",
        "release=", "branch="])
    except:
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)
            sys.exit(2)
        elif opt in ("-s", "--service"):
            arg_service = arg
        elif opt in ("-r", "--release"):
            arg_release = arg
        elif opt in ("-b", "--branch"):
            arg_branch = arg

    print('service:', arg_service)
    print('release:', arg_release)
    print('branch:', arg_branch)

    service_found = False
    release_found = False

    with open("services.json", "r+") as jsonFile:
        jsondata = json.load(jsonFile)
        for service in jsondata["services"]:
            if service["name"] == arg_service:
                service_found = True
                for release in service["releases"]:
                    if release["release"] == arg_release:
                        release_found = True
                        release["branch"] = arg_branch

                if release_found == False:
                    service["releases"].append({ "release": arg_release, "branch": arg_branch })

        if service_found == False:
            jsondata["services"].append({ "name": arg_service, "releases": [ { "release": arg_release, "branch": arg_branch } ] })

        jsonFile.seek(0)
        json.dump(jsondata, jsonFile, indent=4, sort_keys=True)
        jsonFile.truncate()

if __name__ == "__main__":
    update_release(sys.argv)
