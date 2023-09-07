show databases;

use employees_dev;

CREATE TABLE hired_employees (
    id int,
    name varchar(50),
    datetime varchar(20),
    department_id int,
    job_id int
);

CREATE TABLE departments (
    id int,
    department varchar(50)
);

CREATE TABLE jobs (
    id int,
    job varchar(50)
);

show full tables;