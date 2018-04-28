-- MySQL dump 10.13  Distrib 5.6.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: recycle
-- ------------------------------------------------------
-- Server version	5.6.28-0ubuntu0.15.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `industry`
--

DROP TABLE IF EXISTS `industry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `industry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `industry` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `industry`
--

LOCK TABLES `industry` WRITE;
/*!40000 ALTER TABLE `industry` DISABLE KEYS */;
INSERT INTO `industry` VALUES (1,'Construction and Demolition'),(2,'Dry Cleaning'),(3,'Equipment Repair'),(4,'Furniture Manufacturing'),(5,'Laboratories'),(6,'Leather Manufacturing'),(7,'Transportation'),(8,'Pesticide Users and Application Services'),(9,'Photo Processing'),(10,'Printing'),(11,'Textile Manufacturing'),(12,'Vehicle Maintenance');
/*!40000 ALTER TABLE `industry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `industry_waste`
--

DROP TABLE IF EXISTS `industry_waste`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `industry_waste` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `industry_id` int(11) NOT NULL,
  `waste` text NOT NULL,
  `waste_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `industry_waste`
--

LOCK TABLES `industry_waste` WRITE;
/*!40000 ALTER TABLE `industry_waste` DISABLE KEYS */;
INSERT INTO `industry_waste` VALUES (13,1,'ignitable wreckage',1),(15,1,'lead pipe',2),(16,1,'toxic wreckage',3),(17,1,'lead-based paint debris',4),(18,1,'mercury-containing fluorescent lamps',5),(20,1,'debris containing cresols',6),(21,1,'asphalt wastes',7),(22,1,'petroleum distillates',8),(23,1,'used oil sent for disposal',9),(24,1,'arsenic',10),(25,1,'used oil sent for disposal containing cadmium',11),(26,1,'chromium',12),(27,1,'lead',13),(28,1,'asphalt wastes containing benzene',14),(29,1,'acetone',15),(30,1,'adhesives',16),(31,1,'coatings',17),(32,1,'methylene chloride',18),(33,1,'mEK',19),(34,1,'mIK',20),(35,1,'mineral spirits',21),(36,1,'solvents',22),(37,1,'trichloroethylene',23),(38,1,'toluene',24),(39,1,'xylene',25),(40,1,'treated wood',26),(41,1,'unused acetone',27),(42,1,'unused MEK',28),(43,1,'unused MIK',29),(44,1,'unused xylene',30),(45,1,'unused toluene',31),(46,1,'unused methylene chloride',32),(47,1,'chlorobenzene',33),(48,1,'glazes',34),(49,1,'methanol',35),(50,1,'paint',36),(51,1,'stripping compounds',37),(52,1,'waste water',38),(53,1,'chromium pigments',39),(54,1,'lead pigments',40),(55,1,'unused chlorobenzene',41),(56,1,'kerosene',42),(57,1,'hexachloroethane',43),(58,1,'unused hexachloroethane',44),(59,2,'spent solvents',45),(60,2,'spent filter cartridges',46),(61,2,'distillation residues',47),(62,2,'cooked power residues',48),(63,2,'unused perc',49),(65,3,'toxic wastes',51),(66,3,'ignitable wastes',52),(67,3,'paint wastes',53),(68,3,'solvents',22),(69,4,'acetone',15),(70,4,'alcohols',54),(71,4,'metyl ethyl ketone',55),(72,4,'methyl isobutyl ketone',56),(73,4,'methanol',35),(74,4,'methylene chloride',18),(75,4,'mineral spirits',21),(76,4,'oxalic acid',57),(77,4,'petroleum distillates',8),(78,4,'toluene',24),(81,4,'1-trichloroethane',58),(82,4,'volatile organic compounds VOCs',61),(83,4,'xylene',25),(84,4,'methyl ethyl ketone',59),(85,4,'pigments',60),(88,4,'toluene diisocyanate',62),(89,4,'waste water',38),(90,4,'isopropanol',63),(91,5,'spent solvents',45),(92,5,'unused reagents',64),(93,5,'reaction products',65),(94,5,'testing samples',66),(95,5,'contaminated materials',67),(96,6,'high volume of wastewater',68),(97,6,'suspended solids',69),(98,6,'alkaline wastewater',70),(99,6,'ammonium sulfate',71),(100,6,'calcium hydroxide',72),(101,6,'hydrogen sulfide',73),(104,6,'toxic sulfides',74),(105,6,'chromium',12),(106,6,'acid',75),(107,6,'alkaline salts',76),(108,6,'kerosene',42),(109,6,'solvent',22),(110,6,'dye overspray',77),(111,6,'solvent still bottoms',78),(112,6,'toluene',24),(113,6,'toxic dyes',79),(114,6,'alcohols methanol',80),(115,6,'ethanol',81),(116,6,'propanol',82),(117,6,'butanol',83),(118,6,'diacetone alcohol',84),(119,6,'chromium in leather dust',85),(120,6,'esters ethyl',86),(121,6,'propyl',87),(122,6,'butyl acetates',88),(123,6,'glycol ethers butoxyethanol',89),(124,6,'propoxyethanol',90),(125,6,'ketones methyl isobutyl ketone',91),(126,6,'acetone',15),(127,6,'cyclohexanone',92),(128,6,'di-isobutyl ketone',93),(129,6,'methyl ethyl ketone',59),(130,6,'solvent overspray',94),(131,6,'volatile organic air emissions',95),(132,6,'xylene',25),(133,6,'trichloroethylene',23),(134,7,'acid',75),(135,7,'alkaline cleaners',96),(136,7,'ethyl benzene',97),(137,7,'residuals heels from shipment of product',98),(138,7,'hazardous waste',99),(139,7,'residues from wastewater treatment',100),(140,7,'spent solvents',45),(141,7,'volatile organic emissions',101),(142,7,'waste water',38),(143,7,'ammonium hydroxide',102),(144,7,'benzene',103),(145,7,'chromic acid',104),(146,7,'hydrobromic acid',105),(147,7,'hydrochloric acid',106),(148,7,'hydrofluoric acid',107),(149,7,'methylene chloride',18),(150,7,'mineral spirits',21),(151,7,'nitric acid',108),(152,7,'oil',109),(153,7,'grease',110),(154,7,'petroleum distillates',8),(155,7,'phosphoric acid',111),(156,7,'potassium hydroxide',112),(157,7,'rags containing solvents',113),(158,7,'sodium hydroxide',114),(159,7,'sulfuric acid',115),(160,7,'toluene',24),(161,7,'toxic metals',116),(162,7,'volatile organic constituents',117),(163,7,'wastewaters',38),(164,7,'sludges',119),(165,7,'alcohols',54),(166,7,'methyl ethyl ketone',59),(167,7,'methyl isobutyl ketone',56),(168,7,'paint pigments',120),(169,7,'volatile organic compounds',121),(170,7,'xylene',25),(171,7,'acetone',15),(173,7,'isopropanol',63),(174,7,'methanol',35),(175,7,'batteries lead acid',122),(176,7,'nickel cadmium',123),(177,7,'nickel',124),(178,7,'iron',125),(179,7,'carbonate',126),(180,7,'scrap metal',127),(181,7,'used tires',128),(182,7,'fluids contaminated with heavy metals',129),(183,7,'radiator flushing solutions',130),(184,7,'used oil',131),(185,7,'used oil filters',132),(186,8,'used/unused pesticides',133),(187,8,'solvent wastes',134),(188,8,'ignitable wastes',52),(189,8,'contaminated soil from spills',135),(190,8,'contaminated rinsewater',136),(191,8,'empty containers',137),(192,9,'silver',138),(193,9,'acid regenerates',139),(194,9,'system cleaners',140),(195,9,'photographic activators',141),(196,9,'dichromate based Cleaners',142),(197,9,'off-specification chemicals that are RCRA hazardous for corrosivity',143),(198,9,'ignitability',144),(199,10,'waste ink with chromium',145),(200,10,'barium',146),(201,10,'lead content;',13),(202,10,'waste ink contaminated with cleaning solvents',147),(203,10,'such as trichloroethylene',148),(204,10,'methylene chloride',18),(207,10,'1-trichloroethane',58),(208,10,'carbon tetrachloride',149),(209,10,'2-trichloroethane',150),(211,10,'3-trifluoroethane',151),(212,10,'chlorobenzene',33),(213,10,'xylene',25),(214,10,'acetone',15),(215,10,'methanol',35),(216,10,'methyl ethyl ketone MEK',152),(217,10,'toluene',24),(218,10,'carbon disulfide',153),(219,10,'benzene',103),(220,10,'acid plate etching chemicals for metallic lithographic plates',154),(221,10,'flexographic photopolymer plates',155),(222,10,'spent organic solvents might include trichloroethylene',156),(223,10,'1- trichloroethane',157),(224,10,'mEK',19),(225,10,'waste photochemical solutions from fixer',158),(226,10,'rinsewater',159),(227,10,'from alkaline',160),(228,10,'acid process baths',161),(229,10,'unused inks',162),(230,10,'solvents',22),(231,10,'other chemicals used in printing industry',163),(232,11,'hydrogen peroxide',164),(233,11,'sodium silicate',165),(234,11,'organic stabilizer',166),(235,11,'alkali',167),(236,11,'sodium hydroxide',114),(237,11,'tetrachloroethylene',168),(238,11,'trichloroethylene',23),(239,11,'methylene chloride',18),(240,11,'chlorobenzene',33),(241,11,'toluene',24),(242,11,'methyl ethyl ketone',59),(243,11,'benzene',103),(244,11,'xylene',25),(245,11,'ethylene dichloride',169),(246,11,'isopropyl alcohol',170),(247,11,'mineral spirits naptha',171),(248,12,'dichlorodifluoromethane CFC-12',172),(249,12,'lead dross',173),(250,12,'zinc',174),(251,12,'copper',175),(252,12,'spent sulfuric acid',176),(253,12,'scrap metal',127),(254,12,'methylene chloride',18),(255,12,'trichloroethylene',23),(256,12,'aromatic',177),(257,12,'chlorinated hydrocarbons',178),(258,12,'used oil',131),(259,12,'oil filters',179),(260,12,'fuel filters contaminated with cadmium',180),(261,12,'chromium',12),(262,12,'lead',13),(264,12,'scrap tires',182),(265,12,'spent halogenated',183),(266,12,'nonhalogenated solvents such as acetone',184),(267,12,'toluene',24),(268,12,'benzene',103),(269,12,'xylene',25),(270,12,'methanol',35),(273,12,'paint; paint filters;',36),(274,12,'spent rags',187),(275,12,'wipes',188),(277,12,'phosphoric acid',111),(278,12,'hydrochloric acid',106),(279,12,'hydrofluoric acid',107),(280,12,'sodium hydroxide',114),(281,12,'heavy metals',189),(282,12,'petroleum distillates',8),(283,12,'various solvents',22),(284,12,'petroleum products potentially outdated',190),(285,12,'off-specification',191),(286,12,'zinc chloride coolant',192),(287,12,'chlorinated solvents',193),(288,12,'lead solder',194),(290,12,'drain',195),(291,12,'sump sludges contaminated with metals',196),(292,12,'petroleum',197),(294,3,'',50),(295,3,'',75),(296,12,'',185),(297,12,'',170),(298,12,'',181),(299,12,'',198),(300,12,'',8);
/*!40000 ALTER TABLE `industry_waste` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `org_waste_gen`
--

DROP TABLE IF EXISTS `org_waste_gen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `org_waste_gen` (
  `org_id` int(11) NOT NULL,
  `waste_item` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `units` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `org_waste_gen`
--

LOCK TABLES `org_waste_gen` WRITE;
/*!40000 ALTER TABLE `org_waste_gen` DISABLE KEYS */;
/*!40000 ALTER TABLE `org_waste_gen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `org_waste_req`
--

DROP TABLE IF EXISTS `org_waste_req`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `org_waste_req` (
  `org_id` int(11) NOT NULL,
  `waste_item` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `units` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `org_waste_req`
--

LOCK TABLES `org_waste_req` WRITE;
/*!40000 ALTER TABLE `org_waste_req` DISABLE KEYS */;
/*!40000 ALTER TABLE `org_waste_req` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organization`
--

DROP TABLE IF EXISTS `organization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `organization` (
  `org_id` int(11) NOT NULL AUTO_INCREMENT,
  `industry_id` int(11) NOT NULL,
  `org_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `passwd` varchar(255) NOT NULL,
  `contact_no1` varchar(10) NOT NULL,
  `contact_no2` varchar(10) NOT NULL,
  `address` mediumtext NOT NULL,
  `contact_person` varchar(255) NOT NULL,
  PRIMARY KEY (`org_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organization`
--

LOCK TABLES `organization` WRITE;
/*!40000 ALTER TABLE `organization` DISABLE KEYS */;
/*!40000 ALTER TABLE `organization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `waste_master`
--

DROP TABLE IF EXISTS `waste_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `waste_master` (
  `waste_id` int(11) NOT NULL AUTO_INCREMENT,
  `waste` varchar(255) NOT NULL,
  PRIMARY KEY (`waste_id`)
) ENGINE=InnoDB AUTO_INCREMENT=200 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `waste_master`
--

LOCK TABLES `waste_master` WRITE;
/*!40000 ALTER TABLE `waste_master` DISABLE KEYS */;
INSERT INTO `waste_master` VALUES (1,'ignitable wreckage'),(2,'lead pipe'),(3,'toxic wreckage'),(4,'lead-based paint debris'),(5,'mercury-containing fluorescent lamps'),(6,'debris containing cresols'),(7,'asphalt wastes'),(8,'petroleum distillates'),(9,'used oil sent for disposal'),(10,'arsenic'),(11,'used oil sent for disposal containing cadmium'),(12,'chromium'),(13,'lead'),(14,'asphalt wastes containing benzene'),(15,'acetone'),(16,'adhesives'),(17,'coatings'),(18,'methylene chloride'),(19,'MEK'),(20,'MIK'),(21,'mineral spirits'),(22,'solvents'),(23,'trichloroethylene'),(24,'toluene'),(25,'xylene'),(26,'treated wood'),(27,'unused acetone'),(28,'unused MEK'),(29,'unused MIK'),(30,'unused xylene'),(31,'unused toluene'),(32,'unused methylene chloride'),(33,'chlorobenzene'),(34,'glazes'),(35,'methanol'),(36,'paint'),(37,'stripping compounds'),(38,'wastewater'),(39,'chromium pigments'),(40,'lead pigments'),(41,'unused chlorobenzene'),(42,'kerosene'),(43,'hexachloroethane'),(44,'unused hexachloroethane'),(45,'spent solvents'),(46,'spent filter cartridges'),(47,'distillation residues'),(48,'cooked power residues'),(49,'unused perc'),(50,'bases'),(51,'toxic wastes'),(52,'ignitable wastes'),(53,'paint wastes'),(54,'alcohols'),(55,'metyl ethyl ketone'),(56,'methyl isobutyl ketone'),(57,'oxalic acid'),(58,'1-trichloroethane'),(59,'methyl ethyl ketone'),(60,'pigments'),(61,'VOC'),(62,'toluene diisocyanate'),(63,'isopropanol'),(64,'unused reagents'),(65,'reaction products'),(66,'testing samples'),(67,'contaminated materials'),(68,'high volume of wastewater'),(69,'suspended solids'),(70,'alkaline wastewater'),(71,'ammonium sulfate'),(72,'calcium hydroxide'),(73,'hydrogen sulfide'),(74,'toxic sulfides'),(75,'acid'),(76,'alkaline salts'),(77,'dye overspray'),(78,'solvent still bottoms'),(79,'toxic dyes'),(80,'alcohols methanol'),(81,'ethanol'),(82,'propanol'),(83,'butanol'),(84,'diacetone alcohol'),(85,'chromium in leather dust'),(86,'esters ethyl'),(87,'propyl'),(88,'butyl acetates'),(89,'glycol ethers butoxyethanol'),(90,'propoxyethanol'),(91,'ketones methyl isobutyl ketone'),(92,'cyclohexanone'),(93,'di-isobutyl ketone'),(94,'solvent overspray'),(95,'volatile organic air emissions'),(96,'alkaline cleaners'),(97,'ethyl benzene'),(98,'residuals heels from shipment of product'),(99,'hazardous waste'),(100,'residues from wastewater treatment'),(101,'volatile organic emissions'),(102,'ammonium hydroxide'),(103,'benzene'),(104,'chromic acid'),(105,'hydrobromic acid'),(106,'hydrochloric acid'),(107,'hydrofluoric acid'),(108,'nitric acid'),(109,'oil'),(110,'grease'),(111,'phosphoric acid'),(112,'potassium hydroxide'),(113,'rags containing solvents'),(114,'sodium hydroxide'),(115,'sulfuric acid'),(116,'toxic metals'),(117,'volatile organic constituents'),(119,'sludges'),(120,'paint pigments'),(121,'volatile organic compounds'),(122,'batteries lead acid'),(123,'nickel cadmium'),(124,'nickel'),(125,'iron'),(126,'carbonate'),(127,'scrap metal'),(128,'used tires'),(129,'fluids contaminated with heavy metals'),(130,'radiator flushing solutions'),(131,'used oil'),(132,'used oil filters'),(133,'used/unused pesticides'),(134,'solvent wastes'),(135,'contaminated soil from spills'),(136,'contaminated rinsewater'),(137,'empty containers'),(138,'silver'),(139,'acid regenerates'),(140,'system cleaners'),(141,'photographic activators'),(142,'dichromate based Cleaners'),(143,'off-specification chemicals that are RCRA hazardous for corrosivity'),(144,'ignitability'),(145,'waste ink with chromium'),(146,'barium'),(147,'waste ink contaminated with cleaning solvents'),(148,'such as trichloroethylene'),(149,'carbon tetrachloride'),(150,'2-trichloroethane'),(151,'3-trifluoroethane'),(152,'methyl ethyl ketone MEK'),(153,'carbon disulfide'),(154,'acid plate etching chemicals for metallic lithographic plates'),(155,'flexographic photopolymer plates'),(156,'spent organic solvents might include trichloroethylene'),(157,'1- trichloroethane'),(158,'waste photochemical solutions from fixer'),(159,'rinsewater'),(160,'from alkaline'),(161,'acid process baths'),(162,'unused inks'),(163,'other chemicals used in printing industry'),(164,'hydrogen peroxide'),(165,'sodium silicate'),(166,'organic stabilizer'),(167,'alkali'),(168,'tetrachloroethylene'),(169,'ethylene dichloride'),(170,'isopropyl alcohol'),(171,'mineral spirits naptha'),(172,'dichlorodifluoromethane CFC-12'),(173,'lead dross'),(174,'zinc'),(175,'copper'),(176,'spent sulfuric acid'),(177,'aromatic'),(178,'chlorinated hydrocarbons'),(179,'oil filters'),(180,'fuel filters contaminated with cadmium'),(181,'benzopyrene'),(182,'scrap tires'),(183,'spent halogenated'),(184,'nonhalogenated solvents such as acetone'),(185,'waste paint thinner'),(186,'paint filters'),(187,'spent rags'),(188,'wipes'),(189,'heavy metals'),(190,'petroleum products potentially outdated'),(191,'off-specification'),(192,'zinc chloride coolant'),(193,'chlorinated solvents'),(194,'lead solder'),(195,'drain'),(196,'sump sludges contaminated with metals'),(197,'petroleum'),(198,'ethylene glycol antifreeze contaminated with lead');
/*!40000 ALTER TABLE `waste_master` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-16 18:34:36
