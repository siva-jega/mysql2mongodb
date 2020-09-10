CREATE DATABASE IF NOT EXISTS skills;

USE skills; 

CREATE TABLE IF NOT EXISTS employee (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL DEFAULT '',
    PRIMARY KEY (id)

);

CREATE TABLE IF NOT EXISTS salary (
    id INT NOT NULL AUTO_INCREMENT,
    employee_id INT NOT NULL,
    salary DECIMAL(10,2),
    PRIMARY KEY (id),
    FOREIGN KEY (employee_id) REFERENCES employee(id)
);

INSERT INTO employee (id, name) VALUES (1, 'John'), (2, 'Smith'), (3, 'Mary'), (4, 'Lucy');
INSERT INTO salary (id, employee_id, salary) VALUES (1, 1, '1200.00'), (2, 2, '800.00'), (3, 3, '600.00'), (4, 4, '1000.00');

