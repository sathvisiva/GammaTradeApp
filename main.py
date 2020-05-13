import login
import fetchTokenFromFile
import config
import isLoggedIn


if __name__=="__main__":
    print(login.login_fn())
    print(config.access_token)
    print(isLoggedIn.isLoggedIn())