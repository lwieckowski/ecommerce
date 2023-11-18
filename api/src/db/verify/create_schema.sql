-- Verify ecommerce:create_schema on pg

BEGIN;

SELECT pg_catalog.has_schema_privilege('ecommerce', 'usage');

ROLLBACK;
