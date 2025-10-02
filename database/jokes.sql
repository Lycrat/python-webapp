-- MySQL dump 10.13  Distrib 8.0.42, for macos15 (arm64)
--
-- Host: localhost    Database: jokesdb
-- ------------------------------------------------------
-- Server version	9.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

use jokesdb;
--
-- Table structure for table `jokes`
--

DROP TABLE IF EXISTS `jokes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jokes` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Setup` varchar(255) DEFAULT NULL,
  `Punchline` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jokes`
--

LOCK TABLES `jokes` WRITE;
/*!40000 ALTER TABLE `jokes` DISABLE KEYS */;
INSERT INTO `jokes` VALUES (1,'Why don\'t scientists trust atoms?','Because they make up everything!'),(4,'Why did the math book look sad?','Because it had too many problems.'),(5,'What do you call fake spaghetti?','An impasta.'),(6,'Why can’t your nose be 12 inches long?','Because then it would be a foot.'),(7,'Why did the scarecrow win an award?','Because he was outstanding in his field.'),(8,'Why don’t skeletons fight each other?','They don’t have the guts.'),(9,'What do you call cheese that isn’t yours?','Nacho cheese.'),(10,'Why did the bicycle fall over?','Because it was two-tired.'),(11,'Why can’t a leopard hide?','Because he’s always spotted.'),(12,'Why did the computer go to the doctor?','Because it caught a virus.'),(13,'Why was the stadium so hot?','Because all the fans left.'),(14,'Why did the golfer bring two pairs of pants?','In case he got a hole in one.'),(15,'Why don’t oysters donate to charity?','Because they’re shellfish.'),(16,'Why did the tomato blush?','Because it saw the salad dressing.'),(17,'Why don’t eggs tell jokes?','Because they’d crack each other up.');
/*!40000 ALTER TABLE `jokes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vgetjokes`
--

DROP TABLE IF EXISTS `vgetjokes`;
/*!50001 DROP VIEW IF EXISTS `vgetjokes`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vgetjokes` AS SELECT 
 1 AS `ID`,
 1 AS `Setup`,
 1 AS `PunchLine`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vgetjokes`
--

/*!50001 DROP VIEW IF EXISTS `vgetjokes`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vgetjokes` AS select `jokes`.`ID` AS `ID`,`jokes`.`Setup` AS `Setup`,`jokes`.`Punchline` AS `PunchLine` from `jokes` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-01 17:12:47
