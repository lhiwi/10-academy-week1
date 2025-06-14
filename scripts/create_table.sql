-- Drop tables if they exist to start fresh
BEGIN
  EXECUTE IMMEDIATE 'DROP TABLE reviews CASCADE CONSTRAINTS';
EXCEPTION
  WHEN OTHERS THEN
    IF SQLCODE != -942 THEN RAISE; END IF;
END;
/

BEGIN
  EXECUTE IMMEDIATE 'DROP TABLE banks CASCADE CONSTRAINTS';
EXCEPTION
  WHEN OTHERS THEN
    IF SQLCODE != -942 THEN RAISE; END IF;
END;
/

-- Create BANKS table
CREATE TABLE banks (
  bank_id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
  name VARCHAR2(100) NOT NULL
);

-- Insert distinct banks (optional if handled via script)
INSERT INTO banks (name) VALUES ('Commercial Bank of Ethiopia');
INSERT INTO banks (name) VALUES ('Bank of Abyssinia');
INSERT INTO banks (name) VALUES ('Dashen Bank');

COMMIT;

-- Create REVIEWS table with foreign key
CREATE TABLE reviews (
  review_id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
  bank_id NUMBER NOT NULL,
  review_text CLOB,
  rating NUMBER(2,1),
  review_date DATE,
  source VARCHAR2(100),
  CONSTRAINT fk_bank FOREIGN KEY (bank_id) REFERENCES banks(bank_id)
);

-- Optional sample inserts (can be removed in production)
INSERT INTO reviews (bank_id, review_text, rating, review_date, source)
VALUES (1, 'Great mobile banking experience.', 4.5, TO_DATE('2025-06-07', 'YYYY-MM-DD'), 'Google Play');

INSERT INTO reviews (bank_id, review_text, rating, review_date, source)
VALUES (2, 'App crashes too often.', 2.0, TO_DATE('2025-06-06', 'YYYY-MM-DD'), 'Google Play');

INSERT INTO reviews (bank_id, review_text, rating, review_date, source)
VALUES (3, 'Needs better UI design.', 3.0, TO_DATE('2025-06-05', 'YYYY-MM-DD'), 'App Store');

COMMIT;
