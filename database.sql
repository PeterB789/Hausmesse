Entity-Relationship:
*PK, /FK

users:  *user_id, rfid, name, active
logs:   *log_id, time_stamp, /user_id



CREATE DATABASE rfid;
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    rfid BIGINT UNIQUE,
    name VARCHAR(80),
    active TINYINT(1) DEFAULT 1
    );

CREATE TABLE logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    time_stamp TIMESTAMP,
    user_id INT REFERENCES users(user_id),
    );

INSERT INTO users (rfid,name) VALUES (12345678,'peter_bischofberger');
INSERT INTO logs (time_stamp,user_id,authorized) 
	VALUES 	(CURRENT_TIMESTAMP, 
	(SELECT user_id FROM users WHERE rfid='12345678'),
	(SELECT authorized FROM users WHERE rfid='12345678')
	);

#LOGS
SELECT log_id,time_stamp,name AS Username,authorized AS 'Authorized 0=NO 1=YES' FROM logs JOIN users ON logs.user_id=users.user_id ORDER BY time_stamp DESC;

mysql -u root -ptest -D rfid -e "SELECT log_id,time_stamp,name AS Username FROM logs JOIN users ON logs.user_id=users.user_id WHERE log_id>(SELECT MAX(log_id) FROM logs)-10 ORDER BY time_stamp DESC;"
mysql -u root -ptest -D rfid -e "SELECT * FROM users;"


mysql -h mysql2ffb.netcup.net
user:   k99199_rfid-admin
pw:     kkTf709!7