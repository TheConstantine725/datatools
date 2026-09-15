{{
    config(materialized = "view")
}}


with import_data as (

    select
    toString(l_orderkey)||'-'||toString(l_linenumber) as order_line_id,
    --l_orderkey,
    toString(l_partkey) as part_key,
    toString(l_suppkey) as supplier_key,
    l_quantity as billed_quantity,
    l_extendedprice as net_billed_value,
    cast (l_extendedprice/l_quantity as Decimal(13,2) ) as unit_value,
    l_discount as discount_pct,
    l_tax as tax_pct,
    l_returnflag as return_flag,
    l_linestatus,
    l_shipdate as shipping_date,
    l_commitdate as commit_date,
    l_receiptdate as receipt_date,
    l_shipinstruct as ship_instruction,
    l_shipmode as shipping_mode,
    l_comment as additional_comments,
    _extraction_timestamp
    from {{source("tpch","line_items")}}
)
select *
from import_data
