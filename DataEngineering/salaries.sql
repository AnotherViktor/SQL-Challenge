CREATE TABLE salaries (
    emp_no BIGINT NOT NULL,
    salary BIGINT NOT NULL,
    PRIMARY KEY (emp_no, salary),
    FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);
SELECT * FROM salaries;
