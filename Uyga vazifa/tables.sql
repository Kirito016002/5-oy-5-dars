CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    status BOOLEAN NOT NULL,
    smen SMALLINT NOT NULL
);

CREATE TABLE evaluation(
    comment TEXT NOT NULL,
    rating SMALLINT NOT NULL 
);