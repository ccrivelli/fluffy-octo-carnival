from securitycenter import SecurityCenter5
import  getpass
from netaddr import *
from os import listdir
import re
import string


class SecurityCenterTool():
    
    def __init__(self):
        pass
 

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
        '''
        export repositories to files (might contain IP Ranges as well)
        '''

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
        - import a txt containing a list of subnets and convert into a list of IPNetwork Objects
        - input file might contain IP Ranges, they are identified and converted into CIDR subnets (WIP)
        '''

        # read file line by line without \n and save in a list
        with open(file) as f:
            subnet_strings = f.read().splitlines()
            print(subnet_strings)

        # search for IP Ranges like 10.1.2.0-10.1.5.255 and create a new list of subnets with no IP ranges
        l = []
        n = None
        
        for iprange in subnet_strings:
            print("iprange: " + iprange)
            # search for IP Ranges | regexp to search for a dash '-' followed by a word 
            if re.search('(?<=-)\w+',iprange):
                print("IP Range Found!! >> " + iprange)
                x_subnet = iprange.split('-')
                print(x_subnet)
                print("  start: " + x_subnet[0])
                print("  end: " + x_subnet[1])
                # IP Range Object
                r = IPRange(x_subnet[0],x_subnet[1])
                print("Convert to CIDRS:")
                print(r.cidrs())
                for sub in r.cidrs():
                    n = IPNetwork(sub)
                    l.append(n)
                    #print("-- Printing List (IP Ranges)---")
                    #print(l)

            else:
                n = IPNetwork(iprange)
                l.append(n)
                #print("-- Printing List (No Ranges)---")
                #print(l)   

        print("++ Convert " + file + " into IPNetwork list ++")
        print(" ")
        return l  
  

    def repositoriesDiff(self, file1, file2):

        ''' importing 2 files containing ip lists, converting into IPSet then performing a diff'''
        s1 = IPSet()
        s2 = IPSet()

        # read lines into a list
        with open(file1) as f1:
            l1 = f1.read().splitlines()
            print("repo1")
            print(l1)

        # create the IPSet
        for ip1 in l1:
            s1.add(ip1)

        print(s1)    

        # read lines into a list
        with open(file2) as f2:
            l2 = f2.read().splitlines()
            print("repo2")
            print(l2)

        # create the second IPSet
        for ip2 in l2:
            s2.add(ip2)

        print(s2)

        s_diff = s1 ^ s2
        ##print(s_diff)
        return s_diff


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
        print("1. Login                                                           ")
        print("2. Export repositories to file (Login Required)                    ")
        print("3. Convert master list(file) to IPNetork and print (WIP)           ")
        print("4. Convert repositories(file) to IPNetwork and print (WIP)         ")
        print("5. Repositories Exclusion (Diff) from file                         ")  
        print("6. Logout                      ")
        print("                               ")
        



if __name__ == '__main__':


    sct = SecurityCenterTool()
    
    loop=True
    
    while loop:
        sct.printMenu()
        choice = input("Enter your choice [1-6]: ")

        if choice == "1":
            '''Login  '''
            sct.login()

        elif choice == "2":
            '''Export repositories to file (Login Required)  '''
            sct.exportRepositories()  

        elif choice == "3":
            '''Convert master list(file) to IPNetork and print'''
            subnet_list_file = "./files/master_subnet_list.txt"
            master_list = sct.fileToIPNetworkList(subnet_list_file)
            print(" ++ Master List ++")
            print(master_list)

        elif choice == "4":
            '''Convert repositories(file) to IPNetwork and print'''
            print("++ List files in dir ++ \n")
            repo_path="./files/repositories"
            for f in listdir(repo_path):
                print(f)
                repo_list = sct.fileToIPNetworkList(repo_path + "/" + f)
                print("++ IPNetwork List ++")
                print(repo_list)
                print("====================================================================================== \n")




        elif choice == "5":
            '''Repositories Exclusion (Diff) from file  '''
            print("++ Repositories Exclusion (diff) ++")
            repo1 = "./files/input/repo1.txt"
            repo2 = "./files/input/repo2.txt"
            print("   ++ Difference between " + repo1 + " and " + repo2 + " ++")
            diffrepo = sct.repositoriesDiff(repo1, repo2)
            print("diffrepo")

            print(diffrepo)
            output_file = "./files/diff.txt"
            #for ip in diffrepo:
            #    print(ip)



        elif choice == "6":
            '''Logout    '''
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
   








