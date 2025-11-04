-- ## 1.2 Macros SQL

%%sql

CREATE OR REPLACE MACRO jget1(j, p) AS json_extract_string(j, p);