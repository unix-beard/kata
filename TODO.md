+ **freq** - Read a file of text, determine the most frequently used words, and print out a sorted list of those words along with their frequencies.
+ **auth** - Simple authentication program with the following subcommands: *login*, *add*, *del*. All registered users should be stored in a database, along with their user names, their hashed and salted passwords. When the user uses *login* subcommand, the program greets the user and prints the last date-time the user logged in. *add* command registers a user with your program, and *del* command removes a user from database. **Bonus points:** Add *pwd* subcommand to change user's password.

    ######Some usage examples:

```
    $ auth login -u john_doe
    Password:
    Welcome back, John Doe! Last login: 20 Feb, 2015 14:15
    
    $ auth login -u user_does_not_exist
    Password:
    Invalid username or password
    
    $ auth add -u new_user
    Name: Jill Baker
    Password:
    User `new_user` successfully created
    
    $ auth login -u new_user
    Password:
    Welcome back, Jill Baker! Last login: Just now
    
    $ auth del -u new_user
    Password:
    Are you sure you want to delete user `new_user`? [Y/n]
    User `new_user` was deleted.
``` 
+ **crypto** - Implement various crypto algorithms (e.g., DES/3DES, AES). Bonus points for **never!** using your implementations in real software :)
