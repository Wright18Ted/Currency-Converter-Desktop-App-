## All in One Currency Converter

> [!WARNING]
> Active Development: This application is fully functional, but the user interface is still undergoing active design changes. Some features may be missing or unpolished as development continues.

# Project Description 


* Built an all-in-one desktop currency converter in Python (Tkinter) tailored for retail environments requiring fast, frequent daily currency calculations.

* Features a non-technical, user-friendly single-page UI that pairs an Ingestion & Processing calculator with an Analytics & Storage dashboard, letting staff review transaction histories and plan upcoming exchanges simultaneously.

* Integrates flat-file CSV logging with an automated ingestion pipeline to load converted currency data directly into a local PostgreSQL database.

# User Interface

The application features a dark-themed, multi-window layout built in Tkinter that breaks core functionality into focused modal windows for retail ease of use:

* **Main Converter & Historical Log:** Features a quick-entry currency conversion calculator on the left, paired with a real-time flat-file historical logging panel on the right with options to clear, download, or trigger database ingestion.
* **Exchange Rates Dashboard:** Displays live base exchange rates (GBP) across major global currencies in a clean reference table.
* **Database Ingestion Terminal:** Provides a visual terminal output window for tracking real-time status and logs when pushing CSV files into PostgreSQL.
* **Database Information Page:** Built-in onboard documentation answering common user questions, database row limits, and troubleshooting steps for non-technical staff.
* **Database Environment Setup (`.env` Config):** A quick configuration modal for managing local database connection parameters (DB Host, DB Name, DB User, and Password) dynamically.

![App Interface Overview](images/WIP_APP_LAYOUT_AUGUST_26.png)
*Figure 1: Complete application workspace showing all active modular windows.*

