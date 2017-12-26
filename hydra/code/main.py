from securitycenter import SecurityCenter5
import  getpass
from netaddr import *
from os import listdir
import re
import string


class SecurityCenterTool():
    
    def __init__(self):
        pass
        # credentials
        #global hostname
        #hostname = input("SecurityCenter Hostname (without 'https://'): ")
        #global username
        #username = input("Username: ")

        # hide password when typed
        #global password
        #password = getpass.getpass("Password: ")


    def login(self):

        # credentials
        global hostname
        hostname = input("SecurityCenter Hostname (without 'https://'): ")
        global username
        username = input("Username: ")
        
        # hide password when typed
        global password
        password = getpass.getpass("Password: ")

        print("Login to ", hostname)
        global sc
        sc = SecurityCenter5(hostname)
        sc.login(username, password)
        print(" ")

    def exportRepositories(self):

        print("++ Export Repositories into files ++")
        response = sc.get('repository?type=All')
        #print(response.json())
        for repo in response.json()['response']:
            #print(repo)
            #print(repo['id'])
            response2 = sc.get('repository/'+repo['id'])
            json_response2 = response2.json()
            #print(" -- ")
            #print(json_response2)
            repo_name = json_response2['response']['name']
            print("Name: " + repo_name)
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
            print(" ")
        print(" ")


    def fileToIPNetworkList(self, file):

        ''' 
        import a txt containing a list of subnets into a list of IPNetwork
        '''

        #subnet_list_file = "./files/master_subnet_list.txt"

        # read file line by line without \n and save in a list
        with open(file) as f:
            subnet_strings = f.read().splitlines()
            print(subnet_strings)

        # search for IP Ranges like 10.1.2.0-10.1.5.255 and create a new list of subnets with no IP ranges
        l = []
        
        for iprange in subnet_strings:
            if re.search('(?<=-)\w+',iprange):
                print("Found!! >> " + iprange)
                x_subnet = iprange.split('-')
                print(x_subnet)
                #cidr_subnet = IPNetwork(x_subnet)
                #l.append(cidr_subnet)
            print("iprange: " + iprange)
            #cidr_subnet = IPNetwork(iprange)
            #l.append(cidr_subnet)

        ''' to be uncommented ----------------------------------        
        # iter the string list and append to IPNetwork list
        for s in subnet_strings:
            subnet = IPNetwork(s)
            l.append(subnet)	 
        '''
        print("++ Convert " + file + " into IPNetwork list ++")
        print(" ")
        return l  



    def logout(self):

        sc.logout()  


    def printMenu(self):
   
        print(" _________________________________________________________________ ") 
        print(" _______ _______ _______ _     _  ______ _____ _______ __   __     ")
        print(" |______ |______ |       |     | |_____/   |      |      \_/       ")
        print(" ______| |______ |_____  |_____| |    \_ __|__    |       |        ")
        print("                                                                   ")                                                           
        print(" _______ _______ __   _ _______ _______  ______                    ")
        print(" |       |______ | \  |    |    |______ |_____/                    ")
        print(" |_____  |______ |  \_|    |    |______ |    \_                    ")
        print("                                                                   ")                                                                   
        print(" _______  _____   _____                                            ")
        print("    |    |     | |     | |                                         ")
        print("    |    |_____| |_____| |_____                                    ")
        print(" _________________________________________________________________ ")                                                                          
        print("                                                                   ") 
        print("1. Login                       ")
        print("2. Export repositories to file ")
        print("3. Print master list           ")
        print("4. Print repositories          ")
        print("5. Compare repositories        ")  
        print("6. Logout                      ")
        print("                               ")
        



if __name__ == '__main__':


    sct = SecurityCenterTool()
    
    loop=True
    
    while loop:
        sct.printMenu()
        choice = input("Enter your choice [1-6]: ")

        if choice == "1":
            sct.login()

        elif choice == "2":
            sct.exportRepositories()  

        elif choice == "3":
            subnet_list_file = "./files/master_subnet_list.txt"
            master_list = sct.fileToIPNetworkList(subnet_list_file)
            print(" ++ Master List ++")
            print(master_list)

        elif choice == "4":
            print("++ List files in dir ++")
            repo_path="./files/repositories"
            for f in listdir(repo_path):
                print(f)
                repo_list = sct.fileToIPNetworkList(repo_path + "/" + f)
                print(repo_list)




        elif choice == "5":
            print("++ Compare repositories (skip) ++")

        elif choice == "6":
            print("++ Logout ++")
            try:
                sc
            except NameError:
                print("Never logged in. Exit.")
            else:
                sct.logout()
                print("Logged out. Exit.")
            loop = False
       
        else:
            input("Wrong option. Type any key to try again ..")
   








