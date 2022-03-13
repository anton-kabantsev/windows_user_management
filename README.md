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
Main script is Get_user_info.py Params for start:
1 c:\temp\user_data.txt
2 c:\temp\work_done.txt - flag that work is done for 1c.
