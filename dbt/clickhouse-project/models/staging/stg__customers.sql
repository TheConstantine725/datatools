{{config(materialized = "view")}}

with source_customers as
    (select * from {{source("tpch", "customers")}})
SELECT
c_custkey as customer_id,
c_name as customer_name,
c_address as customer_address,
c_nationkey as nation_id,
c_phone as phone_number,
c_acctbal as acctbal,
c_mktsegment as market_segment,
c_comment as customer_comment
FROM source_customers
