# windows_user_management
Collects information about pc users, this is important for server with alo of users, some of them works, some don't. this tool combined with 1c gives you a table with all users 
in table with rows:
1. Name
2. Full name
3. Last login data
4. Last password set data
5. User Sid
6. User profile path, some times user name is different with user dir name
7. User status active or not
8. User comment
9. User group membership
Main script is Get_user_info.py should be started with 2 parameters: 1. location of txt with user data 2. location of flag txt which ia aimed to talk 1c that script work is done
don't forget to write not only the path but also the name of the txt.
