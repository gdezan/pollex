drop table if exists users;
create table users (
    id serial primary key, 
    email text not null unique,
    name text not null,
    n_usp integer not null
);

drop table if exists polls;
create table polls (
    id serial primary key, 
    title text not null,
    votes integer not null,
    user_id serial not null,
    foreign key (user_id) references users(id)
)
