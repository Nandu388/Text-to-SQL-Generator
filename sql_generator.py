import re
import spacy

nlp = spacy.load("en_core_web_sm")

# -----------------------------------
# MAIN FUNCTION
# -----------------------------------

def generate_sql(prompt):

    prompt = prompt.lower()

    doc = nlp(prompt)

    # -----------------------------------
    # DEFAULT VALUES
    # -----------------------------------

    table_name = "table_name"

    columns = []

    conditions = []

    limit = ""

    order_by = ""

    aggregate = ""

    # -----------------------------------
    # DETECT TABLE NAME
    # -----------------------------------

    possible_tables = [
        "employees",
        "students",
        "products",
        "customers",
        "orders",
        "books",
        "sales",
        "movies",
        "teachers",
        "users"
    ]

    for table in possible_tables:

        if table in prompt:

            table_name = table

    # -----------------------------------
    # DETECT COLUMNS
    # -----------------------------------

    possible_columns = [
        "id",
        "name",
        "salary",
        "department",
        "age",
        "price",
        "rating",
        "email",
        "phone",
        "quantity",
        "date",
        "marks",
        "city"
    ]

    for token in doc:

        if token.text in possible_columns:

            columns.append(token.text)

    # Remove duplicates
    columns = list(set(columns))

    # -----------------------------------
    # DEFAULT COLUMN
    # -----------------------------------

    if columns:

        selected_columns = ", ".join(columns)

    else:

        selected_columns = "*"

    # -----------------------------------
    # LIMIT
    # -----------------------------------

    numbers = re.findall(r'\d+', prompt)

    if numbers:

        limit = f" LIMIT {numbers[0]}"

    # -----------------------------------
    # CONDITIONS
    # -----------------------------------

    # GREATER THAN
    if "greater than" in prompt:

        number = re.findall(r'\d+', prompt)

        if number:

            if "age" in prompt:
                conditions.append(
                    f"age > {number[0]}"
                )

            elif "price" in prompt:
                conditions.append(
                    f"price > {number[0]}"
                )

            elif "salary" in prompt:
                conditions.append(
                    f"salary > {number[0]}"
                )

    # LESS THAN
    if "less than" in prompt:

        number = re.findall(r'\d+', prompt)

        if number:

            if "age" in prompt:
                conditions.append(
                    f"age < {number[0]}"
                )

            elif "price" in prompt:
                conditions.append(
                    f"price < {number[0]}"
                )

            elif "salary" in prompt:
                conditions.append(
                    f"salary < {number[0]}"
                )

    # -----------------------------------
    # ORDER BY
    # -----------------------------------

    if "highest" in prompt:

        if "salary" in prompt:

            order_by = " ORDER BY salary DESC"

        elif "price" in prompt:

            order_by = " ORDER BY price DESC"

        elif "rating" in prompt:

            order_by = " ORDER BY rating DESC"

    # -----------------------------------
    # AGGREGATES
    # -----------------------------------

    if "count" in prompt:

        query = f"SELECT COUNT(*) FROM {table_name}"

    elif "average" in prompt:

        if "salary" in prompt:

            query = f"SELECT AVG(salary) FROM {table_name}"

        elif "price" in prompt:

            query = f"SELECT AVG(price) FROM {table_name}"

        elif "marks" in prompt:

            query = f"SELECT AVG(marks) FROM {table_name}"

        else:

            query = f"SELECT AVG(column_name) FROM {table_name}"

    elif "maximum" in prompt:

        if "salary" in prompt:

            query = f"SELECT MAX(salary) FROM {table_name}"

        elif "price" in prompt:

            query = f"SELECT MAX(price) FROM {table_name}"

        else:

            query = f"SELECT MAX(column_name) FROM {table_name}"

    else:

        query = f"SELECT {selected_columns} FROM {table_name}"

    # -----------------------------------
    # CONDITIONS
    # -----------------------------------

    if conditions:

        query += " WHERE "

        query += " AND ".join(conditions)

    # -----------------------------------
    # ORDER BY
    # -----------------------------------

    query += order_by

    # -----------------------------------
    # LIMIT
    # -----------------------------------

    query += limit

    # -----------------------------------
    # END QUERY
    # -----------------------------------

    query += ";"

    return query