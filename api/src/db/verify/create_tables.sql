-- verify ecommerce:create_tables on pg

begin;

select * from ecommerce.users where false;
select * from ecommerce.products where false;
select * from ecommerce.carts where false;
select * from ecommerce.cart_items where false;
select * from ecommerce.orders where false;

rollback;
