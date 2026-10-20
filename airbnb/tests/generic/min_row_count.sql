{% test min_row_count(model, min_count) %}

select count(*) as cnt from {{model}}
having count(*) < {{min_count}}

{% endtest %}