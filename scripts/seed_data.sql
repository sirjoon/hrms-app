-- Departments
INSERT INTO departments (name) VALUES ('IT'), ('HR'), ('Finance');
-- Roles
INSERT INTO roles (name) VALUES ('Developer'), ('Manager'), ('HR'), ('Admin');
-- Admin user
INSERT INTO employees (first_name, last_name, email, password, employment_type, joining_date, department_id, role_id, status)
VALUES ('Admin', 'User', 'admin@example.com', '$2b$12$KIXQ4Qh1QJQwQJQwQJQwQOQJQwQJQwQJQwQJQwQJQwQJQwQJQwQJQ', 'full_time', '2023-01-01', 1, 4, 'active');
-- Employee user
INSERT INTO employees (first_name, last_name, email, password, employment_type, joining_date, department_id, role_id, status)
VALUES ('John', 'Doe', 'john.doe@example.com', '$2b$12$u1Q4Qh1QJQwQJQwQJQwQOQJQwQJQwQJQwQJQwQJQwQJQwQJQwQJQ', 'full_time', '2023-01-01', 1, 1, 'active');
