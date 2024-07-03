CREATE DATABASE IF NOT EXISTS clients_db;

USE clients_db;


-- Create the client_type table
CREATE TABLE IF NOT EXISTS client_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create the services table
CREATE TABLE IF NOT EXISTS services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    path VARCHAR(255) NOT NULL,
    method VARCHAR(10) NOT NULL,
    enabled BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create the permissions table
CREATE TABLE IF NOT EXISTS permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_type INT NOT NULL,
    enabled BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_type) REFERENCES client_type(id)
);

-- Create the permissions_services table to link permissions and services
CREATE TABLE IF NOT EXISTS permissions_services (
    permission_id INT NOT NULL,
    service_id INT NOT NULL,
    PRIMARY KEY (permission_id, service_id),
    FOREIGN KEY (permission_id) REFERENCES permissions(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Create the clients table
CREATE TABLE IF NOT EXISTS clients (
    id CHAR(36) PRIMARY KEY,  -- UUID
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    client_type INT NOT NULL,
    enable BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_type) REFERENCES client_type(id)
);