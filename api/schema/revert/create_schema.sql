-- revert ecommerce:create_schema from pg

begin;

drop schema ecommerce;

commit;
