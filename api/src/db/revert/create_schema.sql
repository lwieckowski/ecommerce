-- Revert ecommerce:create_schema from pg

BEGIN;

DROP SCHEMA ecommerce;

COMMIT;
