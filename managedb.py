from foobar.database import mydatabase


def main():
    dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname="mydb.sqlite")
    # dbms.create_db_tables()
    dbms.print_all_data(mydatabase.USERS)
    # dbms.sample_insert()

if __name__ == "__main__":
    main()
