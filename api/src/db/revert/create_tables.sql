-- revert ecommerce:create_tables from pg

begin;

drop table ecommerce.users cascade;
drop table ecommerce.products cascade;
drop table ecommerce.carts cascade;
drop table ecommerce.cart_products cascade;
drop table ecommerce.orders cascade;
drop type order_status;

commit;
