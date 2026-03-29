def top_departments(db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT d.name, SUM(e.salary)
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    GROUP BY d.name
    ORDER BY SUM(e.salary) DESC
    LIMIT 3
    """)

    result = cursor.fetchall()
    conn.close()
    return result

def employees_with_projects(db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT e.name, p.name
    FROM employees e
    JOIN project_assignments pa ON e.emp_id = pa.emp_id
    JOIN projects p ON pa.project_id = p.project_id
    """)

    result = cursor.fetchall()
    conn.close()
    return result

def salary_rank_by_department(db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT e.name, d.name, e.salary,
    RANK() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) AS rank
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    ORDER BY d.name, rank
    """)

    result = cursor.fetchall()
    conn.close()
    return result