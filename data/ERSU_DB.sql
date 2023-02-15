CREATE TABLE "user_settings" (
	"chat_id"	INTEGER,
	"monday_lunch"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(monday_lunch IN (0,1)),
	"monday_dinner"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(monday_dinner IN (0,1)),
	"tuesday_lunch"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(tuesday_lunch IN (0,1)),
	"tuesday_dinner"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(tuesday_dinner IN (0,1)),
	"wednesday_lunch"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(wednesday_lunch IN (0,1)),
	"wednesday_dinner"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(wednesday_dinner IN (0,1)),
	"thursday_lunch"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(thursday_lunch IN (0,1)),
	"thursday_dinner"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(thursday_dinner IN (0,1)),
	"friday_lunch"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(friday_lunch IN (0,1)),
	"friday_dinner"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(friday_dinner IN (0,1)),
	"saturday_lunch"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(saturday_lunch IN (0,1)),
	"saturday_dinner"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(saturday_dinner IN (0,1)),
	"sunday_lunch"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(sunday_lunch IN (0,1)),
	"sunday_dinner"	INTEGER(1) NOT NULL DEFAULT 0 CHECK(sunday_dinner IN (0,1)),
	PRIMARY KEY("chat_id")
);

CREATE TABLE "Articles" (
	"Title"	TEXT,
	"Time"	TEXT,
	"URL"	TEXT
);
