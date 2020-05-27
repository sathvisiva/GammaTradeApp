import login
import fetchTokenFromFile
import config
import isLoggedIn


if __name__=="__main__":

    print(isLoggedIn.isLoggedIn())
    print("old token ="+config.access_token)
    if(isLoggedIn.isLoggedIn() == False):
        print(login.login_fn())
        print("new token ="+config.access_token)