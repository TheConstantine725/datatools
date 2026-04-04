{{ config(
    alias = "stg__material_hierarchy"
)}}

select
  product_id,
  round(product_length, 2)::decimal(12,2) as product_length_cm,
  round(product_depth, 2)::decimal(12,2) as product_depth_cm,
  round(product_width, 2)::decimal(12,2) as product_width_cm,
  cluster_id,
  hierarchy1_id,
  hierarchy2_id,
  hierarchy3_id,
  hierarchy4_id,
  hierarchy5_id,
  from {{ source("kaggle_retails", "product_hierarchy") }}
