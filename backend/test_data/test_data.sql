-- MariaDB dump 10.17  Distrib 10.4.13-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: SE
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (1590084548,1,1,1,'because','0000000000',0),(1590084562,1,2,1,'zcasdasd','0000000000',0);
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
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
  `pre_Course` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `textbooks` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `semester` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1590084200,1,3,'ç”µç£å­¦','hapy','hi','ads','dcx','ad'),(1590084513,1,4,'è½¯ä»¶å·¥ç¨‹','jisuanke','hi','ads','dcx','ad');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_resource`
--

LOCK TABLES `course_resource` WRITE;
/*!40000 ALTER TABLE `course_resource` DISABLE KEYS */;
INSERT INTO `course_resource` VALUES (1590084910,1,1,'1.PNG','‰PNG\r\n\Z\n\0\0\0\rIHDR\0\0Î\0\0Ô\0\0\0*I®L\0\0\0sBIT|dˆ\0\0\0tEXtSoftware\0gnome-screenshotï¿>\0\0 \0IDATxœíİwœTÕıÆñgvg)\n‚¢(\n*b¯ˆ –XPÄü4¶“±`‰5j4QcìbW,Ñ5ÑM,kì]‘fEPéHÛeÙß8ËÙ[¾wæNİÏÛ×¾dïœ9çÜ3³³Ï9snlŞœÙ©æ¦Zºd±\0\0\0\0¬´Z§ÎŠÅjtçE©×Zk)6ãÛi©††úR÷\0\0\0(;íÛwĞ²eËôğµ×«†Ğ\0\0\0¸kh¨W§ÎÕc«­ûúËÏS¥î\0\0\0PÎ–,Z¤¸Dn\0\0\0ütîÒEqr3\0\0\0à/&)Nn\0\0\0ü557«¦Ô\0\0\0\0Ê]*•b3\0\0\0`Á\Zg\0\0\0À ^ê\0@¥Yºt©xæ9}6ùKM™:U«uXM›ôŞH»íÜ_{ıd÷Våï¾ÿ_zşå×<ëÛc·]tŞoOÏ(»ÎÚİô·[oRmm­ë}^yc„î¸ç>IÒ#÷ß£íÛëäß£ÙsçêÌSNÔ~ƒöÊ(?gÎ<tÖï%Iÿ¸ó6u[sÍœÎ\0*Acc£^~}„F}[Ó¾ùV’´a¯Ú{÷İ4dß½UWW—S½|8\0B˜ôÙçºù»4gÎ¼–c‹/Õì¹sõÎûè­÷ş«³sŠ:vìªŞì×â9sçéµ‘£4dŸA­Ê677ëÉgŸÏ¸oöıı¾w+\0ÕbŞüùºú†›5eê´ŒãŸOşRŸOşR¯¾9J—üñœœ&Xã\0FK—.Õuú³.üA½7ÜP\'w´úôŞH³çÌÓëoÔ3/¾¢wŞÿ@k­ù¨N9áØV÷ße@?]pÎÙµ·~-~ü?ÏjğŞ{ª¦&ósÜcßyO3fÎÎº/Ñ@y?q’$iÛ­·,Z›®¡ÙiÊÔ©ºzø-\Z~å¥¡gÙU\0Œ’ÿGş nk­¥ë®¼DÛn½¥:vì¨6ì©_{´:âç’¤—^¡©Ó¾Í»½ÙsçjÄ¨1­?ñÌ³y×\r :ÜxÛ-ÕÏø‰“tãmw¡G«Ú»éÏwè¦?Ûú•W^³%4_{å0õÛ±oËmıvì«k¯&IšòõT½:bTèúkZ&øâ‹/¾øòı\Zûî%I‡ğSuh×¾Õí‡ğZ£S\'577kÜÇŸdŞ®mIZgn’¤Çşó¬š›š[nûïãôõÔo´Åf}ÔÂÙ†_;A·óÅ_÷uäGè¦?ß¡OÆOô,óé¤ÏuÓŸïĞ/;¬(}J·wõå—éú«¯\nì_”_£Ş~WiÉGÕ°/P¿ûªß}5ìÂ”|ôÑ–ÛG¿ıNèú™q\0ƒúúÍûş{IRŸM6v-Ó¾};õŞx#IÒ´ï¦·ºıİş§ŸsB«¯ïfÌhUv‡m·QŸŞiæìÙzsÌ[-ÇúYÅb1vĞœ€J·ÉÆ½tıÕWéæ¿Ü¥O&Lluû§Ÿ}®n½]W_~™¶Üt“‚÷ÇÙ^ŸziÃõ×õí_Ô¦}óMË¿??Q\r»BÃ.¼@Ã.¼@\r»B_Õ‡©S¿q«ÂW<¥T$€j6sÎª5Åk¬ÑIÎ×Î¦¦¦–İ/Ò3ÅóæÍSöëk*•R*Õú57õãN1Åô‹CÒ\rú‹{êíõ“]õé¤Ï5é‹É\ZØ\'õÜ ‡çıİêËü¾õí\0*SCC½z­ß]×_}•.¸äRsæo´İ6[I’>ıì\rÿ1Än²QOÕ7,+h_¼Úóê_!Äb™ßÇëê´`ş¼–g”Uökc0fœÀ`­®]Zş=ïûù-ÿşæÛïtÆ9è‹/¿’$-[¶òÅÚkwkUÇÀşıôŸ‡ïoõµA­Ê®,¿“zn°¾fÌœ¥Ño½£ÇŸyN’ôóƒıg›	Å@Û²¼¡¡%œŞò—»ôÉ„O[…Ø††ú‚öÁ¯=·şÊÆõnùw¿ûêÊ‹/ÒğÛn×ğÛn×•_”±æ¹÷&½İªğÅ\Zg¾øâ‹/ÃWçNÕ¹sgIÒçŸOn9>jìÛš5g†]w“>ûüK}>ye€îÑ½ûªû;µåSL¿8äg’¤ûJjÜÇãµíÖ[ió>›d–ıñ¾«¯¾š$é‡µª·¾~å/±šš\Zu^½SÉÇ“/¾øŠöky}ƒzõè®k¯¦[şr—†ßz»®½bØÊ[__ğö_|õußöœı{uÄÈ‚õcÇ‡x .\Z6Lã\'NÒø‰“tÑ°a:ôÀUƒ\r\n]?3Î\0`Ôo»m%IÏ¾øŠ-Y\"I:êˆÃ5dĞŞZºt©.½æzÍ™;OµµµÚc·]#is]wÑºİ»kÁÂ$I‡û¬mîÕsIÒ¸Ç·ºí³É_J’6è±nÎÿ(oË\Z´qÏõuíÃtíÃ´qÏõW†Ø\"¸êòKÛK÷ïªË/-X?ï³—6ÛtSIÒeW_“±£Çø‰“tÙÕ×H’6ÛtS\r´gèúkJş\'_|ñÅW…|\r=òuhß^‹–,Ñ/»Bã>¯††ıüàÔsıjll”$ıdàÎZgíµ²îŸfikUÙšš˜~~ğ’¤Şm¨¾ÛoãYç®v’$ÿt’î{ğaÍ_0_+V4ê¢‡}\\’´Ï{”|ùâ‹¯Â}54,ÓÆ={hã=ÔĞ°¬híÎŸ;ÛÔ^CÃ2ÍŸ;»`ıhlX¦á×\\Ùİl¶é¦\Z~Í•ZÃøpå@\00Zk­5uöé§è»ïÕŒ™³uÅ\r7)‹µúÀß»~¨ñŸNÒ6[­Üô?}ë{üO‡=±U½?ÙugıîôS3Ê¦ÿŞoĞ^-—ĞvŞî”’4pÀNúÉ®5æíwõÌ‹¯è™_ÉèßöÛl­ƒØ¿Õ}T—ú¯g.g©TJµ©ºû/·ê¹—^ÑË¯¾¦¯¦L‘$õé½‰†ì·¯~öÓ!úaÁ÷jrù°vxÔ€j6°?mÖ§·ê9}9åkMûö;­¾ÚjÚ°çú\Z<hO}öÅ—zöÅWô¯?¦ë¯¸D1ÇG¼½vÕhn.ÊsæiÚa»m5bÔ}óİtÅb1õÚ`}í±Û.ÚoĞı€jÔÔÔ¤ßÏÕA{éĞŸ ººv’¤ÆÆåZºd‰|?×õµØ\"6yÒ&\0 B/½öºvße :wêTê®\0\0\"›<i<Á\0\0\0À®\Z\0\0\0€\0\0\0â|¼\Z\0\0\0o½©\0\0\0€l¬q\0\0\0Î\0\0\0€\0\0\0âÊñÊ)\0\0\0@[ÂR\r\0\0\0À şİ´)¥î\0\0\0PöbK—,f­\0\0\0€¥\Z\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0ƒœƒó£?©¯§MuŸ%K—jáÂ…­Ï˜9Sûû?ÌõŒûè½õÎ»¡Ú®D_M™¢	?-u7\0\0\0 )ëÿùĞÃêÖ­›z¬·^Æñ¦ÍêĞ¡jjZgò»î¾GûXßoÆñY³æè¾Ô;î wÚI’ôì‹/é£që’ÏoUÏyFßNŸ®İvØrì»éÓ5köœŒrë¬½¶zõÜ ×S,¹‡“iÄ¨QúÓ7hûm·‘$Í›7Oç^x±kùÚÚZİ{×Çxêi½÷ß~ü.–q[,óÛŒï{®¿Î8í”¼ú\0\0PMrÎñx\\ıû=zàßÿÎ8¾bÅ\n]sÅåÚ¨W¯V÷©k×NíÚÕµ|ÿíwÓuæ9çê¶›†«¿uïıÿl	ÎsæÌÑ_}éÚvûöíÕ¾]»ŒcO?û¼zö9mÚgIÒW_OÕàA{é¼ßíy¼är~ØÁÚy§ôÌó/èÚá7éªË.Õ~ûò¼Ïç_|¡cO:U§ôk0ôÍûş{]xéå\Z~ÍUêÚµ«çırqÁÎÑâ¥Kt×İ÷è®?ß*IZŞØ¨IŸ}®ııoí}şÅ:ÿâËZÕñÙç_¨¹¹YÇ}TË±ÆÓ‡şO\'p¼j²Ó³¤×FŒĞû~èÚ§ô˜=şäSúpÜGzéé\'·~\Z}ùÕ}Â‰ºíÆ´é¦}\n6F\0\0\0Å’spÕÄô»3ÎĞî»íj¾O]m\\µµµ«êˆI3gÎRL1tüñ:í¬³õßÿ§şıvT»víZ…ã´šÚZÕÖÔfŒÅ´í¶Ûè–ë¯•$]péå¾}yëw5zìXyÚ©ÇïğA\rŞgoÅ\\¥$İ÷Àƒß¯Ùµ«-Z¤ûxP¿ÿí™¾mZÕ××kÌ[o«®.®!ûî«¥õK5rôIÒë¯/IêÖ­›fÏ™£Ûïü«n»i¸ºvñ¤kvíªm·Ùºåû;ï¾GË–Õk½u»g”ë´zg­¶ZŸø©¤OZÕã³ÁƒiÔ˜±ú`ÜG\ZØ§VeGŒ¥.k¬¡ş;õS,‹|Œ\0\0\0Š-08öùºüªkK/½H¥¤XLsçÎÓ·şYwÜı÷§‹Å”J¥T__¯Ã;DÇ$~¥o¾®ùó¿WMMæÌ«¥K—éãñÔÜÔ¬^=W†Àºº¸úî°ôë§ÿ7Nıûí¸2¸:Âë’¥K5mÚ4ÕÔÔê‡jiı²gS›´IïŞ­úİÔÔä{^ÿ|è!\rÙgŸ–>¤MùzªÆ¼õ¶öØ}·V÷™2ušF«ººU³æ555\ZzôQºş¦[tÒñÇ«sçNAC\Z¨±q…Æ¾ıâñxK€5ö-­·nw]{Åª?–,YªÇ}ä:ãëå­·ßÑ‡ã>Òºİ»ëü‹/•$}5åkuhß^İ¯V[­ƒç}c¶v·5Õ¡C=Ú58¿1r”í½WËJQ\0\0@±&®úúÍ_°@/?ûTÆñ#ûµ~}ìĞ–e\rÍÍÍª¯_®¿üí¯zû÷Z‚ç„I5nÜÇŠÇkõÕ×_káÂ…záåWÔÔØ¨ÓN9)£Î[oº!cFÚiöœ¹zú¹×êƒÇ©C‡zö…´bE“N:ş¸•«wS©–ò¶òÍ·ßé£Çë¤?ßê¶A{í©ûxÈ58ÿëÁ‡´×»ëãO&dßg¯=uÓ­·ê•×_×á‡âİ°QçÎtùÅ¶|ÿÉ„	zîÅ—tÃUWfÌ„Çkãª««óœÏ¶ğ‡4üÖÛ´Şzëªk—.º÷®;ôÊëoèÊk¯×•—^¬uÖ^Ûó¾ÙcÖ±cGí¾ë@=VøİÙ}øæÛïôÕ”):÷ìß¶‹zŒ\0\0\0Š-§]5fÎš¥åË—kä˜1ºæ†uÒégêÈcOĞˆQ#µù¦›j—;kƒ=$I?<XœwÎûİÙ\ZØ¿¿zôXOœû{]|Aëı9CsC}½:¶oßò}ï6Ôç£c>J‹/Ö†={ê¼ß­Î;Gk¯İMRfXnN5{öÔØ±Z}õÕµSß¾­n;~èÑútÒ$½÷ÁÇ§Ï˜¡W^CÇ}t«ûtèĞAĞ¨1c=ÛÌU}}½®½áF~èÁÚaûm3n‹ÅbæĞ¼xñbıá¢K´f—®zø¾ûÔiõÕõ‡‹.ÑµÃoÒoN>Q{ï¹‡ïıİÆlğ }4oŞ<Ÿ81£ìˆ‘#Õm­µ´ãÛ·+ä\0\0ƒ98OùúkpÊo”z¼®»ñf-^²D;tĞaÿL·ß|£yğŸ:ğ§û«WÏ\Z5zL¨ånæÌû^İºukuü¹^Tss³&OùJW\\sR?¦ek€”¤	\'jë-¶pİùc³>}´û®»êşe®eş×ÃIõß©Ÿ¶Übs×:·Şj+Mœ4ÉÜ«á·ÜªùĞé§œœW=o½óššštÛÍÃµÚj´çî»ë­wŞÕ:k¯­ƒ8 ğşnc¶Û®µzÇ\Z9jLFÙ#GkŸA{µ\ZßB\0\0@1˜Óíúë¯¯›o¸Vk­¹¦$éŞşK=ù”¾›>=£ÜÔißdl—mÉâ%úë=+·£;âğÃ<Ë}óÍ7Úa»í2555é©gŸ—´rvù¥W_SïŞëØ£üñ˜ÏúgİßN×6[méyû	CÖ‰¿9CŸL˜ í¶ÙFóæÍÓ/½¬Ûn\ZîyŸ^l E‹ë‡E‹´FçÎ¦~¹ÿÁ‡ôÂË¯hõuÖ¹çëÖ›‡«¹ùÇ™ôTJ+šV(‹­:æcÈà}4xŸ½µ¬¡AW^{½^}c„N?õd}ûmıâè¡:êWGhİvÕf›nêz·1kß®öØ}w3Zgşfå‡,gÎš¥O?ûL¿ÿí­ê(Ä\0\0‹98·ÏÚåâÄãÕ =÷Ğ‚…?´*»åæ[´ü»¹¹YS§MÓ;ï¾¯7GÖÒeË´cß4p@Íûşû–rßMŸ®3g©¿µxñbûøvÒ‰õ=V³çÌÑ6[o¥Õ:tÔ}·×âE‹%I\rËÕŞ±´ÃÏâÅ‹ÕiõÕ=oßfë­4°ÿNºï‡tËõ×êÁGÕ–›o–±ô [§N+?ğ¶(¢PøÄSOëŞûÿ¥ıï«÷?øPÓgÎÔ¥Ã®Ô™?î­¼¢©I,PCCƒ9\"¡ë®æ[ßâÅ‹õÄÓÏèÑÇŸÔj«uĞi\'Ÿ¨Å‹ë®ÛnÕyVşûİóûuÃÕWxŞßmÌöÛw^zí5}ùÕõÙ¤·Ş5Fëvï®í~ÜwÚ)ê1\0\0(&óR/&OÖÒ¥õ’¤©ß|£_uŒÖ^{mõë»ƒştûjnnV¿¾;hËÍ·PÇ«ì\r7ßªcO:U_OûF[l¾™ÖíŞ]ôÏ¨{Ö¬9:ëÜóõı÷ó%I¯¼ö†âñ¸6ŞhÃŒr<ñ¸vÛe`Ë¬è¯;V§Ÿºr	Ãüyóµf×.¦sI¥R³ÓÇ\r=Fo½ıŞûà=õÌs:~è1¾åÓkª\r“¿xêiİ|Ûí\Zvñ…Úu—Õ¹S\'İtİÕúò«)š3wíµ‡ÚÕµÓ¤Ï>—$ÕÆkÕ«WO]uÙ%uşõï÷êáGÓĞ£ÔÃ÷ß§õº¯«û|H<ö„?ô=™|HşãïÚc÷İ]ïï5f;è¯N:éÍÑ£%I#FÔ¾ƒÜ·ó‹rŒ\0\0\0Š-08/Y²XuíêtáeÃtÏı÷µÿö»é-æ›5k–V¬hÔÜ¹ótògèáGk)÷ëãÑã? ÿpz¬»^«ú%é‚Ë.×¡ÿLCï£%Ë–éï÷ÿSõõõJ>şDK™÷>ø@}<^\'ŸpœkÓgÍT÷u¼w…pZ}õÕ´dÙ2ß2ıúî ¶ßV\\r©z®¿¾ïòIZ¶t©$©s§ÕL}ğsğèŸ÷üUûÚ»åØV[l¡Ç~@ô×uW^¡®]»hÄ¨Qê×wÅkkÕe52Êg;÷ì³ôÔ#+qÄáª¯oĞ¾ƒöÒY§ÿF#FRSS“b±˜6í³‰ëºoÉ{Ìêêê4hŸèÍQc4ïûïõÉø‰Úo÷~D9F\0\0\0ÅœgÏ™£õ{ôĞ™§ªGR“¿üJu?~ğ/îøÿŒ3uò¿U‡tÀ!-÷_·{w­Û½»kİ,”$í´c_\r=2!Iºõ¶ÛÕeÎ\ZzdB<ş„–ü¶á%íµÇÚjËÖk“.\\¨ñ&j€c?áìOçZìnk®¥Ù³gº~=t¨\Z\Z\ZuüĞÖ;id›5kâñxËr„|ÔÕÕ¹®5vîıòë¯kşüÚgï½3Ê444èÈcOĞœ¹s3Çb1uìØQóç/ĞA¿ø¥†]u­ØIwŞö\'Ï-\0üÆlğ¾ûè‹É“õïGSõÖs}Œ¤hÇ\0\0 ØƒóÛïıW}·ÛN{ï¹‡è¯á·üÉµÜM·İ®-6ßLwŞz‹Ö\\ÓvYå®]ÖĞ?Ù]Ÿ¿rkº»ÿq¿^ñ¦†]r±NüRË–ë‰ÿ¬Ü?úŠK/Ö5Ã.u­çù—^Öš]»j›­¶Zubà¼lÙ2qô±Z¼xåzè-·Ø\\ŸOØ¿;ĞØ7^õÉMûbòdmÚg“¼w±˜9s–n½ıNqê)êĞ1s]÷ŒY³ôõ´ikˆ»tYCŸÿ}ùõ×:ú„“tÁ¥ÃôÉ„	®eüÆ¬¿Õ¥K=üèc\Zì3VÅ#\0\0€¨ùç/&OÖØ·ßÖÁûJ’Î=û·Jq„ëúÕŸz°®»r˜ùzÒÊËF¿æ*¥Ô¬Ë®ºZı;©á×^¥-6ßL]»vÕO‡ÑO=Ór@·Àõİôéºç¾êÔOÈXfPã¸$÷Œ™3UWW×2ÓÙw‡í5wî<M™:ÍÜW?©TJïÿïê»ıvÁ…ó4}Æ}ŞùÚz«-uØ!µº}Ö¬Ùê¾Î:CMMöÛw¸÷nıiøuZºt‰N9ã¬À±ğ³ÚÚZí³÷^jnnÖà/ˆ“­˜c\0\0PSß~7]¸øR°ÿMşêKMùzjËmcÆ¾-IzãÍ‘Š×ÆÕ°|¹:­¶º^{ãMI+CRûöuÚkÌ‹jÌ7OíË\r~X´HO?÷¼}üIµoßN÷Üy»6ßl³–ÛJ¡g^o\Z£}íÕr¼qùr-_±\\_|ù¥şpÑ%Únë­õ³ş/£­µÖZSsç­Üµcî÷ßkİîë´Ü6p@uëÖM¯¾ş†Nùõñ’V®+>øÀàıŒ%éùÿ<ñı\'ã\'hæÌY:ğÿ~jº+´¢©Iõõõzö…—ô·{ÿ¡wØ^×»L±XLku]yûH;vĞ\'&¨ç«.#ŞÔÔ¤Wß¡‘£Çx¶QWW§ÓÎ<«åûåÚhÃ^eÜÆÌéçüN<çwmrŒ\0\0\0ŠÁ38¯ßc=~òÉÚ}÷]õğ¿Qm<sì)\' 3gJ’NüR’ôÍwß®¼1•RÇ«>\0vöyçëãñ´lÙ2{ÖªË07­hÒø	Ÿê°CÒ‘GüB;vÌhc£^½tÎoÏTŸ>½3×µk§:jÑ¢ÅÚn›­uñùhõ¡¶£~ùKÑEÚ{ÿÔØØ¨]®úp_mm­~qØ!zô‰\'5ôÈ_µj7¬‡yL}wØN›õé“W=nV46ª±±QS¦NÕ£O<®ÓN:Q??ä –óİeç:ğ§ûë†›nQSóÊ™ùÁƒVÍú®X±Bƒí­Ë.ºÀÜfò±\'ôÒ«¯fËwÌ\n9F\0\0\0Å[ºd±íª!y÷Ñ\'š5g¶6ßl3õÎÚb®Ğ–/_®”¤ºx<#\\744èWC×‰\'§ƒò˜5{¶?òııÎ¿x^U0õõõª¯¯W×®]•J¥B]!Q’,X X,¦.]l[õ¥ÛlX¾\\]ÖX#ãx®cVè1\0\0(†¢çr5sÖ,­·îºù×3s–Ö[/ÿz*A®cÖ–Æ\0\0T§6œ\0\0\0+ó•\0\0€¶Œà\0\0\0œ\0\0\0‚3\0\0\0`Ÿùã^Ì\0\0\0\0¼Å$±«\0\0\0€¥\Z\0\0\0€A<™LfH$‘7’İ†_[Aıq«+—2a¥ë,ÄøB¹ô7ªÇÂZõùì7>aúœo=¥x>=7,cèWÆëçİYÎRÆ­¾R?ŸÃH&“‘½îH¹= ÒåúûÂívg¹\\_33–jò8»nKàğ\Z·_Ò~õæ{^•ø‹©úÕca­Çúó#aúœo=¥x>±(úhéŸõÊáyœ‹(ûåx@%Šê÷§ó¸Ûm,ÕP©¿‰DÅõÙ‹å\\Ü\'·ÙM¿¿\\ÃªÇÒç¨ÊXõÙ2†ÖqB¥şì•B¡\0(G–Éª0“CaÄÓÕQ½İ\\Ê_t‰DBÉdRAçëÌxĞ:Ë[f1½êq+—ËcjíOË;ùÔUÀ[O9Ì\Z¶åpe]ög0èvËŒ‡W]\0€ÖÒùÎòšé7#í–å¼ê‰»UæÕHúXv#A·»ÕéÖ^TœƒQÈv,,cèÖßì2ÖÇÂyÿ(úãl?Ÿ5AÅÍùkçc…(ú\\ì?N‹Õç¨Ê±¼†YóÖ×B¿±	ó³\0X¥Ğ?–×ç¸%Yßâµˆ*ˆ•K;VÖ1òêg1gÒ‹Éo\\\n5cÄ2;hUĞ¯¤åõ\ZbywËëA¯2ÖçO±–è\0\0\nÇob0-ì;ƒ–6âÙ	úÅåÕÁr}Øï¼Šİ|Ë—ÓLzT¬çæœËe\\ÊayF®*eœ-}ˆê5ªÜ_ë\0 -zİzÎwR¥ê>õÛì~Üœb¬S­Ä_ÜÖõHnÊ5\\ú©äĞ\0@¹+U\nœ‹LËõ/—03Á¹Œaö}*-<bİpĞxDL£·–1È.SnZÊärÕ¬çÊa\0Ú¯å…x­Í~\r%“ÉŒKnçòéïì\0c}K3—…í_[aX?e]#î÷VõÃVÖöòCË‡,ò¹.ë ­·»•³<–?¤¼D±>7Êq;†–2QıœâÜİ^£œeüó–z¼ÊzİæUÆ­œõÃ†\0P-rÍ\0é×hËkz˜ß¹@\0\0\0à.\\@9zkŠ™H\0\0¢ÁŒ3\0\0\0`Pu»j\0\0\0\0…@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€A\\’’É¤$)‘HdÜ˜>ÍY.è¾‰DÂ³·û…áÖ¶³-KİÉd2°œ¥L¹ñz\\İØd?¯İê³”‰¢-·Ÿ±Bµ±@U#\0\0¼IDATu=A?_ÅgËk]”ı‰òñrÖç7Æù´f|Ê¥0¿›üÊäÓ¯°Ï\rëïJËó\'¨L.…ß¸óu#ß1Œjœ+yÓåJıÚ[‰|gœH$LOº0õäÃëÉ¦nËy„=W”¿\\ŸÇNÎçŸW}–2Q´•}{!ÛŠºô1¯6Š5ÎÖ×:k[ÙõùÕ‘ïó1è~ÅŸr¬Çíg%—2A¢x®Z~WZ?–2a¿q)æëFcÕ8Wê:•úµ·ÕHù…Ù Ú ûå¢RgS“Éd¨\'U>Á>ª?PªUT/L^õYÊd×é÷âæWO!ÿÍeœüêñ+ç÷¢ìÕŸ¨úla=¯ Qşl†	ÍÎö-÷­&–×Ş°¯ÏÙ÷•\nó\\-õsL²>gûA÷Ë¥Bav™jC¿råşÚ[nâ^=…‘H$Z½èøÕ•~{ ÁÎíÁµ<IÂ”IŸZ”!&—2~}±ôÙë“ 6·ûXÕcçìÛ*õ¬jå÷s¾†TÚã•oóy–Ó/ªB¾–‹b¿¦Dõ»2Ÿ~{=®¥èK®í¡µŒTcVµ¾ö–Ju œÁØòÖ‡_=Åâ|\"d¿½Uc-ãl\'è—˜õĞòj},¼nóë³å]ËÛXaŞóîÙõëÅ9ª™,Ës#¨ôíQœ{>³o…PèC¯zŠñü)F;é¶\n9>a_ñ\\ÍõwS¾ï\"xõ\'ß2nœã\Z¦ ß\'A“C…xå[ÆÒ–µL%aTŠùÚ[)âÖ‚Q½°ó/®Jüë)ßĞë»Åşa©ÄÇ´X²_¬+a¡_l‹9VÌö¢åï‚bÕ“oË;Qóû]é÷n›Ûñ ~f‡ñ úsym)·1´–)§1ŒR9¾öV\nsp’=ûg™õD¦r	Íi–™ÛR=–åòŠê—vTmE¥Xm¹ÍÌ•Ë§L¹(Eh®¤ñ)7^ïzù•µÔU97Q<Ç¼Â_.¿Êy½Ê”ÛF©­¾öF!’}œ³ß&w³Ü¯­ğ{;£ÜB³³½ì#zmá­®j=¿|–\'…Às¬µ¶üsZ­¯½¥’wpZët¿\\äºÖO)×ñ”shóÇPĞåôÃ›ÏxZÖ€[ÊDÕVØ±õ*_Œ>‡QÌqÎ·?ù*ÔÏN1Ç§-ğú,B)Ÿ«Ö:\nõ\Zö¼J1†Åø9Í¯½•%–L&SÎ~Ó÷~k\\ıŞÈ÷m\0/nm;Û²¼5äV>L¿\0beYëf=TĞãÔgËcj©Çï¾¹ôÇÚFPÙ¨~¸Ãü|ø•‰¢­¨K[V~õøıì[!Æ9ÌıóíOØ×Ã°?;ne‹5>^¯^¯…úypkÛí¸õµ®ır+“ëkåõ »¬õ¹“k›ÅxlİÊärîa~¶üêñ«ÏÒn[|í­D1I©ÀRğT‰aUbŸÃjç\0\0Š+’5Î@©•ÛR\0\0P}˜qÎC%¾EQ‰}¶ªæs\0\0¥Gp\0\0\0Xª\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0ƒx2™Ì8H$\nÚ`2™l#İ§B÷ÅÂ9>åĞ?Ù¥Svß+é¼\0\0\0ÊA´28¥Ã“_øÊW!ë.„ì\0_îıw`çc\ZT\0\0\0ÁÊr©FPè+…rëU¥ö\0\0 ÜÄƒ\n¸Í²ú½íïV&ûv¿¥~Kœ÷³”Ë.›oˆŒ¢?neÜîEŸÓËbr©ÃÚg¿s[Æï\0\0@©Å’ÉdÊy l¨	|¬È¬½Ú·ôÏÂºö;(¤‡C/aúfÍz˜Ç)ªçB>Ï\0\0€R*ê\ZçJ’½^8Lùbµi­\0\0\0ù\\ªpÊ)°–S_\0\0\0*]Y~8\0\0\0(7%ÎÉd’e!Íò¼‰ª\0\0€“ï‡¥hvÕğ*´«†_[–—YúãÅò!»\\>@èVÖm÷‰\\vÉåƒ^e£zÜs-ãVÎY6—=†-\0\0à“”\n,UÁH…S¨€Êc\0\0ÊQÕ­qæ-øÊFh\0\0åª*gœÃ,Y@n¢ZÊÅ²\Z\0\0€b¨Êà\0\0\0D­ê–j\0\0\0\0…@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0j’É¤’ÉdÑ\ZL·ç×f±ûTNÚêy\0\0”»\ZIJ$Ek°˜mU\ZB3\0\0@ùŠ—ºn×\0\0\0(7ÁÙm4;Øf—ñ\n¾–Ug¯v‰„©\\vÙ°<èÜİêõ;T_aëIÏõÜ\0\0)–L&SAA7(İ\'ûx®u¸İö{+Ë¹GU&èxØ¶¼\0\0rÉ®\ZAø«ÄYO·0šH$BŸCTõ¤Y>\\é¬»’Æ\0\0 œå½Æ9ì¬g%IÏçü£ª\'ßû\0\0 w­fœ«)øFÁ9;œÏØDU\0\0\0J##8èVÉ^‘kèÍµË^ÖÅØï:ª~´å½¹\0@uˆ%“ÉTöÁ0;Bd—ñúğŸu§‹ :Â|øÎ¯‹\\vq+¦?ÖİBüÚÉß|–ˆXîU\0\0€r“Ô*8W“b6\"\0\0@uŠdWrRÊ%„f\0\0€êU•3ÎÖ²DİN!Û\0\0@iUep\0\0\0¢VuK5\0\0\0€B 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0ñd2™q ‘H´Ád2ØFºO~å¢ª§˜,}ö»ošõ¼-e©\\ú\0\0…\Zie¨I›ì ¥¨ê.d%ß>‡	åRË¥\0\0\0Qˆ—ºn¢\n\\7\0\0\0D%08-åp.‡ğzk>»¿%~oïGU[]^}ö;/kŸÃ,™Éw	JĞ¹²r[>\0\0`K&“)ç\\[v°*—o¸Ê··ã–cù„¾0÷µô;×1²{.}:Fh\0\0•,.ÙÂ²(wa×@§ƒh®8,ö:qB3\0\0¨t¾K5¼f\\ƒÂÉuœóÁc\0\0û8£(ŠùG\0\0@!”,8§—”K=ÅTn}.V‚Âs¹\0\0€SË‡ƒ>d–.´¬ ß‹sXëË·ËQ~80»Í\\>`iİÅ\"Šs·°îLâ<nÙ	…e$\0\0 Å$¥K\0\0\0mkœ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00h¹r e›0¯Û³Ë¸•³u™_9«(ú\\ì2–ó*aúZŒóª¤±\0\0å\'&)eÙ_Ø/híwì·\'qT{$Gİçb—	{^•²çq˜~ãœ*eÜ\0\0@ù©ñ›éÍ%€:ÿ]¬«À9Û‰ªÏÅ,“‚\0\0@qÅ¥ÌÌJS©ı‚ß»Ö«æS&Œ(¯ºèÕŸ\\úœÏ\Z\0@ÛózZĞšáìÛÓA.êµÀÖuÙ¹ô¹Te‚î›ş·[Ùãìü>h)IØ2a¹õÅªP}¶,«±Ô\0\0Ú†xvÀtù†Kñ\n¿^m…Ğj>a×5‡ù0^>eÂÈ\'<çÚËy~ÏM\0\0ĞöÄıfìÂ*VÀˆò^Q„Ğ(ËDÍò‡EØûV;·™{\0\0€ŠÛÇ™0ƒ(}@3‘HıC®\0\0 ¼åœİÂE.áÖm\r´[™°õº±ô¹˜eJÍ:ö• ƒúìõØ¸}°²ÒÎ\0\0D¯Õ>ÎRn;}/Š]¬kc£ês±Ëø‰²bîªQnÏŸìãìª\0\0¬b’R¥î\0\0\0Pî*n3\0\0\0P\ng\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`—ü÷jë²JÜ­Øe,Ü¶T«ÅÜ»ºRÇ\0\0”·\Z¿;8Ã×•ÔŠYÆÂZOv¹R—	{n¹ÖÑ–\0@!DråÀ  U/Ù3ŒAõ¸Í~f‡Ñb–ÉE¥…Ã|_\0\0€rO$‘Î\\Fõ–¼µb]¦»y-uÉ~LK¹l&»®BöÙ«\\Øz¸r \0\0pã;ãìœMù	\n©Ùõ]:—™ã°õXÏ«Xeüîëöo\'¯ËH—jÙLv¿‚úœoÂ<Šuî\0\0 zÄƒ\nXfãœÇ-!)]>–ÂÖc)Wm3ÍÎYË9å;So-S.ÂŒßy¥ÇÙùÜ¬–ç\0\0ÈO`p¶(ÕòŒ(Bs¹•‰šW›åÚßb°¬··¼3\0\0Ú–¼?XÉ¡ğÂ2\r\0\0-Tpn³×æºıš×úÓ|ê	ZÛZì2¥VèõÙå,è¹Jx\0\0i±d2™Ê>˜½Ùë6·Û­õXnÏ.ç¶&:›µ?ne-»4²ŒŸ(Û(å®\Z~my}¸ÑÚŸìÀE=^e\0\0@Û“Ô*8\0\0\0È”÷\Zg\0\0\0 - 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0ƒx˜mÒò¹øH[|¹í¯›K}Q·Y)¢Ø>Ğ«l®¯ñ«\'×şäò˜â9aÙj±Ğøù\0À_Mú\niAz°\\ #è6k[^¢üÅêµwpØ2Õ(Ìãå,ã,ëU—W=ÖçW!úVÔ¯\\Wü|\0àÏ´T#ŸĞ\\	,¡-Í†å*Üfı®¤˜o=¹ô…ÇÏ\0 ZÄƒ\n8Ã†WH)ÅŒ‘W²\\…ÎM®¿Ü­K\Z²Ç¯PW«zŒÊQ%Ï8ZŸ‡nÇ²Ï7¨.§B_í°Ú~¾,\nõ³œëÒ5®`	\0å§&™L*ı%ùÿ¢Ï•ó—¬³­¨êË2Û¦Œß’¯€áV¾KY²ëğZ®`å÷Üp+´\\\'ŠÇİÚ_9kŸ-¢x¬¼¾wÖë÷ÜˆòùãìK®u”ÛÏW˜>[Ûòç Ç¡T)\0 ñì ìö!%·ş°aÌ2›Vzæ\'lœ3F^÷³”I³KP[Îó(‡™%¿ç†_ˆ.EßÃôÇòœÛv¡Ïİï9V¨çOµü|YïÕæúGTTu\0\nÇw©†åíg„·òÎ_Ü¹Ô™V®K5¢j¿ÔçQ*–¥Q<ÊQ?_Öûå;†ùÎ|»õ	\0P>×8£x²—´äòK“_´mWÏŸ¶1\0ø)ÉPªqV,-—u³Ù÷)õzFË9XÊ­İ´²ÔÕ\ZêRËeìËíùSH…zœK=†QıÌ\0\n+–L&SÎÖµvn\"ÌæW&Ê¥~ë§İÖRZúbíoP¢ª§ØÂ³W·rÖõîAåréOTãœk[^í¹…¶|Û*ÆyUÊÏ—ETã4>Q¶\0(®˜¤T`)\0y«æwZÚ\nC\0hÛJ²Thk\\\0\0T>fœàmöêå²\0@e\"8\0\0\0,Õ\0\0\0\0Î\0\0\0€Aœµ˜Åã÷±°ƒu‹+¿º\nİ¯ºÂ>¿ü¶jË·\0\0\0aÅ¥ê¾`B¹ğ[¯ìî¬)‡şx]¨$ìP¢|nò<\0\0¹ÈXªÁœ»|¯Øe	ºÖ±\"ô+„ºpşH\0\0•*şGzĞí­ÿì¿R]ÙÌï’¸a®Êe­\'*aÃ¢W_¼B÷ÇKTıÉµÍ ãAW´ªË‰«º\0€\Z)øÒÀ~Äy›3x‡-Vö,púßaÛòªÇ)ÌŒp¾ÂC¿:œ_ae/«°„RkŸò•Ïs\'ûqt{\\Kõ|\0\0å¯es¾ëf-¡!ª`áì¯Wß-mYê)&Ku›5M—÷ZvMq˜5Î~ı)”ôcUÈ¶‚>h™İ>³Í\0\0T¿–¥\ZÖ_ü^å,÷/f¸¨´ šó™.„°ı©´Ç#¨¿Îğl)\0\0*û8DµÌÀ¯~‰ğUiX¦\0@ÛRàl	š…£¥j+*¹ô¹ÜÎ3h}p9Èå¹šı=á\0€¶!–L&SR~®(ö®\Z^k“ıLĞn!nõDÅúáK¿2~õ…ÙQÄÒk=–şXn·ˆê¼ÜÊ²«\0\0°ˆIJ•º@!”Ûì6\0\0¨l¬qFU\"4\0€¨Åƒ‹\0å¥\0\0 ĞXª\0\0\0°T\0\0\00 8\0\0\0kœ­[»e\0\0\0ª‰ïŒ³sg¯«¤–\0\0Ğ°T\0\0\00(Ù%·\0\0€JypæÂ\0\0\0¨F‘gB3\0\0\0ªkœ\0\0\0ƒHƒ³Û®\0\0\0@5ˆ|Æ9(<óÁA\0\0\0T\"ß $	× ëu\0\0\0 ZÅ$¥Jİ	\0\0\0 Üñá@\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0â~[ÍÁ.™Lú][ç ñ©Ô¶\0\0@ÛÑ²3A#w–½¬-†I—sş»\Zs¯oö\0\0…’ÓRr\'åÖ\0\0\0Tß+ºÉ©Ù³£^³¥náÖí\n„ÎW·zÂôÇ¯ ş„é³[Ûa8ëÉşw>uyÍ^Gqîaûâü¾œk\0\0@ÛK&“)ÉüB˜_p{,}<(üX‚˜[=Q‡ßñ\\úœÏR¨‹0çK¿‚n+Öcaíkµ-\0\0¹1Ï8çÒaĞ9ƒêWO>4l=°S¡ÇÒo¹MØçOÔx\0\0Éœ£˜qs†k]agšÃÖƒòôåòü\0\0ˆRà‡£*‰D\"pw‰bö§\\ø­qÆ*Q<\0\0\0råœ£\n©Î™Bg}aÃO%„æìsµp×¿ÉÒç\\Î+ª¶r}şøµæ|¢:w\0\0PÙZ>˜–ı¡¨0ëÓ÷Ïe\'ËB,ı±^h$ê%‚v	êWTû8Gu^Qï,QèN¬me—±<V~õ\0\0€¶#&)X\n©fè\0\0*EN@AybI\0\0@á0ã\\e¬KU\0\0\0Á\0\0\00`©\0\0\0`@p\0\0\0â¬‰FĞVyŒs4¬[$\0\0D­å’Û„‘ÜYv²ºhGTû8W3v\0\0¥”ÓRr0åÖŸJÄ\0\0ø‹É”°²gG½fK­WtÎ¸ºÕ¦?…¾Z]ĞXXe_^ÚùïbÌ:»gTKKÂ<înß»ÕÁŒ<\0\0(…P3ÎùÃD\"Ñòå<î¬Ó+HYûc©ÇÒkŸ³ÛÎ%Ì¹õ?ûß…âõ˜úw.uçSWTã\0\0óŒs>³|éÙ_çª_=–6,ı!\\ùóC–n\0\0\0d2ç(Ş\Zw†gk]^eÂö‡\0İš%4ç3Û\0\0Pm—jD¹4ß·ş£îO¹ğ[ã\\Èöªi\0\0\nÍ78G°œ3ÍÎúÂÃJ|ÙçjQˆ5Î^ı(ÄærÎ•Ø&\0\0hÛbÉd2å<½›A˜õÆéû[vFºİk	AØ]6‚–{ø•µ”q+kY3ìÕVTû8ûínÕc\ZÔVv=ÎúòmËëv\0\0€B‰IJ–\0\0\0Ú¸œ.€\0\0\0´5g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`»}[€…v[»(Æ˜Ç\0\0 Z5R4Wôƒ;g€\r\ZgÆ\0\0 |Å³¯TçŞ˜¹¬,Å|¼˜İ\0\0mé(~Wkó»Bóx˜å\naú‘ËU\nsi/×:œõ„¹Šavy·+zÕi}¼,å²Ë†½r \0\0@µ0_9Ğ\Zİû…Û0a+h)C”myµoxö«#LÀâ2Ø^|}\0\0ĞÅ¥èfVƒDµ†7;4j½p”k!4ß\0`\0\0Š/.ù/§ˆR1_¾mY–šä\"ô£Ø=ƒ\0\r\0\0P<yïãì,yk•tH®fmá\0\0j¢<ÙËœÇ¼3lUb°«Ä>\0\0T³X2™lùp`zßérn,H³ÔãÅë‡…ØÁ#» ãYë	ê×‡Ã¬C*kùğ_Tc\0\0P-Ì»j íbé\r\0\0@kœQ}X&\0\0Ğ\Z3ÎpU¬-\n\0\0*Á\0\0\00`©\0\0\0`@p\0\0\02.¹ë6ra·.³nfi/l;\0\0\0@.â~Õ+à:÷z¶”q«Ó‹åÂ)aÊ\0\0\0Qˆûİh™©\r3››o˜%4\0\0 Tjr	¾ù\\…¯Ë&‰Ë3\0\0\0)ßg§ àë·ïo˜ĞlÙ?˜=†\0\0Pl1I)k(¶Ôìòa>øg©Ç\ZÊùp \0\0\0¢8ãEøôÚƒ@\0\0€Já»3\0\0\0X)ôPÒ[Íy}Ÿ«¨ê\0\0\0\n!–L&SÙÃ®MsË‡ıêÉµŒ_Ÿ\0\0\0€ 1I­‚3\0\0\0€L¡—j\0\0\0\0mÁ\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0Ä%.t…¨Æ0™L–ÍãàÜÖ¯}²\\>İ)—­\nƒÚsyxëøğó\0@u¼ä6Š§Ü.\0“H$ŠÖ\'¿v¼®óKk{ÙõXûäW\0\0T¾¸ÄLXÚòæ;£šoˆ\rÛv¾a–Ğ\0@Û÷{»Ùò}Û>èmt¿·Ís½JaP_üÎ+Ì¹ç;†Ùç”kõº_öq¿«7–‚åJ•Nùu¯Ç£Â\0\0(o5~áÃù‹?‘Häœa¥ê±œ—×€°ÁİÚ–³ìï£–ïøyÕWA¡9½<Ãú‡˜_;ÙuåR\0\0T¢¬qNÏî9×›æ´¢ª\'—v«I¥†<Kğµ¬qv›á÷{>yÕc]O\r\0\0ªCÑ>è½éïKYO®mW:Ëz9ŠâñZÂ\0\0à§¨û8Gµ< ÊeÕÄmLŠ½T€\0\0ÊAQ‚sv°ÊgsõT‚\\Ã¨sLª9pfOTáõÊ\0\0ÀK,™L¦œ¬;2äºãƒ¥-¿rQìªa©\'ÌÎAeÃŒa¾»—xµé×FĞnQôÇOĞãîds}nø[®ÏÕ\\Ï\0\0 rÄ$¥K•H!gL«y6\0\0\0Ñ+Û+F9³íT©A¹ZÏ\0\0 R”ÍŒsTK0ri‹Ğ	\0\0€ eœ\0\0€rVÔíè\0\0\0€JEp\0\0\0â¬÷FĞå–g\0\0€ÊÖ²«A.w–fíIìÜE„­ò\0\0\0ÊONK5ÊíÊjåÖ\0\0\0TŸĞû8g‡TëUñ¬WêsÎ¸ºÕ¦?~õDqu¸ ±°Ê¾t´óßÌ:\0\0”‡P3ÎùÃD\"Ñòå<î¬Ó+ˆ[ûc©ÇÒkŸ³ÛÎ%èºõ?ûß\0\0\0(-spÎgİ­%tº•Ï·?O\0\0\0DÅ´T#Š«¥—N„©Ë«LØş \0\0¯Àç(wxğZòF5î8á·Æ\0\0\0åÁ78GR3ÍÎúÂÃJÍÙçjÁ\Zg\0\0€òK&“)çì]#Â¬7Nßß-à†İ¡Â­]K¬\Z‰bW\r¯²^}·´Å>Î\0\0\0å)&)X\n\0\0\0hãBïãŒòæ\n†\0\0\0\'§+\0\0\0m\rK5\0\0\0\0fœ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0œ\0\0\0‚3\0\0\0`@p\0\0\0Î\0\0\0€Á\0\0\00 8\0\0\0g\0\0\0À€à\0\0\0ÄûXK«oşƒOê¬ú•J¥ZntşÛÉëxZ×Î+´ë6óõİœš0¥³šš#ís(:tĞ1Ç­ç{^3gÎÔ~û\rÖ‚õşûïk‹-¶Ğ€ıõàƒµ”¯­­UÏ=µá†½Ô¹sgÕÕÕiuÖi¹¿$m´ÑFÚo¿Ázá…µÿşC´lÙ2=ñÄ“jllÌhûW¿ú¥:wîìÚ¯‰?Õ[o½ê\\b±˜vÛm7m±Åæš;w®fÌ˜¡o¿ıV3fÌt-?dÈ-[¶T£Gñ¬Ór¾’4xğ¾ª©©Õ+¯¼ØOK»\0€ü¸ı.vkllÔïÿûbv	(k±X¬Õÿc±˜jjVÎ#×ÔÔ¨¾¾^]ºtQMMjjjT[[›ñõÿ#â‚ Q~Ñ\0\0\0\0IEND®B`‚',3);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discussion_answer`
--

