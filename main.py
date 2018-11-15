"""
Main program
"""
from twitter_interface import TwitterHandler

def main():
    twitter_handler = TwitterHandler()

    twitter_handler.print_credentials()

    twitter_user_handle = input("Enter the user handle for the user whose status you want to see: \n")
    twitter_handler.print_user_status(twitter_user_handle)   #Replace the user handle for the user whose recent statuses you want printed

if __name__ == "__main__":
    main()