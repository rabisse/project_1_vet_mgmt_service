DROP TABLE IF EXISTS treatments;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    earnings INT
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    bill INT
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    species VARCHAR(255),
    dob VARCHAR(255),
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id)
);

CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cost INT,
    note TEXT,
    pet_id INT REFERENCES pets(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id)
);

