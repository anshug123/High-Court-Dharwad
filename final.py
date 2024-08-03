import psycopg2

conn = psycopg2.connect(database='highcourt',
                        host="localhost",
                        user="postgres",
                        password="1234",
                        port=5432)
cursor = conn.cursor()

open = True
while open:
    try:
        print("-----------------------------------")
        print("To retrieve details of all courts, enter 1.")
        print("To retrieve judges in a specific court, enter 2.")
        print("To retrieve details of a specific case, enter 3.")
    
        print("To update status(pending/running/end) of case, enter 4.")
        print("To insert a new client into the Clients table, enter 5.")
        print("To delete a lawyer, enter 6.")
        print("To retrieve a lawyer who has handled the most cases, enter 7.")
        print("To retrieve details of all lawyers, enter 8.")
        print("To delete a case and its associated data, enter 9.")
        print("To retrieve number of cases handled by each lawyer, enter 10.")
#-----------------------------------------------------------------------------------------------
        print("To retrieve clients for a specific case, enter 11.")
        print("To retrieve lawyers for a specific case, enter 12.")
        print("To retrieve investigation officers for a specific case, enter 13.")
        print("To retrieve evidences for a specific case, enter 14.")
#----------------------------------------------------------------------------------------------
        print("To insert a new court into the Courts table, enter 15.")
        print("To insert a new case into the Cases table with an assigned judge and court, enter 16.")
        print("To delete a specific judge, enter 17.")
        print("To close the session, enter 0.")
        print("-----------------------------------")

        
        
        
        
        
        k=int(input ("Enter the Query Number:"))
        if k == 0:
            open =False
        elif k ==1:
            cursor.execute('SELECT * FROM Courts')
            courts = cursor.fetchall()
            print("All Courts:")
            for court in courts:
                print(court)
        elif k == 2:
            l = input("Enter the court_id: ")
            cursor.execute('SELECT * FROM Judges WHERE Court_ID = %s;', (l,))
            judges = cursor.fetchall()
            if cursor.rowcount == 0:
                print(f"No court with ID {l} found in the database.")
            else:
                print("\nJudges in Court:")
                for judge in judges:
                    print(judge)

        elif k == 3:
            l = input("Enter the case_id for details: ")
            cursor.execute('SELECT * FROM Cases WHERE Case_ID = %s;', (l,))
            cases = cursor.fetchall()
            if cursor.rowcount == 0:
                print(f"No case with ID {l} found in the database.")
            else:
                print("\nDetails of the Case:")
                for case in cases:
                    print(case)

        elif k == 4:
            l = input("Enter the case_id to update:")
            x = input("Enter the new status(running/pending/end):")
            sql = 'UPDATE Cases SET Status = %s WHERE Case_ID = %s;'
            cursor.execute(sql, (x, l))
            if cursor.rowcount == 0:
                print(f"No case with ID {l} found in the database.")
            else:
                conn.commit()
                print("Status Updated to " + x)

        elif k==5:
            print("Give details of new client to insert.")
            l1=input("Client_ID: ")
            l2=input("Name:" )
            l3=input("Age :" )
            l4=input("Gender:" )
            l5=input("Contact_Number :" )
            l6=input("Address :" )
            cursor.execute("begin;") 
            cursor.execute("select * from Clients where Client_id = " + l1 + ";")
            if cursor.fetchall() == []:
                
                cursor.execute("insert into Clients values" + "(" + l1 + ", '" + l2 + "', '" + l3 + "', '" + l4+ "', '" + l5+ "', '" + l6+ "' )" + ";")
                conn.commit()
                print("Client details inserted into the client table successfully.")
            else:
                conn.rollback()
                print("Client ID already exists.")
        elif k==6:
            lawyer_id = input("Enter the Lawyer's ID to delete: ")

            try:
                # Delete the lawyer's details from the database
                cursor.execute("DELETE FROM Lawyers WHERE Lawyer_ID = %s", (lawyer_id,))
                if cursor.rowcount == 0:
                    print(f"No lawyer with ID {lawyer_id} found in the database.")
                else:
                    conn.commit()
                    print("Lawyer details deleted successfully.")
            except psycopg2.Error as e:
                conn.rollback()
                print("Error deleting lawyer details:", e)

        elif k==7:
            # sql_query = """
            # SELECT Lawyers.Lawyer_ID, Lawyers.Name, COUNT(Cases.Case_ID) AS CasesSolved
            # FROM Lawyers
            # LEFT JOIN CaseLawyers ON Lawyers.Lawyer_ID = CaseLawyers.Lawyer_ID
            # LEFT JOIN Cases ON CaseLawyers.Case_ID = Cases.Case_ID
            # GROUP BY Lawyers.Lawyer_ID, Lawyers.Name
            # HAVING COUNT(Cases.Case_ID) = (SELECT MAX(CasesSolved) FROM (SELECT COUNT(Cases.Case_ID) AS CasesSolved FROM Lawyers LEFT JOIN CaseLawyers ON Lawyers.Lawyer_ID = CaseLawyers.Lawyer_ID LEFT JOIN Cases ON CaseLawyers.Case_ID = Cases.Case_ID GROUP BY Lawyers.Lawyer_ID) AS SubQuery)
            # ORDER BY CasesSolved DESC;

            # """
            # try:
            #     # Execute the query
            #     cursor.execute(sql_query)

            #     # Fetch the result
            #     results = cursor.fetchone()

            #     if results:
            #         for result in results:
            #             lawyer_id, lawyer_name, cases_solved = result
            #             print(f"Lawyer ID: {lawyer_id}")
            #             print(f"Lawyer Name: {lawyer_name}")
            #             print(f"Cases Solved: {cases_solved}")
            #     else:
            #         print("No data found.")

            # except (Exception, psycopg2.Error) as error:
            #     print(f"Error: {error}")
            sql_query = """
                SELECT Lawyers.Lawyer_ID, Lawyers.Name, COUNT(Cases.Case_ID) AS CasesSolved
                FROM Lawyers
                LEFT JOIN CaseLawyers ON Lawyers.Lawyer_ID = CaseLawyers.Lawyer_ID
                LEFT JOIN Cases ON CaseLawyers.Case_ID = Cases.Case_ID
                GROUP BY Lawyers.Lawyer_ID, Lawyers.Name
                HAVING COUNT(Cases.Case_ID) = (
                    SELECT MAX(CasesSolved)
                    FROM (
                        SELECT COUNT(Cases.Case_ID) AS CasesSolved
                        FROM Lawyers
                        LEFT JOIN CaseLawyers ON Lawyers.Lawyer_ID = CaseLawyers.Lawyer_ID
                        LEFT JOIN Cases ON CaseLawyers.Case_ID = Cases.Case_ID
                        GROUP BY Lawyers.Lawyer_ID
                    ) AS SubQuery
                )
                ORDER BY CasesSolved DESC;
            """

            try:
                # Execute the query
                cursor.execute(sql_query)

                # Fetch all the results
                results = cursor.fetchall()

                if results:
                    for i, result in enumerate(results, start=1):
                        lawyer_id, lawyer_name, cases_solved = result
                        print(f"Top Lawyer {i}:")
                        print(f"Lawyer ID: {lawyer_id}")
                        print(f"Lawyer Name: {lawyer_name}")
                        print(f"Cases Solved: {cases_solved}")
                else:
                    print("No data found.")

            except (Exception, psycopg2.Error) as error:
                print(f"Error: {error}")


        elif k==8:
            cursor.execute('SELECT * FROM Lawyers')
            lawyers = cursor.fetchall()
            print("\nAll Lawyers:")
            for lawyer in lawyers:
                print(lawyer)
        elif k==9:
            
            # case_id = input("Enter the case ID and data associated  you want to delete: ")
            # cursor.execute("begin;") 
            # try:

            #     cursor.execute("DELETE FROM Cases WHERE Case_ID = %s", (case_id,))
            #     conn.commit()
            #     print("case details deleted successfully.")
            # except psycopg2.Error as e:
            #     conn.rollback()
            #     print("Error deleting case details:", e)
            case_id = input("Enter the Case ID you want to delete: ")
            cursor.execute("BEGIN;") 
            cursor.execute("SELECT 1 FROM Cases WHERE Case_ID = %s", (case_id,))
            if cursor.fetchone():
                try:
                    cursor.execute("DELETE FROM Cases WHERE Case_ID = %s", (case_id,))
                    conn.commit()
                    print("Case with ID", case_id, "deleted successfully.")
                except psycopg2.Error as e:
                    conn.rollback()
                    print("Error deleting case details:", e)
            else:
                conn.rollback()
                print("Case with ID", case_id, "does not exist in the table.")

        elif k==10:
            cursor.execute('SELECT Lawyers.Name, COUNT(CaseLawyers.Case_ID) FROM Lawyers LEFT JOIN CaseLawyers ON Lawyers.Lawyer_ID = CaseLawyers.Lawyer_ID GROUP BY Lawyers.Name')
            lawyer_case_counts = cursor.fetchall()
            print("\nTotal number of cases handled by each lawyer:")
            for lawyer_count in lawyer_case_counts:
                print(f"{lawyer_count[0]}: {lawyer_count[1]} cases")
        elif k == 11:
            case_id = input("Enter the Case_ID to retrieve clients:")
            cursor.execute('SELECT Clients.Name FROM Clients INNER JOIN ClientsCases ON Clients.Client_ID = ClientsCases.Client_ID WHERE ClientsCases.Case_ID = %s;', (case_id,))
            clients = cursor.fetchall()
            if cursor.rowcount == 0:
                print(f"No case with ID {case_id} found in database.")
            else:
                print("\nClients for Case " + case_id + ":")
                for client in clients:
                    print(client[0])

        elif k == 12:
            case_id = input("Enter the Case_ID to retrieve lawyers:")
            cursor.execute('SELECT Lawyers.Name FROM Lawyers INNER JOIN CaseLawyers ON Lawyers.Lawyer_ID = CaseLawyers.Lawyer_ID WHERE CaseLawyers.Case_ID = %s;', (case_id,))
            lawyers = cursor.fetchall()
            if cursor.rowcount == 0:
                print(f"No case with ID {case_id} found in database.")
            else:
                print("\nLawyers for Case " + case_id + ":")
                for lawyer in lawyers:
                    print(lawyer[0])

        elif k == 13:
            case_id = input("Enter the Case_ID to retrieve investigation officers:")
            cursor.execute('SELECT InvestigatingOfficers.Name FROM InvestigatingOfficers INNER JOIN CaseOfficers ON InvestigatingOfficers.Officer_ID = CaseOfficers.Officer_ID WHERE CaseOfficers.Case_ID = %s;', (case_id,))
            officers = cursor.fetchall()
            if cursor.rowcount == 0:
                print(f"No case with ID {case_id} found in database.")
            else:
                print("\nInvestigating Officers for Case " + case_id + ":")
                for officer in officers:
                    print(officer[0])
                    
        elif k==14:
            case_id=input("Enter the Case_ID to retrieve evidences:")    
            cursor.execute("SELECT * FROM Evidence WHERE Case_ID = "+case_id+";")
            evidences = cursor.fetchall()
            if cursor.rowcount == 0:
                print(f"No case with ID {case_id} found in database.")
            else:
                print("\nEvidences for Case:" + case_id+":")
                for evidence in evidences:
                    print(evidence)
        elif k==15:
            print("Give details of new court to insert.")
            l1 = input("Court_ID: ")
            l2 = input("Court_Name: ")
            l6 = input("Location: ")

            cursor.execute("BEGIN;")
            cursor.execute("SELECT * FROM Courts WHERE Court_ID = " + l1 + ";")

            if cursor.fetchall() == []:
                cursor.execute("INSERT INTO Courts (Court_ID, Court_Name, Location) VALUES (" + l1 + ", '" + l2 + "', '" + l6 + "');")
                conn.commit()
                print("Court details inserted into the Courts table successfully.")
            else:
                conn.rollback()
                print("Court ID already exists.")
        
        elif k==16:
            print("Give details of new case to insert.")
            l1=input("Case_ID: ")
            l2=input("Case_Type(civil/criminal):" )
            l3=input("Filing_Date(YYYY-MM-DD):" )
            l4=input("Status(pending/running/end):" )
            l5=input("Judge_ID:" )
            l6=input("Court_ID:" )
            cursor.execute("begin;") 
        
            cursor.execute("select * from Cases where Case_id = " + l1 + ";")
            if cursor.fetchall() == []:
                
                
                cursor.execute("insert into Cases values" + "(" + l1 + ", '" + l2 + "', '" + l3 + "', '" + l4+ "', '" + l5+ "', '" + l6+ "' )" + ";")
                conn.commit()
                print("New case details inserted into the cases table successfully.")
            else:
                conn.rollback()
                print("Case ID already exists") 
        elif k==17:
            judge_id = input("Enter the Judge's ID to delete: ")
            cursor.execute("begin;") 

            cursor.execute("SELECT 1 FROM Judges WHERE Judge_ID = %s", (judge_id,))
            if cursor.fetchone():
                try:
                    cursor.execute("DELETE FROM Judges WHERE Judge_ID = %s", (judge_id,))
                    conn.commit()
                    print("Judge details with ID", judge_id, "deleted successfully.")
                except psycopg2.Error as e:
                    conn.rollback()
                    print("Error deleting judge details:", e)
            else:
                conn.rollback()
                print("Judge with ID", judge_id, "does not exist in the table.")

            

            
        else:
            print("Choose number between 0 to 17.")
    except Exception as e:
      print(e)
      continue
                
conn.close()   