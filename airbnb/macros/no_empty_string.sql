{% macro no_empty_string(model_obj) %}
    {% for col in adapter.get_columns_in_relation(model_obj) %}
        {% if col.is_string %}
            {{ col.name }} is not null and {{ col.name }} <> '' and
            {% endif %}
    {% endfor %}
    TRUE
{% endmacro %}