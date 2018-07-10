
drop table user;
drop table  test;
create table user (
  id int unsigned not null auto_increment comment '自增id',
  user_id varchar(30) not null default '' comment '用户id，全英文:bedtimepoem',
  user_nickname varchar(30) not null default '' comment '用户昵称',
  signature varchar(50) not null default ''  comment ' 签名',
  location varchar(20) default '' comment '用户居住地址',
  check_in_time varchar(30) default '' comment '加入时间',
  user_intro varchar(200) comment '简介',
  books_wanted varchar(200) not null default '' comment '想读',
  books_red varchar(200) not  null default '' comment '已读',
  movies_wanted varchar(200) not null default '' comment '想看',
  movies_watched varchar(200) not  null default '' comment '看过',
  groups varchar(200) not null default '' comment '加入的小组',
  dou_list varchar(300) not null default '',
  create_dttm timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  primary key (id)
)ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COMMENT='用户表';