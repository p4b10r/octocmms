-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 05-11-2020 a las 20:33:15
-- Versión del servidor: 10.3.23-MariaDB-0+deb10u1
-- Versión de PHP: 7.3.19-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mydb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `correctivo`
--

CREATE TABLE `correctivo` (
  `id` int(11) NOT NULL,
  `tiempo` datetime NOT NULL DEFAULT current_timestamp(),
  `impresora` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Mantenimiento` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Sistema` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Falla` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Estado` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `correctivo`
--

INSERT INTO `correctivo` (`id`, `tiempo`, `impresora`, `Mantenimiento`, `Sistema`, `Falla`, `Estado`) VALUES
(149, '2020-11-03 23:29:24', 'X350', 'Correctivo', 'Termico', 'Calentador no llega a temperatura', 'En proceso'),
(150, '2020-11-03 23:37:55', 'X350', 'Correctivo', 'Termico', 'Calentador no llega a temperatura', 'Terminado'),
(151, '2020-11-03 23:48:50', 'X350', 'correctivo', 'extrusion', 'boquilla tapada ', 'En proceso'),
(155, '2020-11-03 23:57:30', 'X350', 'correctivo', 'extrusion', 'boquilla tapada ', 'Terminado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inspeccion_previa`
--

CREATE TABLE `inspeccion_previa` (
  `id` int(11) NOT NULL,
  `marca_temporal` datetime NOT NULL DEFAULT current_timestamp(),
  `inspeccion_diaria` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `inspeccion_previa`
--

INSERT INTO `inspeccion_previa` (`id`, `marca_temporal`, `inspeccion_diaria`) VALUES
(1, '2020-09-30 00:51:11', 'realizada'),
(2, '2020-09-30 00:51:18', 'realizada'),
(3, '2020-09-30 00:51:20', 'realizada'),
(4, '2020-09-30 00:51:56', 'realizada'),
(5, '2020-09-30 01:20:03', 'realizada'),
(6, '2020-10-19 23:27:37', 'Realizada'),
(7, '2020-10-19 23:32:46', 'Realizada'),
(8, '2020-10-21 01:00:16', 'Realizada'),
(9, '2020-11-02 22:24:42', 'Realizada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mtbf`
--

CREATE TABLE `mtbf` (
  `id` int(11) NOT NULL,
  `Mantenimiento` text NOT NULL,
  `Falla` text NOT NULL,
  `Inicio` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Termino` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `mtbf`
--

INSERT INTO `mtbf` (`id`, `Mantenimiento`, `Falla`, `Inicio`, `Termino`) VALUES
(1, '', '', '2020-09-27 04:23:09', NULL),
(2, 'sad', '', '2020-09-27 04:24:44', NULL),
(3, '', '', '2020-09-27 04:24:50', NULL),
(4, 'sadas', 'asdsad', '2020-09-27 04:26:10', NULL),
(5, '', '', '2020-09-27 04:26:11', NULL),
(6, 'asdsad', 'asdasd', '2020-09-27 04:31:30', NULL),
(7, 'asdas', 'asdas', '2020-09-27 04:32:14', NULL),
(8, 'asdas', 'dasdasd', '2020-09-27 04:35:43', NULL),
(9, 'dsadsad', 'asdasd', '2020-09-27 04:36:08', NULL),
(10, 'qewqeqe', 'dasdq', '2020-09-27 04:38:34', NULL),
(11, 'sadds', 'dasdasd', '2020-09-27 04:40:33', NULL),
(12, 'prueb', 'pr', '2020-09-27 05:15:54', NULL),
(13, 'dasdsa', 'dasdasd', '2020-09-27 05:29:48', NULL),
(14, 'asdasd', 'asdsad', '2020-09-27 05:30:04', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `terminadas`
--

CREATE TABLE `terminadas` (
  `id` int(11) NOT NULL,
  `pieza` text NOT NULL,
  `tiempo_impresion` int(11) NOT NULL,
  `filamento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `correctivo`
--
ALTER TABLE `correctivo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inspeccion_previa`
--
ALTER TABLE `inspeccion_previa`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `mtbf`
--
ALTER TABLE `mtbf`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `terminadas`
--
ALTER TABLE `terminadas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `correctivo`
--
ALTER TABLE `correctivo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=156;

--
-- AUTO_INCREMENT de la tabla `inspeccion_previa`
--
ALTER TABLE `inspeccion_previa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `mtbf`
--
ALTER TABLE `mtbf`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `terminadas`
--
ALTER TABLE `terminadas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
