-- verify ecommerce:create_schema on pg

begin;

select pg_catalog.has_schema_privilege('ecommerce', 'usage');

rollback;
