-- create tables
create table pickem_role (
    id serial primary key,
    name varchar(50) not null,
    description varchar(140),
    can_manage_user boolean,
    can_manage_league boolean,
    can_manage_game boolean,
    can_manage_picks boolean
);

create table pickem_user (
    username varchar(50) primary key,
    email_address varchar(50) not null,
    password varchar(50) not null,
    prefix varchar(5),
    first_name varchar(50) not null,
    middle_initial char(1),
    last_name varchar(50),
    suffix varchar(5),
    photo varchar(140),
    role_id int references pickem_role (id),
    log_time timestamp default now()
);

create table team (
	id serial primary key,
    name varchar(50) not null,
    nickname varchar(50),
    abbreviation varchar(10),
    wins int default 0,
    losses int default 0,
    ties int default 0,
    photo varchar(140),
    notes varchar(140),
    log_time timestamp default now()
);

create table game (
    id serial primary key,
    home_team_id int references team (id),
    away_team_id int references team (id),
    is_conference_game boolean,
    is_neutral_site boolean,
    home_score int,
    away_score int,
    begin_time timestamp,
    notes varchar(140),
    is_final boolean,
    log_time timestamp default now()
);

create table pick (
    id serial primary key,
    game_id int references game (id),
    username varchar(50) references pickem_user (username),
    team_id int references team (id),
    log_time timestamp default now()
);
