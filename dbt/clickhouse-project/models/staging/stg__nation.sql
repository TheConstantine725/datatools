{{
config(
materialized = "view"
)
}}

with source_nation
as (
select *
from {{source("tpch", "nation")}}
)
select
    n_nationkey as nation_key,
    n_name as nation_name,
    n_regionkey as region_key,
    n_comment as n_comment
from source_nation
