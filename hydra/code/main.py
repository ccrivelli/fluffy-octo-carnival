from securitycenter import SecurityCenter5
import  getpass
from netaddr import *


class SecurityCenterTool():
    
    def __init__(self):

        # credentials
        global hostname
        hostname = input("SecurityCenter Hostname (without 'https://'): ")
        global username
        username = input("Username: ")

        # hide password when typed
        global password
        password = getpass.getpass("Password: ")


    def login(self):

        print("Login to ", hostname)
        global sc
        sc = SecurityCenter5(hostname)
        sc.login(username, password)


    def getRepositoriesDump(self):

        print("Repository list:")
        response = sc.get('repository?type=All')
        print(response.json())
        for repo in response.json()['response']:
#            print(repo)
#            print(repo['id'])
            response2 = sc.get('repository/'+repo['id'])
            json_response2 = response2.json()
            print(" -- ")
            print(json_response2)
            repo_name = json_response2['response']['name']
            if 'ipRange' in json_response2['response']['typeFields']:
                repo_ip_range = response2.json()['response']['typeFields']['ipRange']
            print("Repo: " + repo_name)
            if 'ipRange' in json_response2['response']['typeFields']:
                repo_ip_range = response2.json()['response']['typeFields']['ipRange']
                print("IP Range: " + repo_ip_range)
                print("Write to file ..")
                filepath = "./files/repositories/" + repo_name + ".txt"
                print(filepath)
                f = open(filepath, 'w')
                for subnet in repo_ip_range.split(','):
                    f.write(subnet + '\n')
                f.close()

    def subnetListCompare(self):

        subnet_list_file = "./files/master_subnet_list.txt"

        # read file line by line without \n and save in a list
        with open(subnet_list_file) as f:
            subnet_strings = f.read().splitlines()

        # define an empty list 
        l = [] 
        
        # iter the string list and append to IPNetwork list
        for s in subnet_strings:
            subnet = IPNetwork(s)
            l.append(subnet)	 

        print("Master list .. ")
        print(l)



    def logout(self):

        sc.logout()  


if __name__ == '__main__':

    sct = SecurityCenterTool()
    sct.login()
    sct.getRepositoriesDump()
    sct.subnetListCompare()
    sct.logout()








