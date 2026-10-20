with mart_fool_moon as (
    select * from {{ ref('mart_full_moon_review') }}
)
select
    is_full_moon,
    review_sentiment,
    count(*) as reviews
from
    mart_fool_moon
group by
    is_full_moon,
    review_sentiment
order by
    is_full_moon,
    review_sentiment
