{{ config(
    alias = "stg__kaggle_sales"
)}}

select
  product_id,
  store_id,
  date::date as sales_date,
  sales::decimal(13, 3) as sold_quantity,
  revenue::decimal(13,2) as net_value,
  stock::decimal(13,3) as stock_quantity,
  price::decimal(13,2) as product_unit_price,
  promo_type_1,
  promo_bin_1,
  promo_type_2,
  promo_bin_2,
  promo_discount_2::decimal(4,2) as promo_discount_2_prct,
  promo_discount_type_2,
from {{ source("kaggle_retails", "sales") }}
