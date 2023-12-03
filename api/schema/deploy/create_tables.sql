-- deploy ecommerce:create_tables to pg
-- requires: create_schema

begin;

create table ecommerce.users (
    username varchar(16) primary key,
    email varchar(255) not null unique,
    password varchar(255) not null
);

create table ecommerce.products (
    id integer generated always as identity primary key,
    name varchar(255) not null,
    price money not null
);

create table ecommerce.carts (
    id integer generated always as identity primary key,
    username varchar(16) references ecommerce.users,
    created_on timestamp not null,
    ordered boolean not null
);

create table ecommerce.cart_items (
    cart_id integer references ecommerce.carts,
    product_id integer references ecommerce.products,
    quantity integer not null,
    subtotal money not null,
    primary key (cart_id, product_id)
);

create type order_status as enum ('placed', 'in progress', 'shipped');

create table ecommerce.orders (
    id integer generated always as identity primary key,
    cart_id integer references ecommerce.carts unique,
    username varchar(16) references ecommerce.users,
    placed_on timestamp not null,
    status order_status not null,
    total money not null
);

commit;
