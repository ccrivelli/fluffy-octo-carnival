from securitycenter import SecurityCenter5
import  getpass

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


    def getRepos(self):
        print("Repository list:")
        response = sc.get('repository?type=All')
        print(response.json())
        for repo in response.json()['response']:
            print(repo)
#            repo_id_url = 'repository/'+repo['id']
#            print(repo['id'])
#            response2 = sc.get(repo_id_url)



    def logout(self):
        sc.logout()  


if __name__ == '__main__':

    sct = SecurityCenterTool()
    sct.login()
    sct.getRepos()
    sct.logout()
