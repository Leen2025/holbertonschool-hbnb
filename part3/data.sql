-- data.sql

-- Insert Admin User (password: "admin1234", hashed using bcrypt)
INSERT INTO User (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    '$2b$12$nFM6oN9mA1ZJlv.npV1WIeGFT6e1Iz/EZjI/R9R5JgFzkfsMj5nsS',
    TRUE
);

-- Insert Initial Amenities
INSERT INTO Amenity (id, name) VALUES
('2fae58a3-1a63-4a08-b31e-93c2549f69e3', 'WiFi'),
('7c3ef0cb-c020-4b3b-98c7-d59f9e7b891a', 'Swimming Pool'),
('19d8f90e-76cc-4026-9f50-6e0b4c9de6bc', 'Air Conditioning');
