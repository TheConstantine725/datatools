{{config(
materialized = "view")
}}

with source_orders as
    (select *
    from {{source("tpch", "orders")}})

select
    o_orderkey as order_key,
    o_custkey as customer_id,
    o_orderstatus as order_status,
    o_totalprice as orders_total_price,
    o_orderdate as order_date,
    o_orderpriority as order_priority,
    o_clerk as clerk_id,
    o_shippriority as shipping_priority,
    o_comment as orders_comment
from source_orders
