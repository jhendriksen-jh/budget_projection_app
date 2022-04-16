# budget_projection_app
A tailor made for me budgeting app that tracks budget related items and can create savings projections based off user input parameters.

# Purpose/Goals
Budgeting is important both to avoid excess spending and to develop a firm understanding of your financial situation. As I approach a time in my life where signficant financial plans/decisions must be made (house/cars/etc.) I wanted to build something that would provide me with the information I want.
 - Ability to track account balances (user input based off name, number, date)
 - Categorize spending (user input)
 - Create projections for savings with confidence range
 - Compare user performance on a chosen basis (week, month, quarter, year)
     - vs their decided upon budget
     - vs previous months
     - vs projections
  
# Methods
- Build into an executable
  - More user friendly (dictates how seriously used)
  - PyInstaller (directory or single file executables)
- GUI with multiple input options and display of projections/performance
  - Kivy: high cross platform support
  - I would be fine with command line use but would make more difficult to use and cause barrier to usage
- User based data storage
  - Store data locally + local run of app = should not be security issues (no important info anyway)
  - User based so multiple could use app on same computer if want
  - (how to save data in a way it's not erased when "upgrading" app)
