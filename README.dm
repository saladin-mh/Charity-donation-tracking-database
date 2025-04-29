SMH Charity Donation Tracker Welcome to the SMH Charity Donation Tracker, a full-stack Python application designed to streamline the management of donors, volunteers, events, and donations for charitable organisations. Built with a focus on modularity, security, and ease of use, this project embodies industry best practices and real-world development standards.

Project Overview This application was created to enable charity administrators to securely track all donation-related activities through a clean, command-line interface. Developed using Python and SQLite, the project applies robust principles such as the Single Responsibility Principle, modular architecture (similar to MVC), and secure authentication practices (bcrypt password hashing).

Key Features Full CRUD (Create, Read, Update, Delete) operations for:

Donors

Volunteers

Events

Donations

Contact Preferences

Event Sponsors

Admin authentication system using bcrypt

Parameterised SQL queries to prevent SQL injection

Database foreign key enforcement

Tabulated search results for better readability

Structured, scalable, and maintainable codebase

Technologies Used Python 3.10+

SQLite (local database)

bcrypt (password security)

tabulate (for formatted table outputs)

contextlib (for managed database connections)

getpass (for secure password inputs)

Project Structure

SMH/ ├── db/ │ └── db_manager.py ├── models/ │ ├── admin.py │ ├── donor.py │ ├── volunteer.py │ ├── event.py │ ├── donation.py │ ├── contact_preference.py │ └── event_sponsor.py ├── services/ │ └── search.py ├── scripts/ │ └── populate_sample_data.py └── src/ └── main.py

Citations & References

SQLite Official Documentation: sqlite.org

OWASP Password Storage Cheat Sheet: owasp.org

Robert C. Martin's SOLID Principles: Agile Software Development: Principles, Patterns, and Practices (2002)

MVC Architectural Patterns: Design Patterns: Elements of Reusable Object-Oriented Software (Gamma et al., 1995)

Final Thoughts

This project represents a deep commitment to building clean, secure, and professional software. It stands as a testament to countless hours of hard work, careful planning, and an unwavering passion for software development.
