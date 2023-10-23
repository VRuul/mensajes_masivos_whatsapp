// #include <mysql_driver.h>
// #include <mysql_connection.h>
// #include <cppconn/resultset.h>
// #include <cppconn/statement.h>
#include <mysqlcppconn-9-vs14.dll>
#include <mysqlcppconn8-2-vs14.dll>

int main() {
    sql::mysql::MySQL_Driver *driver;
    sql::Connection *con;

    try {
        driver = sql::mysql::get_mysql_driver_instance();
        con = driver->connect("tcp://82.180.174.52:3306", "u636070509_root", "VRuul2000");
        con->setSchema("u636070509_BD_Xv");

        sql::Statement *stmt;
        sql::ResultSet *res;

        stmt = con->createStatement();
        res = stmt->executeQuery("SELECT * FROM invitados");

        while (res->next()) {
            std::cout << "Columna1: " << res->getString(1) << ", Columna2: " << res->getString(2) << std::endl;
        }

        delete res;
        delete stmt;
        delete con;
    } catch (sql::SQLException &e) {
        std::cout << "Error de MySQL: " << e.what() << std::endl;
    }

    return 0;
}
