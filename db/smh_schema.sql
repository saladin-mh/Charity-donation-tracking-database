-- SMH Charity Donation Tracker Database Schema
-- Author: [Your Name]
-- Purpose: Structured relational schema for tracking charity donations
-- Compliance: Normalised to 3NF, with enforced relational integrity

PRAGMA foreign_keys = ON;

-- -------------------------
-- Donors Table
-- -------------------------
CREATE TABLE IF NOT EXISTS donors (
    donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    business_name TEXT,
    postcode TEXT,
    house_number TEXT,
    phone_number TEXT
);

-- -------------------------
-- Events Table
-- -------------------------
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    room_info TEXT,
    booking_datetime DATETIME NOT NULL,
    cost REAL NOT NULL CHECK (cost >= 0)
);

-- -------------------------
-- Volunteers Table
-- -------------------------
CREATE TABLE IF NOT EXISTS volunteers (
    volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    phone_number TEXT
);

-- -------------------------
-- Donations Table
-- -------------------------
CREATE TABLE IF NOT EXISTS donations (
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

-- -------------------------
-- admin_users Table
-- -------------------------

CREATE TABLE IF NOT EXISTS admin_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);
