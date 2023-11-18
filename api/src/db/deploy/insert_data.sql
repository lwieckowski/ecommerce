-- deploy ecommerce:insert_data to pg
-- requires: create_tables

begin;

insert into ecommerce.products (name, price) values
    ('Keyboard', 25.41),
    ('Monitor', 221.99),
    ('Chair', 110.49),
    ('Mouse', 10.45),
    ('PC', 999.99),
    ('Cable pack', 9.99);

insert into ecommerce.users (username, email, first_name, last_name, password) values
    ('john776', 'jdoe@hotmail.com', 'John', 'Doe', 'h6hgd82hdy6ds'),
    ('jdoe', 'janedoe@gmail.com', 'Jane', 'Doe', 'j6hgd72huy68s');

insert into ecommerce.carts (username, created_on, ordered) values
    ('jdoe', '2022-01-01 00:11:21', false),
    ('jdoe', '2023-01-01 00:11:21', false);

insert into ecommerce.cart_items (cart_id, product_id, quantity, subtotal) values
    (1, 1, 2, 23.22),
    (1, 3, 1, 232.11),
    (1, 4, 1, 222.44);

insert into ecommerce.orders (cart_id, username, placed_on, status, total) values
    (1, 'jdoe', '2023-02-02 00:00:00', 'placed', 445.21);

commit;
