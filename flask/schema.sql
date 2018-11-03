DROP TABLE IF EXISTS classrooms;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS topics;


CREATE TABLE classrooms (
  room_id INTEGER UNIQUE PRIMARY KEY,
  instructor TEXT NOT NULL,
  active BOOLEAN NOT NULL
);

CREATE TABLE students (
  room_id INTEGER NOT NULL,
  student TEXT NOT NULL
  PRIMARY KEY (room_id, student)
);

CREATE TABLE topics (
  topic TEXT NOT NULL
)
