{{ config(
    alias = "stg__store_cities"
)}}

select
  store_id,
  storetype_id as store_type_id,
  store_size,
  city_id
from {{source("kaggle_retails","store_cities")}}
