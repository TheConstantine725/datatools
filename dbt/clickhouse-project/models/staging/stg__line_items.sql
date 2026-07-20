{{
    config(materialized = "materialized_view",
    engine = "SummingMergeTree()",
    order_by = "(shipping_year, shipping_month)")
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
    from data_landing.tpch_line_items
),
create_additional_columns as (select
YEAR(shipping_date) as shipping_year,
MONTH(shipping_date) as shipping_month,
net_billed_value,
billed_quantity,
part_key,
supplier_key,
shipping_mode
from import_data)

select
    shipping_year,
    shipping_month,
    part_key,
    supplier_key,
    shipping_mode,
    sum(net_billed_value) as total_net_billed_value,
    sum(billed_quantity) as total_billed_quantity
from create_additional_columns
group by shipping_year,
    shipping_month,
    part_key,
    supplier_key,
    shipping_mode
