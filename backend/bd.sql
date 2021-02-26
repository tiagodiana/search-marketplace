create table researches (
    id int primary key auto_increment,
    ip_address varchar (255),
    site varchar (255),
    type varchar (40),
    query varchar (255),
    result text,
    create_date datetime default now(),
    update_date datetime
) engine=innodb;