SQL> SELECT DBMS_METADATA.GET_DDL('TABLE', table_name, user) FROM user_tables;

DBMS_METADATA.GET_DDL('TABLE',TABLE_NAME,USER)                                  
--------------------------------------------------------------------------------
                                                                                
  CREATE TABLE "BANK_ADMIN"."BANKS"                                             
   (	"BANK_ID" NUMBER GENERATED BY DEFAULT                                      
                                                                                
                                                                                
  CREATE TABLE "BANK_ADMIN"."REVIEWS"                                           
   (	"REVIEW_ID" NUMBER GENERATED BY DEF                                        
                                                                                
SQL> ELECT 'INSERT INTO ' || table_name || ' VALUES (...);' FROM user_tables;
SP2-0734: unknown command beginning "ELECT 'INS..." - rest of line ignored.
SQL> SELECT 'INSERT INTO ' || table_name || ' VALUES (...);' FROM user_tables;

'INSERTINTO'||TABLE_NAME||'VALUES(...);'                                        
--------------------------------------------------------------------------------
INSERT INTO BANKS VALUES (...);                                                 
INSERT INTO REVIEWS VALUES (...);                                               
SQL> SPOOL OFF;
