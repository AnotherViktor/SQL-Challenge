SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e
JOIN dept_manager dm ON e.emp_no = dm.emp_no
JOIN departments d ON dm.dept_no = d.dept_no
WHERE d.dept_name IN ('Sales', 'Development');