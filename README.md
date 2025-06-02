# Capstone Project

## Overview

This Capstone Project is designed to manage an ETL process for a bank dataset. The main components of this application are an ETL Pipeline, Command Line Interface, and [Tableau Dashboard](https://public.tableau.com/views/CustomerDataDashboard_17484417707510/CustomerDataDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Repository Structure

- **`app/`**: Contains the main application components (Data Client & CLI).
- **`config/`**: Holds configuration files and settings.
- **`data/`**: Includes datasets and data-related resources.
- **`dev/`**: Development scripts and tools.
- **`docs/`**: Documentation and related materials.
- **`lib/`**: Library modules and utilities.
- **`sql/`**: SQL scripts for database setup and queries.
- **`utils/`**: Helper functions and utilities.
- **`main.py`**: The main entry point of the application.
- **`requirements.txt`**: Lists all Python dependencies.

## Getting Started

### Prerequisites

- Python 3.8 or higher (3.8-3.11 recommended)
- MySQL
- Apache Spark

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kencopas/Capstone.git
   cd Capstone
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the main application:

```bash
spark-submit main.py
```

Before running on your local machine, update the config.json file to match your MySQL and PySpark configurations

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeatureName`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeatureName`
5. Open a pull request.

## Contact

For questions or suggestions, please contact Kenneth Copas at [kenny@copas.net](mailto:kenny@copas.net).
