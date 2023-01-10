/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 8.0.26 : Database - final
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`final` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `final`;

/*Table structure for table `albums` */

DROP TABLE IF EXISTS `albums`;

CREATE TABLE `albums` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `aname` char(20) NOT NULL,
  `bname` char(20) DEFAULT NULL,
  `release_time` date NOT NULL,
  `release_company` char(20) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `aname` (`aname`),
  KEY `album_fk` (`bname`),
  CONSTRAINT `album_fk` FOREIGN KEY (`bname`) REFERENCES `bands` (`bname`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `albums` */

insert  into `albums`(`ID`,`aname`,`bname`,`release_time`,`release_company`) values 
(1,'乐与怒','Beyond','1993-03-09','华纳唱片'),
(2,'命运派对','Beyond','1991-04-01','新艺宝唱片'),
(3,'请将手放开','Beyond','1997-04-11','滚石唱片'),
(4,'F.I.R.飞儿乐团同名专辑','飞儿乐团','2004-04-23','华纳唱片'),
(5,'飞行部落','飞儿乐团','2006-07-28','华纳唱片'),
(6,'人生海海','五月天','2001-07-06','滚石唱片'),
(7,'自传','五月天','2016-07-21','相信音乐唱片');

/*Table structure for table `bands` */

DROP TABLE IF EXISTS `bands`;

CREATE TABLE `bands` (
  `band_id` char(15) NOT NULL,
  `bname` char(20) NOT NULL,
  `leader` char(10) NOT NULL,
  `establish_time` date NOT NULL,
  `num` smallint DEFAULT NULL,
  PRIMARY KEY (`band_id`),
  UNIQUE KEY `bname` (`bname`),
  CONSTRAINT `bands_chk_1` CHECK ((`num` between 1 and 99))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `bands` */

insert  into `bands`(`band_id`,`bname`,`leader`,`establish_time`,`num`) values 
('band1','Beyond','黄家驹','1983-01-01',4),
('band2','飞儿乐团','韩睿','2002-05-01',4),
('band3','五月天','阿信','1997-03-29',5);

/*Table structure for table `concerts` */

DROP TABLE IF EXISTS `concerts`;

CREATE TABLE `concerts` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `bname` char(20) NOT NULL,
  `begin_time` datetime NOT NULL,
  `duration` char(5) NOT NULL,
  `hold_location` char(20) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `concert_uq` (`bname`,`begin_time`),
  CONSTRAINT `concert_fk` FOREIGN KEY (`bname`) REFERENCES `bands` (`bname`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `concerts` */

insert  into `concerts`(`ID`,`bname`,`begin_time`,`duration`,`hold_location`) values 
(1,'Beyond','2023-02-12 18:00:00','2小时','北京'),
(2,'飞儿乐团','2022-12-30 14:30:00','3小时','南京'),
(3,'五月天','2023-01-14 15:45:00','2.5小时','常州');

/*Table structure for table `fan_album` */

DROP TABLE IF EXISTS `fan_album`;

CREATE TABLE `fan_album` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `fan_id` char(15) NOT NULL,
  `aname` char(20) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `fan_album_UQ` (`fan_id`,`aname`),
  KEY `fan_album_fk2` (`aname`),
  CONSTRAINT `fan_album_fk1` FOREIGN KEY (`fan_id`) REFERENCES `fans` (`fan_id`),
  CONSTRAINT `fan_album_fk2` FOREIGN KEY (`aname`) REFERENCES `albums` (`aname`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fan_album` */

insert  into `fan_album`(`ID`,`fan_id`,`aname`) values 
(2,'fan1','F.I.R.飞儿乐团同名专辑'),
(1,'fan1','乐与怒'),
(3,'fan2','乐与怒'),
(4,'fan3','自传'),
(5,'fan4','人生海海'),
(6,'fan4','飞行部落'),
(7,'fan5','命运派对');

/*Table structure for table `fan_band` */

DROP TABLE IF EXISTS `fan_band`;

CREATE TABLE `fan_band` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `fan_id` char(15) NOT NULL,
  `bname` char(20) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `fan_band_UQ` (`fan_id`,`bname`),
  KEY `fan_band_fk2` (`bname`),
  CONSTRAINT `fan_band_fk1` FOREIGN KEY (`fan_id`) REFERENCES `fans` (`fan_id`),
  CONSTRAINT `fan_band_fk2` FOREIGN KEY (`bname`) REFERENCES `bands` (`bname`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fan_band` */

insert  into `fan_band`(`ID`,`fan_id`,`bname`) values 
(2,'fan1','Beyond'),
(1,'fan1','飞儿乐团'),
(4,'fan2','Beyond'),
(3,'fan3','Beyond'),
(5,'fan3','五月天'),
(6,'fan4','飞儿乐团'),
(7,'fan5','Beyond');

/*Table structure for table `fan_concert` */

DROP TABLE IF EXISTS `fan_concert`;

CREATE TABLE `fan_concert` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `fan_id` char(15) NOT NULL,
  `bname` char(20) NOT NULL,
  `begin_time` datetime NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `fan_concert_UQ` (`fan_id`,`bname`,`begin_time`),
  KEY `fan_concert_fk2` (`bname`,`begin_time`),
  CONSTRAINT `fan_concert_fk1` FOREIGN KEY (`fan_id`) REFERENCES `fans` (`fan_id`),
  CONSTRAINT `fan_concert_fk2` FOREIGN KEY (`bname`, `begin_time`) REFERENCES `concerts` (`bname`, `begin_time`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fan_concert` */

insert  into `fan_concert`(`ID`,`fan_id`,`bname`,`begin_time`) values 
(1,'fan1','Beyond','2023-02-12 18:00:00'),
(3,'fan1','飞儿乐团','2022-12-30 14:30:00'),
(2,'fan2','Beyond','2023-02-12 18:00:00'),
(4,'fan3','五月天','2023-01-14 15:45:00');

/*Table structure for table `fan_song` */

DROP TABLE IF EXISTS `fan_song`;

CREATE TABLE `fan_song` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `fan_id` char(15) NOT NULL,
  `sname` char(20) NOT NULL,
  `bname` char(20) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `fan_song_UQ` (`fan_id`,`sname`,`bname`),
  KEY `fan_song_fk2` (`sname`,`bname`),
  CONSTRAINT `fan_song_fk1` FOREIGN KEY (`fan_id`) REFERENCES `fans` (`fan_id`),
  CONSTRAINT `fan_song_fk2` FOREIGN KEY (`sname`, `bname`) REFERENCES `songs` (`sname`, `bname`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fan_song` */

insert  into `fan_song`(`ID`,`fan_id`,`sname`,`bname`) values 
(1,'fan1','光辉岁月','Beyond'),
(2,'fan1','我们的爱','飞儿乐团'),
(3,'fan2','光辉岁月','Beyond'),
(4,'fan3','海阔天空','Beyond'),
(5,'fan4','后来的我们','五月天'),
(6,'fan5','月牙湾','飞儿乐团');

/*Table structure for table `fans` */

DROP TABLE IF EXISTS `fans`;

CREATE TABLE `fans` (
  `fan_id` char(15) NOT NULL,
  `fname` char(20) NOT NULL,
  `sex` char(2) DEFAULT NULL,
  `age` smallint DEFAULT NULL,
  `occupation` char(15) DEFAULT NULL,
  PRIMARY KEY (`fan_id`),
  CONSTRAINT `fans_chk_1` CHECK ((`sex` in (_utf8mb3'男',_utf8mb3'女'))),
  CONSTRAINT `fans_chk_2` CHECK ((`age` between 6 and 120))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fans` */

insert  into `fans`(`fan_id`,`fname`,`sex`,`age`,`occupation`) values 
('fan1','曹小明','男',20,'学生'),
('fan2','易大坤','男',20,'前端工程师'),
('fan3','田贤','男',55,'厨师'),
('fan4','韩冰','女',13,'摄影师'),
('fan5','汪撕葱','男',33,'老板');

/*Table structure for table `members` */

DROP TABLE IF EXISTS `members`;

CREATE TABLE `members` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `mname` char(10) NOT NULL,
  `sex` char(2) DEFAULT NULL,
  `age` smallint DEFAULT NULL,
  `bname` char(20) NOT NULL,
  `job` char(10) DEFAULT NULL,
  `capacity` char(4) DEFAULT NULL,
  `join_time` date NOT NULL,
  `leave_time` date DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `member_fk` (`bname`),
  CONSTRAINT `member_fk` FOREIGN KEY (`bname`) REFERENCES `bands` (`bname`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `members_chk_1` CHECK ((`sex` in (_utf8mb3'男',_utf8mb3'女'))),
  CONSTRAINT `members_chk_2` CHECK ((`age` between 12 and 99)),
  CONSTRAINT `members_chk_3` CHECK ((`capacity` in (_utf8mb3'队长',_utf8mb3'队员')))
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `members` */

insert  into `members`(`ID`,`mname`,`sex`,`age`,`bname`,`job`,`capacity`,`join_time`,`leave_time`) values 
(1,'黄家驹','男',31,'Beyond','主唱','队长','1983-01-01',NULL),
(2,'黄贯中','男',58,'Beyond','吉他手','队员','1985-03-01',NULL),
(3,'黄家强','男',58,'Beyond','贝斯手','队员','1983-01-01',NULL),
(4,'叶世荣','男',59,'Beyond','鼓手','队员','1983-01-01',NULL),
(5,'韩睿','女',26,'飞儿乐团','主唱','队长','2018-10-25',NULL),
(6,'陈建宁','男',31,'飞儿乐团','键盘','队员','2002-05-01',NULL),
(7,'黄汉青','男',28,'飞儿乐团','吉他手','队员','2002-05-01',NULL),
(8,'詹雯婷','女',29,'飞儿乐团','主唱','队员','2002-05-01','2018-02-01'),
(9,'阿信','男',45,'五月天','主唱','队长','1997-03-29',NULL),
(10,'石头','男',39,'五月天','吉他手','队员','1997-03-29',NULL),
(11,'玛莎','男',35,'五月天','贝斯','队员','1998-03-15','2008-04-09'),
(12,'怪兽','男',42,'五月天','吉他手','队员','1997-03-29',NULL),
(13,'冠佑','男',41,'五月天','鼓手','队员','1997-03-29',NULL);

/*Table structure for table `sheets` */

DROP TABLE IF EXISTS `sheets`;

CREATE TABLE `sheets` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `concert_id` int DEFAULT NULL,
  `song_order` smallint NOT NULL,
  `bname` char(20) NOT NULL,
  `duration` char(5) NOT NULL,
  `sname` char(20) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `sheet_fk1` (`concert_id`),
  KEY `sheet_fk2` (`bname`),
  KEY `sheet_fk3` (`sname`),
  CONSTRAINT `sheet_fk1` FOREIGN KEY (`concert_id`) REFERENCES `concerts` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sheet_fk2` FOREIGN KEY (`bname`) REFERENCES `bands` (`bname`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sheet_fk3` FOREIGN KEY (`sname`) REFERENCES `songs` (`sname`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sheets_chk_1` CHECK ((`song_order` between 1 and 99))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sheets` */

insert  into `sheets`(`ID`,`concert_id`,`song_order`,`bname`,`duration`,`sname`) values 
(1,1,1,'Beyond','5','海阔天空'),
(2,1,2,'Beyond','5','光辉岁月'),
(3,1,3,'Beyond','3','走不开的快乐'),
(4,1,4,'Beyond','4','大时代'),
(5,1,5,'Beyond','3','和平与爱'),
(6,2,1,'飞儿乐团','5','我们的爱'),
(7,2,2,'飞儿乐团','3','千年之恋'),
(8,2,3,'飞儿乐团','2','月牙湾'),
(9,3,1,'五月天','5','后来的我们'),
(10,3,2,'五月天','6','ok啦'),
(11,3,3,'五月天','5','最好的一天');

/*Table structure for table `songs` */

DROP TABLE IF EXISTS `songs`;

CREATE TABLE `songs` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `sname` char(20) NOT NULL,
  `bname` char(20) NOT NULL,
  `aname` char(20) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `song_uq` (`sname`,`bname`),
  KEY `song_fk` (`aname`),
  KEY `song_fk2` (`bname`),
  CONSTRAINT `song_fk` FOREIGN KEY (`aname`) REFERENCES `albums` (`aname`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `song_fk2` FOREIGN KEY (`bname`) REFERENCES `bands` (`bname`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `songs` */

insert  into `songs`(`ID`,`sname`,`bname`,`aname`) values 
(1,'海阔天空','Beyond','乐与怒'),
(2,'和平与爱','Beyond','乐与怒'),
(3,'走不开的快乐','Beyond','乐与怒'),
(4,'撒旦的诅咒','Beyond','命运派对'),
(5,'光辉岁月','Beyond','命运派对'),
(6,'大时代','Beyond','请将手放开'),
(7,'回响','Beyond','请将手放开'),
(8,'我们的爱','飞儿乐团','F.I.R.飞儿乐团同名专辑'),
(9,'千年之恋','飞儿乐团','F.I.R.飞儿乐团同名专辑'),
(10,'月牙湾','飞儿乐团','飞行部落'),
(11,'一颗苹果','五月天','人生海海'),
(12,'ok啦','五月天','人生海海'),
(13,'彩虹','五月天','人生海海'),
(14,'最好的一天','五月天','自传'),
(15,'后来的我们','五月天','自传');

/* Trigger structure for table `members` */

DELIMITER $$

/*!50003 DROP TRIGGER*//*!50032 IF EXISTS */ /*!50003 `add_num_count` */$$

/*!50003 CREATE */ /*!50017 DEFINER = 'root'@'%' */ /*!50003 TRIGGER `add_num_count` AFTER INSERT ON `members` FOR EACH ROW BEGIN
	IF new.bname IS NOT NULL AND new.leave_time IS NULL 
	/*如过添加的成员所在乐队不为空，且离队时间为null，即此时还在乐队中*/
	THEN
		UPDATE bands
		SET num = (SELECT COUNT(*) FROM members WHERE bname = new.bname)
		WHERE bname = new.bname;
	END IF;
END */$$


DELIMITER ;

/* Trigger structure for table `members` */

DELIMITER $$

/*!50003 DROP TRIGGER*//*!50032 IF EXISTS */ /*!50003 `delete_num_count` */$$

/*!50003 CREATE */ /*!50017 DEFINER = 'root'@'%' */ /*!50003 TRIGGER `delete_num_count` AFTER DELETE ON `members` FOR EACH ROW BEGIN
	IF old.bname IS NOT NULL AND old.leave_time IS NULL 
	/*如离队时间为null，则还在乐队中,删除后则更新人数*/
	THEN
		UPDATE bands
		SET num = (SELECT COUNT(*) FROM members WHERE bname = old.bname)
		WHERE bname = old.bname;
	END IF;
END */$$


DELIMITER ;

/*Table structure for table `band_age` */

DROP TABLE IF EXISTS `band_age`;

/*!50001 DROP VIEW IF EXISTS `band_age` */;
/*!50001 DROP TABLE IF EXISTS `band_age` */;

/*!50001 CREATE TABLE  `band_age`(
 `age1` decimal(23,0) ,
 `age2` decimal(23,0) ,
 `age3` decimal(23,0) ,
 `age4` decimal(23,0) 
)*/;

/*Table structure for table `band_album` */

DROP TABLE IF EXISTS `band_album`;

/*!50001 DROP VIEW IF EXISTS `band_album` */;
/*!50001 DROP TABLE IF EXISTS `band_album` */;

/*!50001 CREATE TABLE  `band_album`(
 `ID` int ,
 `aname` char(20) ,
 `release_time` date ,
 `release_company` char(20) 
)*/;

/*Table structure for table `band_concert` */

DROP TABLE IF EXISTS `band_concert`;

/*!50001 DROP VIEW IF EXISTS `band_concert` */;
/*!50001 DROP TABLE IF EXISTS `band_concert` */;

/*!50001 CREATE TABLE  `band_concert`(
 `ID` int ,
 `begin_time` datetime ,
 `duration` char(5) ,
 `hold_location` char(20) 
)*/;

/*Table structure for table `band_fans` */

DROP TABLE IF EXISTS `band_fans`;

/*!50001 DROP VIEW IF EXISTS `band_fans` */;
/*!50001 DROP TABLE IF EXISTS `band_fans` */;

/*!50001 CREATE TABLE  `band_fans`(
 `fname` char(20) ,
 `sex` char(2) ,
 `age` smallint ,
 `occupation` char(15) 
)*/;

/*Table structure for table `band_favorite` */

DROP TABLE IF EXISTS `band_favorite`;

/*!50001 DROP VIEW IF EXISTS `band_favorite` */;
/*!50001 DROP TABLE IF EXISTS `band_favorite` */;

/*!50001 CREATE TABLE  `band_favorite`(
 `sname` char(20) ,
 `喜欢的人数` bigint 
)*/;

/*Table structure for table `band_own` */

DROP TABLE IF EXISTS `band_own`;

/*!50001 DROP VIEW IF EXISTS `band_own` */;
/*!50001 DROP TABLE IF EXISTS `band_own` */;

/*!50001 CREATE TABLE  `band_own`(
 `band_id` char(15) ,
 `mname` char(10) ,
 `sex` char(2) ,
 `age` smallint ,
 `job` char(10) ,
 `capacity` char(4) ,
 `join_time` date ,
 `leave_time` date 
)*/;

/*Table structure for table `band_song` */

DROP TABLE IF EXISTS `band_song`;

/*!50001 DROP VIEW IF EXISTS `band_song` */;
/*!50001 DROP TABLE IF EXISTS `band_song` */;

/*!50001 CREATE TABLE  `band_song`(
 `ID` int ,
 `bname` char(20) ,
 `sname` char(20) ,
 `release_time` date 
)*/;

/*Table structure for table `band_total_fans` */

DROP TABLE IF EXISTS `band_total_fans`;

/*!50001 DROP VIEW IF EXISTS `band_total_fans` */;
/*!50001 DROP TABLE IF EXISTS `band_total_fans` */;

/*!50001 CREATE TABLE  `band_total_fans`(
 `total_fans` bigint 
)*/;

/*Table structure for table `band_total_manfans` */

DROP TABLE IF EXISTS `band_total_manfans`;

/*!50001 DROP VIEW IF EXISTS `band_total_manfans` */;
/*!50001 DROP TABLE IF EXISTS `band_total_manfans` */;

/*!50001 CREATE TABLE  `band_total_manfans`(
 `total_man` bigint 
)*/;

/*Table structure for table `band_total_womanfans` */

DROP TABLE IF EXISTS `band_total_womanfans`;

/*!50001 DROP VIEW IF EXISTS `band_total_womanfans` */;
/*!50001 DROP TABLE IF EXISTS `band_total_womanfans` */;

/*!50001 CREATE TABLE  `band_total_womanfans`(
 `total_man` bigint 
)*/;

/*Table structure for table `fan_album_own` */

DROP TABLE IF EXISTS `fan_album_own`;

/*!50001 DROP VIEW IF EXISTS `fan_album_own` */;
/*!50001 DROP TABLE IF EXISTS `fan_album_own` */;

/*!50001 CREATE TABLE  `fan_album_own`(
 `aname` char(20) ,
 `bname` char(20) ,
 `release_time` date ,
 `release_company` char(20) 
)*/;

/*Table structure for table `fan_band_own` */

DROP TABLE IF EXISTS `fan_band_own`;

/*!50001 DROP VIEW IF EXISTS `fan_band_own` */;
/*!50001 DROP TABLE IF EXISTS `fan_band_own` */;

/*!50001 CREATE TABLE  `fan_band_own`(
 `bname` char(20) ,
 `leader` char(10) ,
 `establish_time` date ,
 `num` smallint 
)*/;

/*Table structure for table `fan_concert_own` */

DROP TABLE IF EXISTS `fan_concert_own`;

/*!50001 DROP VIEW IF EXISTS `fan_concert_own` */;
/*!50001 DROP TABLE IF EXISTS `fan_concert_own` */;

/*!50001 CREATE TABLE  `fan_concert_own`(
 `bname` char(20) ,
 `begin_time` datetime ,
 `duration` char(5) 
)*/;

/*Table structure for table `fan_own` */

DROP TABLE IF EXISTS `fan_own`;

/*!50001 DROP VIEW IF EXISTS `fan_own` */;
/*!50001 DROP TABLE IF EXISTS `fan_own` */;

/*!50001 CREATE TABLE  `fan_own`(
 `fan_id` char(15) ,
 `fname` char(20) ,
 `sex` char(2) ,
 `age` smallint ,
 `occupation` char(15) 
)*/;

/*Table structure for table `fan_song_own` */

DROP TABLE IF EXISTS `fan_song_own`;

/*!50001 DROP VIEW IF EXISTS `fan_song_own` */;
/*!50001 DROP TABLE IF EXISTS `fan_song_own` */;

/*!50001 CREATE TABLE  `fan_song_own`(
 `sname` char(20) ,
 `bname` char(20) ,
 `aname` char(20) 
)*/;

/*View structure for view band_age */

/*!50001 DROP TABLE IF EXISTS `band_age` */;
/*!50001 DROP VIEW IF EXISTS `band_age` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `band_age` (`age1`,`age2`,`age3`,`age4`) AS select sum((case when (`fans`.`age` between 6 and 18) then 1 else 0 end)) AS `6~18岁`,sum((case when (`fans`.`age` between 19 and 30) then 1 else 0 end)) AS `19~30岁`,sum((case when (`fans`.`age` between 31 and 50) then 1 else 0 end)) AS `31~51岁`,sum((case when (`fans`.`age` > 51) then 1 else 0 end)) AS `50岁以上` from ((`fan_band` join `fans`) join `bands`) where ((`bands`.`band_id` = substring_index(user(),'@',1)) and (`bands`.`bname` = `fan_band`.`bname`) and (`fan_band`.`fan_id` = `fans`.`fan_id`)) */;

/*View structure for view band_album */

/*!50001 DROP TABLE IF EXISTS `band_album` */;
/*!50001 DROP VIEW IF EXISTS `band_album` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `band_album` AS select `albums`.`ID` AS `ID`,`albums`.`aname` AS `aname`,`albums`.`release_time` AS `release_time`,`albums`.`release_company` AS `release_company` from (`bands` join `albums`) where ((`bands`.`band_id` = substring_index(user(),'@',1)) and (`bands`.`bname` = `albums`.`bname`)) WITH CASCADED CHECK OPTION */;

/*View structure for view band_concert */

/*!50001 DROP TABLE IF EXISTS `band_concert` */;
/*!50001 DROP VIEW IF EXISTS `band_concert` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `band_concert` AS select `concerts`.`ID` AS `ID`,`concerts`.`begin_time` AS `begin_time`,`concerts`.`duration` AS `duration`,`concerts`.`hold_location` AS `hold_location` from (`bands` join `concerts`) where ((`bands`.`band_id` = substring_index(user(),'@',1)) and (`concerts`.`bname` = `bands`.`bname`)) WITH CASCADED CHECK OPTION */;

/*View structure for view band_fans */

/*!50001 DROP TABLE IF EXISTS `band_fans` */;
/*!50001 DROP VIEW IF EXISTS `band_fans` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `band_fans` AS select `fans`.`fname` AS `fname`,`fans`.`sex` AS `sex`,`fans`.`age` AS `age`,`fans`.`occupation` AS `occupation` from ((`fans` join `fan_band`) join `bands`) where ((`bands`.`band_id` = substring_index(user(),'@',1)) and (`fan_band`.`fan_id` = `fans`.`fan_id`) and (`bands`.`bname` = `fan_band`.`bname`)) */;

/*View structure for view band_favorite */

/*!50001 DROP TABLE IF EXISTS `band_favorite` */;
/*!50001 DROP VIEW IF EXISTS `band_favorite` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `band_favorite` AS select `fan_song`.`sname` AS `sname`,count(0) AS `喜欢的人数` from (`fan_song` join `bands`) where ((`bands`.`band_id` = substring_index(user(),'@',1)) and (`bands`.`bname` = `fan_song`.`bname`)) group by `fan_song`.`sname` order by count(0) desc limit 1 */;

/*View structure for view band_own */

/*!50001 DROP TABLE IF EXISTS `band_own` */;
/*!50001 DROP VIEW IF EXISTS `band_own` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `band_own` AS select `bands`.`band_id` AS `band_id`,`members`.`mname` AS `mname`,`members`.`sex` AS `sex`,`members`.`age` AS `age`,`members`.`job` AS `job`,`members`.`capacity` AS `capacity`,`members`.`join_time` AS `join_time`,`members`.`leave_time` AS `leave_time` from (`members` join `bands`) where ((`bands`.`band_id` = substring_index(user(),'@',1)) and (`members`.`bname` = `bands`.`bname`)) WITH CASCADED CHECK OPTION */;

/*View structure for view band_song */

/*!50001 DROP TABLE IF EXISTS `band_song` */;
/*!50001 DROP VIEW IF EXISTS `band_song` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `band_song` AS select `songs`.`ID` AS `ID`,`songs`.`bname` AS `bname`,`songs`.`sname` AS `sname`,`albums`.`release_time` AS `release_time` from ((`songs` join `albums`) join `bands`) where ((`bands`.`band_id` = substring_index(user(),'@',1)) and (`songs`.`bname` = `bands`.`bname`) and (`songs`.`aname` = `albums`.`aname`)) WITH CASCADED CHECK OPTION */;

/*View structure for view band_total_fans */

/*!50001 DROP TABLE IF EXISTS `band_total_fans` */;
/*!50001 DROP VIEW IF EXISTS `band_total_fans` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `band_total_fans` (`total_fans`) AS select count(0) AS `COUNT(*)` from (`fan_band` join `bands`) where ((`bands`.`band_id` = substring_index(user(),'@',1)) and (`bands`.`bname` = `fan_band`.`bname`)) */;

/*View structure for view band_total_manfans */

/*!50001 DROP TABLE IF EXISTS `band_total_manfans` */;
/*!50001 DROP VIEW IF EXISTS `band_total_manfans` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `band_total_manfans` (`total_man`) AS select count(0) AS `COUNT(*)` from ((`fan_band` join `fans`) join `bands`) where ((`fan_band`.`fan_id` = `fans`.`fan_id`) and (`fans`.`sex` = '男') and (`bands`.`band_id` = substring_index(user(),'@',1)) and (`bands`.`bname` = `fan_band`.`bname`)) */;

/*View structure for view band_total_womanfans */

/*!50001 DROP TABLE IF EXISTS `band_total_womanfans` */;
/*!50001 DROP VIEW IF EXISTS `band_total_womanfans` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `band_total_womanfans` (`total_man`) AS select count(0) AS `COUNT(*)` from ((`fan_band` join `fans`) join `bands`) where ((`fan_band`.`fan_id` = `fans`.`fan_id`) and (`fans`.`sex` = '女') and (`bands`.`band_id` = substring_index(user(),'@',1)) and (`bands`.`bname` = `fan_band`.`bname`)) */;

/*View structure for view fan_album_own */

/*!50001 DROP TABLE IF EXISTS `fan_album_own` */;
/*!50001 DROP VIEW IF EXISTS `fan_album_own` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `fan_album_own` AS select `albums`.`aname` AS `aname`,`albums`.`bname` AS `bname`,`albums`.`release_time` AS `release_time`,`albums`.`release_company` AS `release_company` from (`fan_album` join `albums`) where ((`fan_album`.`fan_id` = substring_index(user(),'@',1)) and (`fan_album`.`aname` = `albums`.`aname`)) WITH CASCADED CHECK OPTION */;

/*View structure for view fan_band_own */

/*!50001 DROP TABLE IF EXISTS `fan_band_own` */;
/*!50001 DROP VIEW IF EXISTS `fan_band_own` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `fan_band_own` AS select `bands`.`bname` AS `bname`,`bands`.`leader` AS `leader`,`bands`.`establish_time` AS `establish_time`,`bands`.`num` AS `num` from (`bands` join `fan_band`) where ((`fan_band`.`fan_id` = substring_index(user(),'@',1)) and (`fan_band`.`bname` = `bands`.`bname`)) WITH CASCADED CHECK OPTION */;

/*View structure for view fan_concert_own */

/*!50001 DROP TABLE IF EXISTS `fan_concert_own` */;
/*!50001 DROP VIEW IF EXISTS `fan_concert_own` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `fan_concert_own` AS select `concerts`.`bname` AS `bname`,`concerts`.`begin_time` AS `begin_time`,`concerts`.`duration` AS `duration` from (`fan_concert` join `concerts`) where ((`fan_concert`.`fan_id` = substring_index(user(),'@',1)) and (`fan_concert`.`bname` = `concerts`.`bname`) and (`fan_concert`.`begin_time` = `concerts`.`begin_time`)) WITH CASCADED CHECK OPTION */;

/*View structure for view fan_own */

/*!50001 DROP TABLE IF EXISTS `fan_own` */;
/*!50001 DROP VIEW IF EXISTS `fan_own` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `fan_own` AS select `fans`.`fan_id` AS `fan_id`,`fans`.`fname` AS `fname`,`fans`.`sex` AS `sex`,`fans`.`age` AS `age`,`fans`.`occupation` AS `occupation` from `fans` where (`fans`.`fan_id` = substring_index(user(),'@',1)) WITH CASCADED CHECK OPTION */;

/*View structure for view fan_song_own */

/*!50001 DROP TABLE IF EXISTS `fan_song_own` */;
/*!50001 DROP VIEW IF EXISTS `fan_song_own` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `fan_song_own` AS select `fan_song`.`sname` AS `sname`,`fan_song`.`bname` AS `bname`,`songs`.`aname` AS `aname` from (`fan_song` join `songs`) where ((`fan_song`.`fan_id` = substring_index(user(),'@',1)) and (`fan_song`.`sname` = `songs`.`sname`)) WITH CASCADED CHECK OPTION */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
