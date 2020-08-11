-- MariaDB dump 10.17  Distrib 10.4.13-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: SE
-- ------------------------------------------------------
-- Server version	10.4.13-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `content` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `author_gid` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `stars` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`),
  KEY `author_gid` (`author_gid`),
  CONSTRAINT `answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`),
  CONSTRAINT `answer_ibfk_2` FOREIGN KEY (`author_gid`) REFERENCES `user` (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answer_up_vote`
--

DROP TABLE IF EXISTS `answer_up_vote`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer_up_vote` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer_id` int(11) DEFAULT NULL,
  `user_gid` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `answer_id` (`answer_id`),
  KEY `user_gid` (`user_gid`),
  CONSTRAINT `answer_up_vote_ibfk_1` FOREIGN KEY (`answer_id`) REFERENCES `answer` (`id`),
  CONSTRAINT `answer_up_vote_ibfk_2` FOREIGN KEY (`user_gid`) REFERENCES `user` (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer_up_vote`
--

LOCK TABLES `answer_up_vote` WRITE;
/*!40000 ALTER TABLE `answer_up_vote` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer_up_vote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assignment`
--

DROP TABLE IF EXISTS `assignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `assignment` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) DEFAULT NULL,
  `title` varchar(63) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `due` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `schedule_id` (`schedule_id`),
  CONSTRAINT `assignment_ibfk_1` FOREIGN KEY (`schedule_id`) REFERENCES `schedule` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assignment`
--

LOCK TABLES `assignment` WRITE;
/*!40000 ALTER TABLE `assignment` DISABLE KEYS */;
INSERT INTO `assignment` VALUES (1590685733,1,1,1,'123',938000013);
/*!40000 ALTER TABLE `assignment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `name_zh` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name_en` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `intro` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pre_course` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `textbooks` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `semester` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1590683794,1,2,'软件工程','jisuanke','hi','ads','dcx','ad'),(1591092844,1,3,'软件工程','jisuanke','hi','ads','dcx','ad');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course_resource`
--

DROP TABLE IF EXISTS `course_resource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course_resource` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data` blob DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `course_resource_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_resource`
--

LOCK TABLES `course_resource` WRITE;
/*!40000 ALTER TABLE `course_resource` DISABLE KEYS */;
/*!40000 ALTER TABLE `course_resource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discussion_answer`
--

DROP TABLE IF EXISTS `discussion_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discussion_answer` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic_id` int(11) DEFAULT NULL,
  `content` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `author_gid` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `reply_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `topic_id` (`topic_id`),
  KEY `author_gid` (`author_gid`),
  CONSTRAINT `discussion_answer_ibfk_1` FOREIGN KEY (`topic_id`) REFERENCES `discussion_topic` (`id`),
  CONSTRAINT `discussion_answer_ibfk_2` FOREIGN KEY (`author_gid`) REFERENCES `user` (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discussion_answer`
--

LOCK TABLES `discussion_answer` WRITE;
/*!40000 ALTER TABLE `discussion_answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `discussion_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discussion_topic`
--

DROP TABLE IF EXISTS `discussion_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discussion_topic` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `title` varchar(127) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `author_gid` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `stars` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`),
  KEY `author_gid` (`author_gid`),
  CONSTRAINT `discussion_topic_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`),
  CONSTRAINT `discussion_topic_ibfk_2` FOREIGN KEY (`author_gid`) REFERENCES `user` (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discussion_topic`
--

LOCK TABLES `discussion_topic` WRITE;
/*!40000 ALTER TABLE `discussion_topic` DISABLE KEYS */;
/*!40000 ALTER TABLE `discussion_topic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enroll`
--

DROP TABLE IF EXISTS `enroll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `enroll` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_gid` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `course_cid` int(11) DEFAULT NULL,
  `enroll_type` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_gid` (`user_gid`),
  KEY `course_cid` (`course_cid`),
  CONSTRAINT `enroll_ibfk_1` FOREIGN KEY (`user_gid`) REFERENCES `user` (`gid`),
  CONSTRAINT `enroll_ibfk_2` FOREIGN KEY (`course_cid`) REFERENCES `course` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enroll`
--

LOCK TABLES `enroll` WRITE;
/*!40000 ALTER TABLE `enroll` DISABLE KEYS */;
INSERT INTO `enroll` VALUES (1590683794,1,1,'0000000010',2,3),(1590683794,1,2,'0000000011',2,1),(1590683794,1,3,'0000000011',2,1),(1590683794,1,4,'0000000012',2,1),(1590683794,1,5,'0000000013',2,2),(1590683794,1,6,'0000000014',2,2),(1591092844,1,7,'0000000010',3,3),(1591092844,1,8,'0000000011',3,1),(1591092844,1,9,'0000000011',3,1),(1591092844,1,10,'0000000012',3,1),(1591092844,1,11,'0000000013',3,2),(1591092844,1,12,'0000000014',3,2);
/*!40000 ALTER TABLE `enroll` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history_question`
--

DROP TABLE IF EXISTS `history_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `history_question` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(127) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `question_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `history_question_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history_question`
--

LOCK TABLES `history_question` WRITE;
/*!40000 ALTER TABLE `history_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `history_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(127) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `author_gid` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author_gid` (`author_gid`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `question_ibfk_1` FOREIGN KEY (`author_gid`) REFERENCES `user` (`gid`),
  CONSTRAINT `question_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_tag_table`
--

DROP TABLE IF EXISTS `question_tag_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_tag_table` (
  `tag_id` int(11) DEFAULT NULL,
  `question_id` int(11) DEFAULT NULL,
  KEY `tag_id` (`tag_id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `question_tag_table_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`),
  CONSTRAINT `question_tag_table_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_tag_table`
--

LOCK TABLES `question_tag_table` WRITE;
/*!40000 ALTER TABLE `question_tag_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `question_tag_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_up_vote`
--

DROP TABLE IF EXISTS `question_up_vote`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_up_vote` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `user_gid` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`),
  KEY `user_gid` (`user_gid`),
  CONSTRAINT `question_up_vote_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`),
  CONSTRAINT `question_up_vote_ibfk_2` FOREIGN KEY (`user_gid`) REFERENCES `user` (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_up_vote`
--

LOCK TABLES `question_up_vote` WRITE;
/*!40000 ALTER TABLE `question_up_vote` DISABLE KEYS */;
/*!40000 ALTER TABLE `question_up_vote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule`
--

DROP TABLE IF EXISTS `schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schedule` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `week_id` int(11) DEFAULT NULL,
  `topic` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `reference` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `schedule_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule`
--

LOCK TABLES `schedule` WRITE;
/*!40000 ALTER TABLE `schedule` DISABLE KEYS */;
INSERT INTO `schedule` VALUES (1590683915,1,1,2,1,'1423','123'),(1590685815,1,2,2,1,'1423','123');
/*!40000 ALTER TABLE `schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `gid` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(24) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nickname` varchar(24) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `auth` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`gid`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `nickname` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1590683792,1,'0000000000','9990@ustc.edu.cn','Super0',4),(1590683792,1,'0000000001','9991@ustc.edu.cn','Super1',4),(1590683792,1,'0000000002','9992@ustc.edu.cn','Super2',4),(1590683792,1,'0000000003','9993@ustc.edu.cn','Super3',4),(1590683792,1,'0000000004','9994@ustc.edu.cn','Super4',4),(1590683792,1,'0000000005','9995@ustc.edu.cn','Super5',4),(1590683792,1,'0000000006','9996@ustc.edu.cn','Super6',4),(1590683792,1,'0000000007','9997@ustc.edu.cn','Super7',4),(1590683792,1,'0000000008','9998@ustc.edu.cn','Super8',4),(1590683792,1,'0000000009','9999@ustc.edu.cn','Super9',4),(1590683792,1,'0000000010','99910@ustc.edu.cn','Super10',4),(1590683792,1,'0000000011','99911@ustc.edu.cn','Super11',4),(1590683792,1,'0000000012','99912@ustc.edu.cn','Super12',4),(1590683792,1,'0000000013','99913@ustc.edu.cn','Super13',4),(1590683792,1,'0000000014','99914@ustc.edu.cn','Super14',4),(1590683792,1,'0000000015','99915@ustc.edu.cn','Super15',4),(1590683792,1,'0000000016','99916@ustc.edu.cn','Super16',4),(1590683792,1,'0000000017','99917@ustc.edu.cn','Super17',4),(1590683792,1,'0000000018','99918@ustc.edu.cn','Super18',4),(1590683792,1,'0000000019','99919@ustc.edu.cn','Super19',4),(1590683792,1,'0000000020','99920@ustc.edu.cn','Super20',4),(1590683792,1,'0000000021','99921@ustc.edu.cn','Super21',4),(1590683792,1,'0000000022','99922@ustc.edu.cn','Super22',4),(1590683792,1,'0000000023','99923@ustc.edu.cn','Super23',4),(1590683792,1,'0000000024','99924@ustc.edu.cn','Super24',4),(1590683792,1,'0000000025','99925@ustc.edu.cn','Super25',4),(1590683792,1,'0000000026','99926@ustc.edu.cn','Super26',4),(1590683792,1,'0000000027','99927@ustc.edu.cn','Super27',4),(1590683792,1,'0000000028','99928@ustc.edu.cn','Super28',4),(1590683792,1,'0000000029','99929@ustc.edu.cn','Super29',4),(1590683792,1,'0000000030','99930@ustc.edu.cn','Super30',4),(1590683792,1,'0000000031','99931@ustc.edu.cn','Super31',4),(1590683792,1,'0000000032','99932@ustc.edu.cn','Super32',4),(1590683792,1,'0000000033','99933@ustc.edu.cn','Super33',4),(1590683792,1,'0000000034','99934@ustc.edu.cn','Super34',4),(1590683792,1,'0000000035','99935@ustc.edu.cn','Super35',4),(1590683792,1,'0000000036','99936@ustc.edu.cn','Super36',4),(1590683792,1,'0000000037','99937@ustc.edu.cn','Super37',4),(1590683792,1,'0000000038','99938@ustc.edu.cn','Super38',4),(1590683792,1,'0000000039','99939@ustc.edu.cn','Super39',4),(1590683792,1,'0000000040','99940@ustc.edu.cn','Super40',4),(1590683792,1,'0000000041','99941@ustc.edu.cn','Super41',4),(1590683792,1,'0000000042','99942@ustc.edu.cn','Super42',4),(1590683792,1,'0000000043','99943@ustc.edu.cn','Super43',4),(1590683792,1,'0000000044','99944@ustc.edu.cn','Super44',4),(1590683792,1,'0000000045','99945@ustc.edu.cn','Super45',4),(1590683792,1,'0000000046','99946@ustc.edu.cn','Super46',4),(1590683792,1,'0000000047','99947@ustc.edu.cn','Super47',4),(1590683792,1,'0000000048','99948@ustc.edu.cn','Super48',4),(1590683792,1,'0000000049','99949@ustc.edu.cn','Super49',4),(1590683792,1,'0000000050','99950@ustc.edu.cn','Super50',4),(1590683792,1,'0000000051','99951@ustc.edu.cn','Super51',4),(1590683792,1,'0000000052','99952@ustc.edu.cn','Super52',4),(1590683792,1,'0000000053','99953@ustc.edu.cn','Super53',4),(1590683792,1,'0000000054','99954@ustc.edu.cn','Super54',4),(1590683792,1,'0000000055','99955@ustc.edu.cn','Super55',4),(1590683792,1,'0000000056','99956@ustc.edu.cn','Super56',4),(1590683792,1,'0000000057','99957@ustc.edu.cn','Super57',4),(1590683792,1,'0000000058','99958@ustc.edu.cn','Super58',4),(1590683792,1,'0000000059','99959@ustc.edu.cn','Super59',4),(1590683792,1,'0000000060','99960@ustc.edu.cn','Super60',4),(1590683792,1,'0000000061','99961@ustc.edu.cn','Super61',4),(1590683792,1,'0000000062','99962@ustc.edu.cn','Super62',4),(1590683792,1,'0000000063','99963@ustc.edu.cn','Super63',4),(1590683792,1,'0000000064','99964@ustc.edu.cn','Super64',4),(1590683792,1,'0000000065','99965@ustc.edu.cn','Super65',4),(1590683792,1,'0000000066','99966@ustc.edu.cn','Super66',4),(1590683792,1,'0000000067','99967@ustc.edu.cn','Super67',4),(1590683792,1,'0000000068','99968@ustc.edu.cn','Super68',4),(1590683792,1,'0000000069','99969@ustc.edu.cn','Super69',4),(1590683792,1,'0000000070','99970@ustc.edu.cn','Super70',4),(1590683792,1,'0000000071','99971@ustc.edu.cn','Super71',4),(1590683792,1,'0000000072','99972@ustc.edu.cn','Super72',4),(1590683792,1,'0000000073','99973@ustc.edu.cn','Super73',4),(1590683792,1,'0000000074','99974@ustc.edu.cn','Super74',4),(1590683792,1,'0000000075','99975@ustc.edu.cn','Super75',4),(1590683792,1,'0000000076','99976@ustc.edu.cn','Super76',4),(1590683792,1,'0000000077','99977@ustc.edu.cn','Super77',4),(1590683792,1,'0000000078','99978@ustc.edu.cn','Super78',4),(1590683792,1,'0000000079','99979@ustc.edu.cn','Super79',4),(1590683792,1,'0000000080','99980@ustc.edu.cn','Super80',4),(1590683792,1,'0000000081','99981@ustc.edu.cn','Super81',4),(1590683792,1,'0000000082','99982@ustc.edu.cn','Super82',4),(1590683792,1,'0000000083','99983@ustc.edu.cn','Super83',4),(1590683792,1,'0000000084','99984@ustc.edu.cn','Super84',4),(1590683792,1,'0000000085','99985@ustc.edu.cn','Super85',4),(1590683792,1,'0000000086','99986@ustc.edu.cn','Super86',4),(1590683792,1,'0000000087','99987@ustc.edu.cn','Super87',4),(1590683792,1,'0000000088','99988@ustc.edu.cn','Super88',4),(1590683792,1,'0000000089','99989@ustc.edu.cn','Super89',4),(1590683792,1,'0000000090','99990@ustc.edu.cn','Super90',4),(1590683792,1,'0000000091','99991@ustc.edu.cn','Super91',4),(1590683792,1,'0000000092','99992@ustc.edu.cn','Super92',4),(1590683792,1,'0000000093','99993@ustc.edu.cn','Super93',4),(1590683792,1,'0000000094','99994@ustc.edu.cn','Super94',4),(1590683792,1,'0000000095','99995@ustc.edu.cn','Super95',4),(1590683792,1,'0000000096','99996@ustc.edu.cn','Super96',4),(1590683792,1,'0000000097','99997@ustc.edu.cn','Super97',4),(1590683792,1,'0000000098','99998@ustc.edu.cn','Super98',4),(1590683792,1,'0000000099','99999@ustc.edu.cn','Super99',4);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-19 17:44:46
