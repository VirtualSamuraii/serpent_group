CREATE TABLE hosts (
	host_id INTEGER NOT NULL PRIMARY KEY,
	hostname TEXT NOT NULL,
	hash TEXT NOT NULL DEFAULT "",
	os TEXT DEFAULT 'windows',
	ip TEXT
);


CREATE TABLE commands (
	command_id INTEGER NOT NULL PRIMARY KEY,
	command TEXT NOT NULL,
	answer TEXT NULL,
	answer_time DATETIME NULL,
	status INTEGER NULL DEFAULT 0,
	fk_host_id INTEGER NOT NULL, answer_url TEXT NULL,
	FOREIGN KEY (fk_host_id) REFERENCES hosts(host_id)
);
