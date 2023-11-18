-- deploy ecommerce:create_tables to pg
-- requires: create_schema

begin;

create table ecommerce.users (
    username varchar(16) primary key,
    email varchar(255) not null unique,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    password_hash varchar(255) not null
);

create table ecommerce.products (
    id integer generated always as identity primary key,
    name varchar(255) not null,
    description text not null,
    price money not null
);

create table ecommerce.carts (
    id integer generated always as identity primary key,
    username varchar(16) references ecommerce.users
);

create table ecommerce.cart_products (
    cart_id integer references ecommerce.carts primary key,
    product_id integer references ecommerce.products
);

create type order_status as enum ('placed', 'in progress', 'shipped');

create table ecommerce.orders (
    id integer generated always as identity primary key,
    cart_id integer references ecommerce.carts,
    username varchar(16) references ecommerce.users,
    placed_on timestamp not null,
    status order_status not null,
    total money not null
);

commit;
