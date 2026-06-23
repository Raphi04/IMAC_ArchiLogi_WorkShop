-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 23 juin 2026 à 13:02
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `commentaires`
--

DROP TABLE IF EXISTS `commentaires`;
CREATE TABLE IF NOT EXISTS `commentaires` (
  `idCommentaire` int NOT NULL AUTO_INCREMENT,
  `idName` varchar(20) NOT NULL,
  `idAnimal` int DEFAULT NULL,
  `commentaire` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idCommentaire`),
  KEY `fk_animal2` (`idAnimal`),
  KEY `fk_name2` (`idName`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `especes`
--

DROP TABLE IF EXISTS `especes`;
CREATE TABLE IF NOT EXISTS `especes` (
  `idEspece` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idEspece`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `especes`
--

INSERT INTO `especes` (`idEspece`, `name`) VALUES
(2, 'Asterion');

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
  KEY `fk_name4` (`idName`),
  KEY `fk_espece2` (`idEspece`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `fiches_animal`
--

INSERT INTO `fiches_animal` (`idAnimal`, `name`, `idName`, `idEspece`) VALUES
(1, 'Patrick', 'cherrierbgdu77', 2);

-- --------------------------------------------------------

--
-- Structure de la table `inclue`
--

DROP TABLE IF EXISTS `inclue`;
CREATE TABLE IF NOT EXISTS `inclue` (
  `idInclue` int NOT NULL AUTO_INCREMENT,
  `idEspece` int NOT NULL,
  `idActivite` int NOT NULL,
  PRIMARY KEY (`idInclue`),
  KEY `fk_espece` (`idEspece`),
  KEY `fk_activite` (`idActivite`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `notes`
--

DROP TABLE IF EXISTS `notes`;
CREATE TABLE IF NOT EXISTS `notes` (
  `idNote` int NOT NULL AUTO_INCREMENT,
  `idName` varchar(20) NOT NULL,
  `idAnimal` int NOT NULL,
  `note` int NOT NULL,
  PRIMARY KEY (`idNote`,`idName`,`idAnimal`),
  KEY `fk_animal3` (`idAnimal`),
  KEY `fk_name3` (`idName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `participe`
--

DROP TABLE IF EXISTS `participe`;
CREATE TABLE IF NOT EXISTS `participe` (
  `idParticipe` int NOT NULL AUTO_INCREMENT,
  `idName` varchar(20) NOT NULL,
  `idAnimal` int NOT NULL,
  `idActivite` int NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`idParticipe`),
  KEY `fk_activite2` (`idActivite`),
  KEY `fk_animal` (`idAnimal`),
  KEY `fk_name` (`idName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `utilisateurs`
--

INSERT INTO `utilisateurs` (`idName`, `username`, `pwd`) VALUES
('cherrierbgdu77', 'CherrierGaming', 'canicuuuuuule'),
('testa', 'Test', 'caca');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `commentaires`
--
ALTER TABLE `commentaires`
  ADD CONSTRAINT `fk_animal2` FOREIGN KEY (`idAnimal`) REFERENCES `fiches_animal` (`idAnimal`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_name2` FOREIGN KEY (`idName`) REFERENCES `utilisateurs` (`idName`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `fiches_animal`
--
ALTER TABLE `fiches_animal`
  ADD CONSTRAINT `fk_espece2` FOREIGN KEY (`idEspece`) REFERENCES `especes` (`idEspece`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_name4` FOREIGN KEY (`idName`) REFERENCES `utilisateurs` (`idName`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `inclue`
--
ALTER TABLE `inclue`
  ADD CONSTRAINT `fk_activite` FOREIGN KEY (`idActivite`) REFERENCES `activites` (`idActivite`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_espece` FOREIGN KEY (`idEspece`) REFERENCES `especes` (`idEspece`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `notes`
--
ALTER TABLE `notes`
  ADD CONSTRAINT `fk_animal3` FOREIGN KEY (`idAnimal`) REFERENCES `fiches_animal` (`idAnimal`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_name3` FOREIGN KEY (`idName`) REFERENCES `utilisateurs` (`idName`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `participe`
--
ALTER TABLE `participe`
  ADD CONSTRAINT `fk_activite2` FOREIGN KEY (`idActivite`) REFERENCES `activites` (`idActivite`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_animal` FOREIGN KEY (`idAnimal`) REFERENCES `fiches_animal` (`idAnimal`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_name` FOREIGN KEY (`idName`) REFERENCES `utilisateurs` (`idName`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;