LOCK TABLES `discussion_answer` WRITE;
/*!40000 ALTER TABLE `discussion_answer` DISABLE KEYS */;
INSERT INTO `discussion_answer` VALUES (1590084659,1,1,1,'123123','0000000000',0),(1590084661,1,2,1,'123123','0000000000',0),(1590084663,1,3,1,'123123','0000000000',0);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discussion_topic`
--

LOCK TABLES `discussion_topic` WRITE;
/*!40000 ALTER TABLE `discussion_topic` DISABLE KEYS */;
INSERT INTO `discussion_topic` VALUES (1590084591,1,1,1,'Why','123123','0000000000',0),(1590084591,1,2,1,'Why','123123','0000000000',0),(1590084593,1,3,1,'Why','123123','0000000000',0);
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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enroll`
--

LOCK TABLES `enroll` WRITE;
/*!40000 ALTER TABLE `enroll` DISABLE KEYS */;
INSERT INTO `enroll` VALUES (1590084200,1,7,'0000000000',3,3),(1590084200,1,10,'0000000002',3,1),(1590084200,1,11,'0000000003',3,2),(1590084200,1,12,'0000000004',3,2),(1590084513,1,13,'0000000010',4,3),(1590084513,1,14,'0000000011',4,1),(1590084513,1,15,'0000000011',4,1),(1590084513,1,16,'0000000012',4,1),(1590084513,1,17,'0000000013',4,2),(1590084513,1,18,'0000000014',4,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1590084524,1,1,'zm','123','0000000000',3,1590084524),(1590084572,1,2,'zm11','123','0000000000',3,1590084572),(1590084573,1,3,'zm11','123','0000000000',3,1590084573),(1590084690,1,4,'zm11','123','0000000000',3,1590084690);
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
INSERT INTO `question_tag_table` VALUES (1,4),(2,4);
/*!40000 ALTER TABLE `question_tag_table` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (1590084690,1,1,'123123avc'),(1590084690,1,2,'tag');
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
INSERT INTO `user` VALUES (1590083923,1,'0000000000','9990@ustc.edu.cn','Super0',4),(1590083923,1,'0000000001','9991@ustc.edu.cn','Super1',4),(1590083923,1,'0000000002','9992@ustc.edu.cn','Super2',4),(1590083923,1,'0000000003','9993@ustc.edu.cn','Super3',4),(1590083923,1,'0000000004','9994@ustc.edu.cn','Super4',4),(1590083923,1,'0000000005','9995@ustc.edu.cn','Super5',4),(1590083923,1,'0000000006','9996@ustc.edu.cn','Super6',4),(1590083923,1,'0000000007','9997@ustc.edu.cn','Super7',4),(1590083923,1,'0000000008','9998@ustc.edu.cn','Super8',4),(1590083923,1,'0000000009','9999@ustc.edu.cn','Super9',4),(1590083923,1,'0000000010','99910@ustc.edu.cn','Super10',4),(1590083923,1,'0000000011','99911@ustc.edu.cn','Super11',4),(1590083923,1,'0000000012','99912@ustc.edu.cn','Super12',4),(1590083923,1,'0000000013','99913@ustc.edu.cn','Super13',4),(1590083923,1,'0000000014','99914@ustc.edu.cn','Super14',4),(1590083923,1,'0000000015','99915@ustc.edu.cn','Super15',4),(1590083923,1,'0000000016','99916@ustc.edu.cn','Super16',4),(1590083923,1,'0000000017','99917@ustc.edu.cn','Super17',4),(1590083923,1,'0000000018','99918@ustc.edu.cn','Super18',4),(1590083923,1,'0000000019','99919@ustc.edu.cn','Super19',4),(1590083923,1,'0000000020','99920@ustc.edu.cn','Super20',4),(1590083923,1,'0000000021','99921@ustc.edu.cn','Super21',4),(1590083923,1,'0000000022','99922@ustc.edu.cn','Super22',4),(1590083923,1,'0000000023','99923@ustc.edu.cn','Super23',4),(1590083923,1,'0000000024','99924@ustc.edu.cn','Super24',4),(1590083923,1,'0000000025','99925@ustc.edu.cn','Super25',4),(1590083923,1,'0000000026','99926@ustc.edu.cn','Super26',4),(1590083923,1,'0000000027','99927@ustc.edu.cn','Super27',4),(1590083923,1,'0000000028','99928@ustc.edu.cn','Super28',4),(1590083923,1,'0000000029','99929@ustc.edu.cn','Super29',4),(1590083923,1,'0000000030','99930@ustc.edu.cn','Super30',4),(1590083923,1,'0000000031','99931@ustc.edu.cn','Super31',4),(1590083923,1,'0000000032','99932@ustc.edu.cn','Super32',4),(1590083923,1,'0000000033','99933@ustc.edu.cn','Super33',4),(1590083923,1,'0000000034','99934@ustc.edu.cn','Super34',4),(1590083923,1,'0000000035','99935@ustc.edu.cn','Super35',4),(1590083923,1,'0000000036','99936@ustc.edu.cn','Super36',4),(1590083923,1,'0000000037','99937@ustc.edu.cn','Super37',4),(1590083923,1,'0000000038','99938@ustc.edu.cn','Super38',4),(1590083923,1,'0000000039','99939@ustc.edu.cn','Super39',4),(1590083923,1,'0000000040','99940@ustc.edu.cn','Super40',4),(1590083923,1,'0000000041','99941@ustc.edu.cn','Super41',4),(1590083923,1,'0000000042','99942@ustc.edu.cn','Super42',4),(1590083923,1,'0000000043','99943@ustc.edu.cn','Super43',4),(1590083923,1,'0000000044','99944@ustc.edu.cn','Super44',4),(1590083923,1,'0000000045','99945@ustc.edu.cn','Super45',4),(1590083923,1,'0000000046','99946@ustc.edu.cn','Super46',4),(1590083923,1,'0000000047','99947@ustc.edu.cn','Super47',4),(1590083923,1,'0000000048','99948@ustc.edu.cn','Super48',4),(1590083923,1,'0000000049','99949@ustc.edu.cn','Super49',4),(1590083923,1,'0000000050','99950@ustc.edu.cn','Super50',4),(1590083923,1,'0000000051','99951@ustc.edu.cn','Super51',4),(1590083923,1,'0000000052','99952@ustc.edu.cn','Super52',4),(1590083923,1,'0000000053','99953@ustc.edu.cn','Super53',4),(1590083923,1,'0000000054','99954@ustc.edu.cn','Super54',4),(1590083923,1,'0000000055','99955@ustc.edu.cn','Super55',4),(1590083923,1,'0000000056','99956@ustc.edu.cn','Super56',4),(1590083923,1,'0000000057','99957@ustc.edu.cn','Super57',4),(1590083923,1,'0000000058','99958@ustc.edu.cn','Super58',4),(1590083923,1,'0000000059','99959@ustc.edu.cn','Super59',4),(1590083923,1,'0000000060','99960@ustc.edu.cn','Super60',4),(1590083923,1,'0000000061','99961@ustc.edu.cn','Super61',4),(1590083923,1,'0000000062','99962@ustc.edu.cn','Super62',4),(1590083923,1,'0000000063','99963@ustc.edu.cn','Super63',4),(1590083923,1,'0000000064','99964@ustc.edu.cn','Super64',4),(1590083923,1,'0000000065','99965@ustc.edu.cn','Super65',4),(1590083923,1,'0000000066','99966@ustc.edu.cn','Super66',4),(1590083923,1,'0000000067','99967@ustc.edu.cn','Super67',4),(1590083923,1,'0000000068','99968@ustc.edu.cn','Super68',4),(1590083923,1,'0000000069','99969@ustc.edu.cn','Super69',4),(1590083923,1,'0000000070','99970@ustc.edu.cn','Super70',4),(1590083923,1,'0000000071','99971@ustc.edu.cn','Super71',4),(1590083923,1,'0000000072','99972@ustc.edu.cn','Super72',4),(1590083923,1,'0000000073','99973@ustc.edu.cn','Super73',4),(1590083923,1,'0000000074','99974@ustc.edu.cn','Super74',4),(1590083923,1,'0000000075','99975@ustc.edu.cn','Super75',4),(1590083923,1,'0000000076','99976@ustc.edu.cn','Super76',4),(1590083923,1,'0000000077','99977@ustc.edu.cn','Super77',4),(1590083923,1,'0000000078','99978@ustc.edu.cn','Super78',4),(1590083923,1,'0000000079','99979@ustc.edu.cn','Super79',4),(1590083923,1,'0000000080','99980@ustc.edu.cn','Super80',4),(1590083923,1,'0000000081','99981@ustc.edu.cn','Super81',4),(1590083923,1,'0000000082','99982@ustc.edu.cn','Super82',4),(1590083923,1,'0000000083','99983@ustc.edu.cn','Super83',4),(1590083923,1,'0000000084','99984@ustc.edu.cn','Super84',4),(1590083923,1,'0000000085','99985@ustc.edu.cn','Super85',4),(1590083923,1,'0000000086','99986@ustc.edu.cn','Super86',4),(1590083923,1,'0000000087','99987@ustc.edu.cn','Super87',4),(1590083923,1,'0000000088','99988@ustc.edu.cn','Super88',4),(1590083923,1,'0000000089','99989@ustc.edu.cn','Super89',4),(1590083923,1,'0000000090','99990@ustc.edu.cn','Super90',4),(1590083923,1,'0000000091','99991@ustc.edu.cn','Super91',4),(1590083923,1,'0000000092','99992@ustc.edu.cn','Super92',4),(1590083923,1,'0000000093','99993@ustc.edu.cn','Super93',4),(1590083923,1,'0000000094','99994@ustc.edu.cn','Super94',4),(1590083923,1,'0000000095','99995@ustc.edu.cn','Super95',4),(1590083923,1,'0000000096','99996@ustc.edu.cn','Super96',4),(1590083923,1,'0000000097','99997@ustc.edu.cn','Super97',4),(1590083923,1,'0000000098','99998@ustc.edu.cn','Super98',4),(1590083923,1,'0000000099','99999@ustc.edu.cn','Super99',4);
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

-- Dump completed on 2020-05-22  2:26:31
