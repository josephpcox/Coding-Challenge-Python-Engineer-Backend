# Coding-Challenge-Python-Engineer-Backend

Initial Set Up 

```sql
CREATE TABLE netflix_titles(
   show_id        CHAR(30) PRIMARY KEY NOT NULL,
   "type"         TEXT,
   title   		  TEXT,
   driector       TEXT,
   "cast"         TEXT,
   country        TEXT,
   date_added     TEXT,
   release_year   TEXT,
   rating         TEXT,
   duration       TEXT,
   listed_in      TEXT,
   description    TEXT
);
ALTER TABLE netflix_titles ADD COLUMN id SERIAL PRIMARY KEY;
```