import os
import sys
from getpass import getpass

from dotenv import load_dotenv
import findspark
findspark.init()
from pyspark.sql import SparkSession

from utils.sql import SafeSQL
from app.menu import CLIManager
from app.data_client import DataClient
from config.constants import MYSQL_JAR_PATH, JDBC_URL


class Application:
    """
    Manages the ETL process for a bank dataset using PySpark, MySQL,
    and a CLI interface.

    This class initializes a SparkSession, sets up secure SQL access, runs an
    ETL pipeline, and launches a command-line interface for user interaction.
    It also verifies Python version compatibility between the application and
    PySpark environment.

    Methods:
        verify_version(pyspark_python: str):
            Verifies the application and PySpark Python versions are compatible
    """

    def __init__(self, app_name: str, *, log: str) -> None:

        # Load the .env file if it exists
        load_dotenv()

        # Retrieve the MySQL configurations from env variables
        mysql_config = self.get_config()

        # Create the SparkSession
        self.spark = SparkSession.builder \
            .appName(app_name) \
            .config("spark.jars", MYSQL_JAR_PATH) \
            .getOrCreate()

        # Set the log level
        self.spark.sparkContext.setLogLevel(log.upper())

        # Initialize SafeSQL connection
        self.mysql_connect(mysql_config)

        # Initialize the DataClient and run the pipeline
        self.dc = DataClient(self.spark, self.sql)
        self.dc.pipeline()

        # Initialize and run the CLIManager
        self.cli = CLIManager(self.dc)
        self.cli.run()

    def mysql_connect(self, config):
        while True:
            try:
                self.sql = SafeSQL(**config)
                break
            except Exception:
                print(
                    "Failed to connect to MySQL with the following configurations:\n\n"
                    f"Username: {config['user']}\n"
                    f"JDBC url: {os.getenv['JDBC_URL']}\n\n"
                )

    # Prompts the user for MySQL username and password if not provided
    def get_config(self) -> dict[str: str]:

        # Required environment variables for MySQL configuration
        required_vars = {
            'MYSQL_USER': 'MySQL username',
            'MYSQL_PASSWORD': 'MySQL password',
            'MYSQL_HOST': 'MySQL hostname (X.X.X.X)'
        }

        # Initialize config dict
        config = {}

        # For each variable, prompt for the value if necessary
        for var_name in required_vars.keys():
            if os.getenv(var_name):
                val = os.getenv(var_name)
            else:
                val = getpass(f"Please enter {required_vars[var_name]}: ")
            os.environ[var_name] = val
            config.update({var_name.split('_')[-1].lower(): val})

        # If jdbc_url env variable doesn't exist, prompt for port number
        if not os.getenv('JDBC_URL'):
            port = getpass("Please enter MySQL port number: ")
            host = config['host']

            if host == '127.0.0.1':
                host = 'localhost'

            # Construct the jdbc url with the hostname and port number
            os.environ['JDBC_URL'] = JDBC_URL.format(hostname=host, port=port)

        return config

    # Print a warning if the python version being run is not 3.8-3.11
    def verify_version(self) -> None:

        # Set the environment variable to the pyspark python version being used
        pyspark_python = os.getenv('PYTHONPATH')
        os.environ['PYSPARK_PYTHON'] = pyspark_python

        # Retrieve the version running the script
        pyspark_version = sys.version[:6]
        version_num = int(pyspark_version[2:4])

        # Check if either version is not fully compatible
        if not 8 <= version_num <= 11:
            ans = input(
                f"\nPossibly Incompatible Python version: {pyspark_version}" +
                "\nReccomended Versions: 3.8-3.11" +
                "\nWould you like to continue? Y | N\n"
            )
            if ans.lower().strip() != "y":
                exit(0)


if __name__ == "__main__":

    myapp = Application("Capstone ETL Manager", log="OFF")
