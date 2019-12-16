#!/usr/bin/env python3

###################################################################################
# Simple authentication program with the following subcommands: login, add, del. 
# All registered users should be stored in a database, along with their user names, 
# their hashed and salted passwords. 
# When the user uses login subcommand, the program greets the user and prints 
# the last date-time the user logged in. 
# add command registers a user with your program, 
# del command removes a user from database. 
# Bonus points: Add pwd subcommand to change user's password.
###################################################################################

import argparse
import getpass
import sqlite3
import os
import uuid
import hashlib
from datetime import datetime


def db_init():
    users_db = 'users.db'
    if not os.path.isfile(users_db):
        raise Exception('Users database not found!')

    db_con = sqlite3.connect(users_db)
    db_cur = db_con.cursor()

    return db_con, db_cur


db_con, db_cur = db_init()


def salt_and_hash(passwd):
    return passwd


def from_db(username, field=''):
    db_cur.execute('SELECT ' + field + ' FROM user WHERE username=?', (username,))
    res = db_cur.fetchone()
    return res if res is None else res[0]


def update_last_login(username):
    db_cur.execute('UPDATE user SET last_login=? where username=?', (datetime.now(), username,))
    db_con.commit()


def user_login(args):
    assert from_db(args.user, field='username') is not None, 'User doesn\'t exists!'
    salt = from_db(args.user, field='salt')
    passwd = hashlib.sha512(getpass.getpass().encode('utf-8') + salt.encode('utf-8')).hexdigest()
    if passwd == from_db(args.user, field='hash'):
        print('Welcome back, {0}'.format(from_db(args.user, field='name')))
        last_login = from_db(args.user, field='last_login')
        print('Last login: {0}'.format(last_login if last_login is not None else 'Just now'))
        update_last_login(args.user)
    else:
        print('Wrong password')


def db_user_add(username, name, hash, salt):
    db_cur.execute('INSERT INTO user VALUES(?,?,?,?, NULL)', (username, name, hash, salt,))
    db_con.commit()


def user_add(args):
    assert from_db(args.user, field='username') is None, 'User already exists!'

    name = input('Name: ')
    passwd1, passwd2 = uuid.uuid4().hex + '1', uuid.uuid4().hex + '2'
    while passwd1 != passwd2:
        salt = uuid.uuid4().hex
        passwd1 = hashlib.sha512(getpass.getpass().encode('utf-8') + salt.encode('utf-8')).hexdigest()
        passwd2 = hashlib.sha512(getpass.getpass('Retype password: ').encode('utf-8') + salt.encode('utf-8')).hexdigest()
        if passwd1 != passwd2:
            print('Sorry, passwords don\'t match. Try again')

    db_user_add(args.user, name, passwd1, salt)
    print('User `{0}` successfully created'.format(args.user))


def main():
    parser = argparse.ArgumentParser(prog='auth')
    subparsers = parser.add_subparsers()
    subparsers.required = True
    subparsers.dest = 'command'

    ############################################################################
    # Parser for "login" command
    ############################################################################
    login_parser = subparsers.add_parser('login', help='Logs user in')
    login_parser.add_argument('-u', '--user', type=str, required=True, help='Username')
    login_parser.set_defaults(func=user_login)

    ############################################################################
    # Parser for "add" command
    ############################################################################
    add_user_parser = subparsers.add_parser('add', help='Add a user to the program')
    add_user_parser.add_argument('-u', '--user', type=str, required=True, help='Username')
    add_user_parser.set_defaults(func=user_add)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    try:
        db_init()
        main()
    except Exception as ex:
        print(ex)
