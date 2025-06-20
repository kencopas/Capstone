# Set of file extenstions that are supported for ETL processes
SUPPORTED_EXTENSIONS = {".json", ".csv"}

# Path to the MySQL jdbc jar file
MYSQL_JAR_PATH = r"./lib/mysql-connector-j-9.3.0.jar"

# Spark-MySQL jdbc connector driver
JDBC_DRIVER = "com.mysql.cj.jdbc.Driver"

# Url for MySQL jdbc connector, hostname and port placeholders
JDBC_URL = "jdbc:mysql://{hostname}:{port}/creditcard_capstone"

# API url for the loan dataset
LOAN_API_URL = (
    r"https://raw.githubusercontent.com/platformps/"
    r"LoanDataset/main/loan_data.json"
)

# Regex patterns for input validation by input type
VALIDATIONS = {
    "name": r"^[A-Za-z]{1,50}$",
    "CCN": r"^\d{16}$",
    "SSN": r"^\d{9}$",
    "address": r"^[0-9A-Za-z\s.,#'-]{5,100}$",
    "city": r"^[A-Za-z\s-]{1,100}$",
    "state": r"^[A-Z]{2}$",
    "country": r"^[A-Za-z\s]{2,100}$",
    "zip": r"^\d{5}$",
    "phone_number": r"\(\d{3}\)\d{3}-\d{4}",
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "mmyyyy": r"^(0[1-9]|1[0-2])-\d{4}$",
    "mmddyyyy": r"^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-\d{4}$"
}
