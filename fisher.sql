/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : fisher

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2022-04-29 17:10:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `author` varchar(30) DEFAULT NULL,
  `binding` varchar(20) DEFAULT NULL,
  `publisher` varchar(50) DEFAULT NULL,
  `price` varchar(20) DEFAULT NULL,
  `pages` int(11) DEFAULT NULL,
  `pubdate` varchar(20) DEFAULT NULL,
  `isbn` varchar(15) NOT NULL,
  `summary` varchar(1000) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `isbn` (`isbn`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of book
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(24) NOT NULL,
  `phone_number` varchar(18) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `confirmed` tinyint(1) DEFAULT NULL,
  `beans` float DEFAULT NULL,
  `send_counter` int(11) DEFAULT NULL,
  `receive_counter` int(11) DEFAULT NULL,
  `wx_open_id` varchar(50) DEFAULT NULL,
  `wx_name` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
