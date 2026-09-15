create database ducklake;
create user ducklake_user with password 'ducklake';
grant all privileges on database ducklake to ducklake_user;

create database metabase;
create user metabase_user with password 'metabase';
grant all privileges on database metabase to metabase_user;
