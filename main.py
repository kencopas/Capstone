import os
import sys

from dotenv import load_dotenv
import findspark
findspark.init()
from pyspark.sql import SparkSession

from utils.sql import SafeSQL
from app.menu import CLIManager
from app.data_client import DataClient


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

        # Load the configuration and verify the python version
        load_dotenv()
        # self.verify_version()

        # Create the SparkSession
        self.spark = SparkSession.builder \
            .appName(app_name) \
            .config("spark.jars", os.getenv('MYSQL_JAR')) \
            .config("spark.driver.bindAddress", "127.0.0.1") \
            .config("spark.driver.host", "127.0.0.1") \
            .config("spark.driver.port", "4041") \
            .config("spark.driver.memory", "4g") \
            .getOrCreate()

        # Set the log level
        self.spark.sparkContext.setLogLevel(log.upper())

        # Initialize SafeSQL connection
        self.sql = SafeSQL(
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("MYSQL_HOST")
        )

        # Initialize the DataClient and run the pipeline
        self.dc = DataClient(self.spark, self.sql)
        self.dc.pipeline()

        # Initialize and run the CLIManager
        self.cli = CLIManager(self.dc)
        self.cli.run()

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
