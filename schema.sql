drop table if exists message;
create table entries (
  id integer primary key autoincrement,
  user string not null,
  text string not null
);