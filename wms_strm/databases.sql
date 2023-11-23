-- Create the warehouse_management database
CREATE DATABASE IF NOT EXISTS warehouse_management;
USE warehouse_management;

-- Create items table
CREATE TABLE items (
    `Item name` VARCHAR(255),
    `Item Id` INT PRIMARY KEY,
    Quantity INT,
    Position VARCHAR(255),
    Perishable VARCHAR(3),
    `time` TIMESTAMP
);

-- Create shipment_records table
CREATE TABLE shipment_records (
    `Item name` VARCHAR(255),
    `Item Id` INT PRIMARY KEY,
    Quantity INT
);

-- Insert data into items table
INSERT INTO items (`Item name`, `Item Id`, Quantity, Position, Perishable, `time`)
VALUES ('Item1', 1, 10, 'A1', 'No', CURRENT_TIMESTAMP),
       ('Item2', 2, 20, 'B2', 'Yes', CURRENT_TIMESTAMP),
       ('Item3', 3, 15, 'C3', 'No', CURRENT_TIMESTAMP);

-- Insert data into shipment_records table
INSERT INTO shipment_records (`Item name`, `Item Id`, Quantity)
VALUES ('Item1', 1, 5),
       ('Item2', 2, 10),
       ('Item3', 3, 8);