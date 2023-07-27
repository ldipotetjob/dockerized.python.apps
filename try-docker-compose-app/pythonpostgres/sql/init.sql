
GRANT ALL PRIVILEGES ON DATABASE genhub TO genhub;
CREATE TABLE genhubrequest (
  userId text NOT NULL,
  request_time timestamp NOT NULL,
  requestid text NOT NULL,
  requested_samples int NOT NULL,
  available_samples int NOT NULL ,
  payable boolean,
  status text NOT NULL,
  PRIMARY KEY (requestid)
);

INSERT INTO genhubrequest values ('petergabriel@email.net','2022-10-19 10:23:54','petergabriel@email.net1666171434',50,60,true,'not started');
INSERT INTO genhubrequest values ('sebbatch@mail.com','2022-11-23 10:23:54','jfdz@gmaila.com1668853417',150,70,true,'not started');
