-- SMH Charity Donation Tracker Schema
-- Version 1.0
-- Author: [Your Name]
-- Created: 2025-04-11

PRAGMA foreign_keys = ON;

CREATE TABLE donors (
    donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    business_name TEXT,
    postcode TEXT,
    house_number TEXT,
    phone_number TEXT
);

CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    room_info TEXT,
    booking_datetime DATETIME NOT NULL,
    cost REAL NOT NULL CHECK (cost >= 0)
);

CREATE TABLE volunteers (
    volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT
);

CREATE TABLE donations (
    donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL CHECK (amount > 0),
    donation_date DATE NOT NULL,
    gift_aid BOOLEAN DEFAULT 0,
    notes TEXT,
    donor_id INTEGER,
    event_id INTEGER,
    volunteer_id INTEGER,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE RESTRICT,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE RESTRICT,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE SET NULL
);
