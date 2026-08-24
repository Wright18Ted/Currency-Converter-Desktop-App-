## All in One Currency Converter

> [!WARNING]
> Active Development: This application is fully functional, but the user interface is still undergoing active design changes. Some features may be missing or unpolished as development continues.

# Project Description 


* Built an all-in-one desktop currency converter in Python (Tkinter) tailored for retail environments requiring fast, frequent daily currency calculations.

* Features a non-technical, user-friendly single-page UI that pairs an Ingestion & Processing calculator with an Analytics & Storage dashboard, letting staff review transaction histories and plan upcoming exchanges simultaneously.

* Integrates flat-file CSV logging with an automated ingestion pipeline to load converted currency data directly into a local PostgreSQL database.

# User Interface

## User Interface

The application features a dark-themed, multi-window layout built in Tkinter that breaks core functionality into focused modal windows for retail ease of use:

* **Main Converter & Historical Log:** A dual-pane home window featuring a quick-entry currency conversion calculator on the left, paired with a real-time flat-file historical logging window on the right with options to clear, download, or trigger automated database ingestion.
* **Exchange Rates Dashboard:** A dedicated pop-up window displaying live base exchange rates (GBP) across major global currencies for quick reference during transaction planning.
* **Database Ingestion Terminal:** An automated upload utility window providing visual terminal feedback when pushing stored CSV log files directly into the local PostgreSQL database.
* **Database Environment Setup (`.env` Config):** A quick configuration modal for managing local database connection parameters (DB Host, DB Name, DB User, and Password) dynamically without altering source code.

![App Interface Overview](Images/WIP_APP_LAYOUT_AUGUST_26.png)
*Figure 1: Application workspace showing the main converter, live rate board, DB ingestion terminal, and environment setup window.*

