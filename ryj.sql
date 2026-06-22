-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 22 juin 2026 à 11:57
-- Version du serveur : 8.0.31
-- Version de PHP : 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `ryj`
--

-- --------------------------------------------------------

--
-- Structure de la table `activites`
--

DROP TABLE IF EXISTS `activites`;
CREATE TABLE IF NOT EXISTS `activites` (
  `idActivite` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`idActivite`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `commentaires`
--

DROP TABLE IF EXISTS `commentaires`;
CREATE TABLE IF NOT EXISTS `commentaires` (
  `idName` varchar(20) NOT NULL,
  `idAnimal` int NOT NULL,
  `commentaire` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idName`,`idAnimal`),
  KEY `fk_animal` (`idAnimal`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `especes`
--

DROP TABLE IF EXISTS `especes`;
CREATE TABLE IF NOT EXISTS `especes` (
  `idEspece` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idEspece`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `fiches_animal`
--

DROP TABLE IF EXISTS `fiches_animal`;
CREATE TABLE IF NOT EXISTS `fiches_animal` (
  `idAnimal` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `idName` varchar(20) NOT NULL,
  `idEspece` int NOT NULL,
  PRIMARY KEY (`idAnimal`),
  KEY `fk_name` (`idName`),
  KEY `fk_espece` (`idEspece`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `inclue`
--

DROP TABLE IF EXISTS `inclue`;
CREATE TABLE IF NOT EXISTS `inclue` (
  `idEspece` int NOT NULL,
  `idActivite` int NOT NULL,
  PRIMARY KEY (`idEspece`,`idActivite`),
  KEY `fk_activite` (`idActivite`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `notes`
--

DROP TABLE IF EXISTS `notes`;
CREATE TABLE IF NOT EXISTS `notes` (
  `idName` varchar(20) NOT NULL,
  `idAnimal` int NOT NULL,
  `note` int NOT NULL,
  PRIMARY KEY (`idName`,`idAnimal`),
  KEY `fk_animal` (`idAnimal`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `participe`
--

DROP TABLE IF EXISTS `participe`;
CREATE TABLE IF NOT EXISTS `participe` (
  `idName` varchar(20) NOT NULL,
  `idAnimal` int NOT NULL,
  `idActivite` int NOT NULL,
  `dateActivite` date DEFAULT NULL,
  PRIMARY KEY (`idName`,`idAnimal`,`idActivite`),
  KEY `fk_animal` (`idAnimal`),
  KEY `fk_activite` (`idActivite`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs`
--

DROP TABLE IF EXISTS `utilisateurs`;
CREATE TABLE IF NOT EXISTS `utilisateurs` (
  `idName` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  PRIMARY KEY (`idName`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
