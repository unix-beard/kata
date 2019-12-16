CREATE TABLE user(
    username varchar(255) primary key not null, 
    name varchar(255), 
    hash varchar(512) not null, 
    salt varchar(64) not null,
    last_login datetime
);
