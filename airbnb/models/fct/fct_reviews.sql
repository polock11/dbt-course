{{
    config(
        materialized='incremental',
        on_schema_change='fail',
        unique_key='review_id',
        incremental_strategy='merge'
    )
}}
with src_reviews as(
    select * from {{ref('src_reviews')}}
)
select
    {{ dbt_utils.generate_surrogate_key(['listing_id', 'review_date', 'review_text']) }} as review_id,
    * 
from src_reviews 
where review_text is not null
{# {% if is_incremental() %}
    and review_date > (select max(review_date) from {{this}})
{% endif %} #}
{% if is_incremental() %}
    and review_date >= (
        select dateadd(
            day, -7, coalesce(max(review_date), '1900-01-01')
        )
        from {{ this }}
    )
{% endif %}