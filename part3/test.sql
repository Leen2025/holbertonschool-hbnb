-- test.sql

-- ✅ SELECT: Check inserted Admin User
SELECT * FROM User WHERE email = 'admin@hbnb.io';

-- ✅ SELECT: Check inserted Amenities
SELECT * FROM Amenity;

-- ✅ INSERT: Add a Place owned by Admin
INSERT INTO Place (id, title, description, price, latitude, longitude, owner_id)
VALUES (
    '0c973e04-51b6-45a6-b2ff-2ff96d0deedc',
    'Cozy Loft',
    'Modern and central location',
    150.00,
    24.7136,
    46.6753,
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1'
);

-- ✅ INSERT: Link Place with Amenities
INSERT INTO Place_Amenity (place_id, amenity_id) VALUES
('0c973e04-51b6-45a6-b2ff-2ff96d0deedc', '2fae58a3-1a63-4a08-b31e-93c2549f69e3'), -- WiFi
('0c973e04-51b6-45a6-b2ff-2ff96d0deedc', '7c3ef0cb-c020-4b3b-98c7-d59f9e7b891a'); -- Swimming Pool

-- ✅ INSERT: Create a Review
INSERT INTO Review (id, text, rating, user_id, place_id)
VALUES (
    '403e48f6-5184-4609-a7b5-6e2733e5e4f5',
    'Great place to stay!',
    5,
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    '0c973e04-51b6-45a6-b2ff-2ff96d0deedc'
);

-- ❌ INSERT: Duplicate review test (should fail due to UNIQUE constraint)
-- INSERT INTO Review (id, text, rating, user_id, place_id)
-- VALUES (
--     'another-uuid',
--     'Trying a duplicate review',
--     4,
--     '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
--     '0c973e04-51b6-45a6-b2ff-2ff96d0deedc'
-- );

-- ✅ UPDATE: Update Place Price
UPDATE Place SET price = 180.00 WHERE id = '0c973e04-51b6-45a6-b2ff-2ff96d0deedc';

-- ✅ DELETE: Delete the Review
DELETE FROM Review WHERE id = '403e48f6-5184-4609-a7b5-6e2733e5e4f5';

-- ✅ SELECT ALL DATA FOR REVIEW
SELECT * FROM Review;
