-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 23, 2023 at 12:09 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vacations`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_user_by_credentials` (`user_email` VARCHAR(70), `user_password` VARCHAR(100))   BEGIN
    SELECT * FROM users WHERE users.password = user_password AND users.email = user_email;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `countries`
--

CREATE TABLE `countries` (
  `country_id` int(11) NOT NULL,
  `country_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `countries`
--

INSERT INTO `countries` (`country_id`, `country_name`) VALUES
(1, 'Israel'),
(2, 'United States'),
(3, 'United Kingdom'),
(4, 'Iceland'),
(5, 'Japan'),
(6, ' Republic of Korea'),
(7, 'Italy'),
(8, 'Germany'),
(9, 'France'),
(10, 'Canada'),
(11, 'philippines');

-- --------------------------------------------------------

--
-- Table structure for table `likes`
--

CREATE TABLE `likes` (
  `user_id` int(11) NOT NULL,
  `vacation_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `likes`
--

INSERT INTO `likes` (`user_id`, `vacation_id`) VALUES
(1, 1),
(1, 6),
(1, 19),
(2, 4);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `role_id` int(11) NOT NULL,
  `role_type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`role_id`, `role_type`) VALUES
(1, 'Admin'),
(2, 'User');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(70) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `password`, `role_id`) VALUES
(1, 'Josef', 'Gvirtzman', 'yosef.gvirtzman@gmail.com', 'Qaz8035693@', 1),
(2, 'David', 'Fincher', 'thesocialnetwork@fincher.com', 'Zaq123123@', 2),
(3, 'John', 'Doe', 'johndoe@example.com', 'password', 2),
(4, 'Ugi', 'Fletzet', 'ugi@example.com', 'password', 2),
(5, 'Test', 'User', 'test_user@example.com', 'password', 2),
(6, 'Second_Test', 'User', 'second_test_user@example.com', 'password', 2);

-- --------------------------------------------------------

--
-- Table structure for table `vacations`
--

CREATE TABLE `vacations` (
  `vacation_id` int(11) NOT NULL,
  `country_id` int(11) NOT NULL,
  `description` varchar(200) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `price` float NOT NULL,
  `vacation_photo_filename` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vacations`
--

INSERT INTO `vacations` (`vacation_id`, `country_id`, `description`, `start_date`, `end_date`, `price`, `vacation_photo_filename`) VALUES
(1, 10, 'Summer in the amazing great Canada', '2024-02-11', '2024-02-25', 1000, 'western_wall_trip.jpg'),
(2, 2, 'USA National Park Tour: Discover the natural beauty of the United States with a tour of its national parks. Hike through stunning landscapes, see wildlife, and camp under the stars.', '2024-06-01', '2024-06-14', 3800, ' usa_national_parks.jpg'),
(3, 3, 'UK Historical Journey: Embark on a historical journey through the United Kingdom. Visit iconic landmarks like the Tower of London, Stonehenge, and the Scottish Highlands.', '2024-08-10', '2024-08-20', 2900, 'uk_historical_journey.jpg'),
(4, 4, 'Icelandic Adventure: Experience the otherworldly landscapes of Iceland. Explore geysers, waterfalls, and glaciers, and relax in geothermal hot springs.', '2024-07-05', '2024-07-15', 3500, 'icelandic_adventure.jpg'),
(5, 5, 'Japan Cherry Blossom Tour: Witness the beauty of cherry blossoms in Japan. Explore historic temples, enjoy sushi, and immerse yourself in Japanese culture.', '2024-04-05', '2024-04-15', 3600, 'japan_cherry_blossoms.jpg'),
(6, 6, 'South Korean Delights: Experience the vibrant culture of the Republic of Korea. Explore Seoul, visit ancient palaces, and savor Korean BBQ.', '2024-09-10', '2024-09-20', 2800, 'korean_delights.jpg'),
(7, 7, 'Italian Riviera Escape: Enjoy the stunning beauty of the Italian Riviera. Visit picturesque coastal towns, indulge in Italian cuisine, and soak up the Mediterranean sun.', '2024-06-20', '2024-06-30', 3900, 'italian_riviera.jpg'),
(8, 8, 'German Castle Tour: Dive into the fairy-tale world of Germany\'s castles. Explore historic fortresses, sample Bavarian beer, and enjoy scenic drives through the countryside.', '2024-10-15', '2024-10-25', 3400, 'german_castles.jpg'),
(9, 9, 'French Wine Country Retreat: Experience the charm of the French countryside. Visit vineyards in Bordeaux, savor French cuisine, and relax in picturesque villages.', '2024-09-05', '2024-09-15', 3700, 'french_wine_country.jpg'),
(10, 10, 'Canadian Wilderness Expedition: Explore the rugged beauty of Canada\'s wilderness. Go canoeing, spot wildlife, and camp in the pristine wilderness of the Canadian Rockies.', '2024-07-20', '2024-07-30', 4200, 'canadian_wilderness.jpg'),
(11, 2, 'Hawaii Beach Getaway: Relax on the beautiful beaches of Hawaii. Enjoy surfing, snorkeling, and luaus in this tropical paradise.', '2024-02-10', '2024-02-17', 2900, 'hawaii_beach_getaway.jpg'),
(18, 1, 'Trip across the streets of Haifa', '2023-02-11', '2023-02-25', 1000, 'haifa_trip.jpg'),
(19, 11, 'summer in amazing Philippines', '2024-02-11', '2024-02-25', 2000, 'summer_in_Philippines.jpg'),
(21, 3, 'Visit the Big Ben', '2024-06-01', '2024-08-31', 2000, 'big_ben_trip.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`country_id`);

--
-- Indexes for table `likes`
--
ALTER TABLE `likes`
  ADD PRIMARY KEY (`user_id`,`vacation_id`),
  ADD KEY `vacation_id` (`vacation_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `role_id` (`role_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `vacations`
--
ALTER TABLE `vacations`
  ADD PRIMARY KEY (`vacation_id`),
  ADD KEY `country_id` (`country_id`),
  ADD KEY `vacation_id` (`vacation_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `countries`
--
ALTER TABLE `countries`
  MODIFY `country_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `vacations`
--
ALTER TABLE `vacations`
  MODIFY `vacation_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `likes`
--
ALTER TABLE `likes`
  ADD CONSTRAINT `likes_ibfk_1` FOREIGN KEY (`vacation_id`) REFERENCES `vacations` (`vacation_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `likes_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`);

--
-- Constraints for table `vacations`
--
ALTER TABLE `vacations`
  ADD CONSTRAINT `vacations_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
