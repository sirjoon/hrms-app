the complete steps to seed your database, start the app, and test everything:

1. Seed the Database
Option A: Fresh Start (Recommended for Clean Setup)

Stop all running containers:
Remove the existing PostgreSQL data volume (this will delete all data):
Start containers and seed database:
This will re-run scripts/seed_data.sql and seed your admin and employee users.
Option B: Manual Seed (If you don’t want to delete all data)

Make sure PostgreSQL is running:
Open pgAdmin at http://localhost:5050, log in, and connect to hrms_db.
Open the Query Tool, paste the contents of scripts/seed_data.sql, and run the query.
2. Run Alembic Migrations
Open a terminal and activate your Python virtual environment:
Run migrations:
3. Start the Backend
In the same terminal (with venv activated):
API docs will be available at http://localhost:8000/docs.
4. Start the Frontend
Open a new terminal:
The app will be available at http://localhost:3000.
5. Test the Application
Login Credentials:

Admin:
Email: admin@example.com
Password: admin123
Employee:
Email: john.doe@example.com
Password: employee123
Testing Steps:

Go to http://localhost:3000.
Log in as Admin or Employee.
Test employee management, attendance, leave, payroll, performance, and admin dashboard features.
Use http://localhost:8000/docs to test API endpoints directly.
Let me know if you need troubleshooting help or want to test a specific feature!
