from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute("""create table users (
    id integer not null primary key,
    email varchar(256),
    password varchar(256),
    first_name varchar(256),
    last_name varchar(256),
    nickname varchar(256),
    created_at varchar(256)
    );""")

    session.execute("""create table auth_token (
      id integer not null primary key,
      token varchar(256),
      user_id integer references users,
      created_at varchar(256)
      );""")

    session.execute("""create table task (
      id integer not null primary key,
      user_id integer references users,
      title varchar(256),
      topic varchar(256),
      created_at varchar(256)
      );""")

    session.close()


if __name__ == '__main__':
    main()
