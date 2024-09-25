
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

INSERT INTO genhubrequest values ('petergabriel@email.net','2024-06-14 13:10:59','petergabriel@email.net_1718367059812',50,60,true,'not started');
INSERT INTO genhubrequest values ('lennykravitz@gmail.com','2024-06-14 13:11:57','lennykravitz@gmail.com_1718367117788',150,70,true,'not started');
