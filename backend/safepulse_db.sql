-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 30, 2026 at 11:58 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `safepulse_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_profile`
--

CREATE TABLE `accounts_profile` (
  `id` bigint(20) NOT NULL,
  `role` varchar(10) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `address` longtext NOT NULL,
  `emergency_contact` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounts_profile`
--

INSERT INTO `accounts_profile` (`id`, `role`, `full_name`, `phone`, `dob`, `gender`, `address`, `emergency_contact`, `created_at`, `user_id`) VALUES
(5, 'admin', 'SafePulse Admin System', '', '', '', '', '', '2026-03-26 07:44:13.923627', 6),
(7, 'user', 'user', '', '', '', '', '', '2026-03-26 10:13:45.107306', 8);

-- --------------------------------------------------------

--
-- Table structure for table `assessments_healthassessment`
--

CREATE TABLE `assessments_healthassessment` (
  `id` bigint(20) NOT NULL,
  `assessment_type` varchar(20) NOT NULL,
  `inputs` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`inputs`)),
  `results` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`results`)),
  `score` int(11) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `assessments_healthassessment`
--

INSERT INTO `assessments_healthassessment` (`id`, `assessment_type`, `inputs`, `results`, `score`, `timestamp`, `user_id`) VALUES
(15, 'brain', '{\"mmse\": 30, \"age\": 70, \"clinical\": \"MCI\", \"family_history\": true}', '{\"riskLevel\": \"Mild Risk\", \"score\": 100, \"points\": 35}', 100, '2026-03-26 10:15:10.185019', 8),
(16, 'kidney', '{\"gfr\": 90, \"creatinine\": 1.2, \"protein_present\": true, \"urea\": 30}', '{\"riskLevel\": \"Medium\", \"score\": 70, \"stage\": \"Stage 1 \\u2022 Normal\"}', 70, '2026-03-26 10:18:51.090890', 8),
(17, 'lung', '{\"is_smoker\": true, \"fev1\": 90, \"spo2\": 100, \"ratio\": 1, \"status\": \"Mild\"}', '{\"riskLevel\": \"LOW-MEDIUM\", \"status\": \"Mild\", \"score\": 75}', 75, '2026-03-26 10:19:09.349405', 8),
(18, 'cancer', '{\"metastasis\": true, \"tumor_size\": \"T2\", \"biopsy_grade\": \"Intermediate\", \"lymph_node\": true}', '{\"stage\": \"Stage IV\", \"riskLevel\": \"Very High\", \"score\": 20}', 20, '2026-03-26 10:20:23.103517', 8),
(19, 'liver', '{\"ast\": 90, \"alp\": 80, \"albumin\": 5, \"alt\": 80, \"bilirubin\": 2, \"status\": \"Mild\"}', '{\"riskLevel\": \"Moderate Risk\", \"status\": \"Mild\", \"score\": 75}', 75, '2026-03-26 10:28:06.420619', 8),
(20, 'heart', '{\"systolic\": 130, \"diastolic\": 90, \"ldl\": 150, \"cholesterol\": 200, \"abnormal_ecg\": true, \"sugar\": 150}', '{\"riskLevel\": \"High Risk\", \"riskPercentage\": \"35%\", \"score\": 65}', 65, '2026-03-26 10:28:36.991953', 8),
(21, 'kidney', '{\"gfr\": 90, \"creatinine\": 1.2, \"protein_present\": true, \"urea\": 20}', '{\"riskLevel\": \"Medium\", \"score\": 70, \"stage\": \"Stage 1 \\u2022 Normal\"}', 70, '2026-03-27 07:49:57.784545', 8),
(22, 'heart', '{\"systolic\": 130, \"diastolic\": 90, \"ldl\": 140, \"cholesterol\": 300, \"abnormal_ecg\": true, \"sugar\": 100}', '{\"riskLevel\": \"High Risk\", \"riskPercentage\": \"35%\", \"score\": 65}', 65, '2026-03-27 07:50:09.506576', 8),
(23, 'lung', '{\"is_smoker\": true, \"fev1\": 90, \"spo2\": 100, \"ratio\": 1, \"status\": \"Mild\"}', '{\"riskLevel\": \"LOW-MEDIUM\", \"status\": \"Mild\", \"score\": 75}', 75, '2026-03-27 07:50:21.624395', 8),
(24, 'cancer', '{\"metastasis\": true, \"tumor_size\": \"T2\", \"biopsy_grade\": \"Intermediate\", \"lymph_node\": true}', '{\"stage\": \"Stage IV\", \"riskLevel\": \"Very High\", \"score\": 20}', 20, '2026-03-27 07:50:36.780780', 8),
(25, 'brain', '{\"mmse\": 12, \"family_history\": true, \"clinical\": \"MCI\", \"age\": 70}', '{\"riskLevel\": \"Moderate Risk\", \"score\": 40, \"points\": 70}', 40, '2026-03-27 07:50:47.103029', 8);

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('a3bb1cd0b5432257b7d964512d10942e12012d2b', '2026-03-26 10:13:45.124446', 8),
('admin12', '2026-03-26 07:44:17.095142', 6);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 3, 'add_permission'),
(6, 'Can change permission', 3, 'change_permission'),
(7, 'Can delete permission', 3, 'delete_permission'),
(8, 'Can view permission', 3, 'view_permission'),
(9, 'Can add group', 2, 'add_group'),
(10, 'Can change group', 2, 'change_group'),
(11, 'Can delete group', 2, 'delete_group'),
(12, 'Can view group', 2, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add profile', 7, 'add_profile'),
(26, 'Can change profile', 7, 'change_profile'),
(27, 'Can delete profile', 7, 'delete_profile'),
(28, 'Can view profile', 7, 'view_profile'),
(29, 'Can add health assessment', 8, 'add_healthassessment'),
(30, 'Can change health assessment', 8, 'change_healthassessment'),
(31, 'Can delete health assessment', 8, 'delete_healthassessment'),
(32, 'Can view health assessment', 8, 'view_healthassessment'),
(33, 'Can add daily log', 9, 'add_dailylog'),
(34, 'Can change daily log', 9, 'change_dailylog'),
(35, 'Can delete daily log', 9, 'delete_dailylog'),
(36, 'Can view daily log', 9, 'view_dailylog'),
(37, 'Can add patient', 11, 'add_patient'),
(38, 'Can change patient', 11, 'change_patient'),
(39, 'Can delete patient', 11, 'delete_patient'),
(40, 'Can view patient', 11, 'view_patient'),
(41, 'Can add clinical data', 10, 'add_clinicaldata'),
(42, 'Can change clinical data', 10, 'change_clinicaldata'),
(43, 'Can delete clinical data', 10, 'delete_clinicaldata'),
(44, 'Can view clinical data', 10, 'view_clinicaldata'),
(45, 'Can add Token', 12, 'add_token'),
(46, 'Can change Token', 12, 'change_token'),
(47, 'Can delete Token', 12, 'delete_token'),
(48, 'Can view Token', 12, 'view_token'),
(49, 'Can add Token', 13, 'add_tokenproxy'),
(50, 'Can change Token', 13, 'change_tokenproxy'),
(51, 'Can delete Token', 13, 'delete_tokenproxy'),
(52, 'Can view Token', 13, 'view_tokenproxy');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(6, 'pbkdf2_sha256$1200000$Ogh8KSvYavslep4Pb1TJme$0bnnUkHL0sOJXaiReB1b3lRNCOHNNx8s+N8rQRgWCnE=', NULL, 0, 'admin@safepulse.com', '', '', 'admin@safepulse.com', 1, 1, '2026-03-26 07:44:11.047425'),
(8, 'pbkdf2_sha256$1200000$YVlrcIc78TLTH2NF7qUR2D$wPJGoZ6qNeKfkww/I9IRY101UwuIJUVtHIputSkatDc=', NULL, 0, 'user@gmail.com', '', '', 'user@gmail.com', 0, 1, '2026-03-26 10:13:42.346903');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'profile'),
(1, 'admin', 'logentry'),
(8, 'assessments', 'healthassessment'),
(2, 'auth', 'group'),
(3, 'auth', 'permission'),
(4, 'auth', 'user'),
(12, 'authtoken', 'token'),
(13, 'authtoken', 'tokenproxy'),
(5, 'contenttypes', 'contenttype'),
(10, 'reports', 'clinicaldata'),
(11, 'reports', 'patient'),
(6, 'sessions', 'session'),
(9, 'tracker', 'dailylog');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-03-22 13:21:59.729684'),
(2, 'auth', '0001_initial', '2026-03-22 13:22:00.048614'),
(3, 'accounts', '0001_initial', '2026-03-22 13:22:00.120892'),
(4, 'admin', '0001_initial', '2026-03-22 13:22:00.209806'),
(5, 'admin', '0002_logentry_remove_auto_add', '2026-03-22 13:22:00.215484'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2026-03-22 13:22:00.223458'),
(7, 'assessments', '0001_initial', '2026-03-22 13:22:00.269217'),
(8, 'contenttypes', '0002_remove_content_type_name', '2026-03-22 13:22:00.313061'),
(9, 'auth', '0002_alter_permission_name_max_length', '2026-03-22 13:22:00.355369'),
(10, 'auth', '0003_alter_user_email_max_length', '2026-03-22 13:22:00.366387'),
(11, 'auth', '0004_alter_user_username_opts', '2026-03-22 13:22:00.374182'),
(12, 'auth', '0005_alter_user_last_login_null', '2026-03-22 13:22:00.419759'),
(13, 'auth', '0006_require_contenttypes_0002', '2026-03-22 13:22:00.421871'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2026-03-22 13:22:00.429060'),
(15, 'auth', '0008_alter_user_username_max_length', '2026-03-22 13:22:00.440808'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2026-03-22 13:22:00.452729'),
(17, 'auth', '0010_alter_group_name_max_length', '2026-03-22 13:22:00.462945'),
(18, 'auth', '0011_update_proxy_permissions', '2026-03-22 13:22:00.470019'),
(19, 'auth', '0012_alter_user_first_name_max_length', '2026-03-22 13:22:00.479583'),
(20, 'authtoken', '0001_initial', '2026-03-22 13:22:00.532057'),
(21, 'authtoken', '0002_auto_20160226_1747', '2026-03-22 13:22:00.555460'),
(22, 'authtoken', '0003_tokenproxy', '2026-03-22 13:22:00.557865'),
(23, 'authtoken', '0004_alter_tokenproxy_options', '2026-03-22 13:22:00.561443'),
(24, 'reports', '0001_initial', '2026-03-22 13:22:00.663829'),
(25, 'sessions', '0001_initial', '2026-03-22 13:22:00.686944'),
(26, 'tracker', '0001_initial', '2026-03-22 13:22:00.761605'),
(27, 'tracker', '0002_dailylog_diastolic_dailylog_systolic_dailylog_weight', '2026-03-23 17:55:00.512603');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reports_clinicaldata`
--

CREATE TABLE `reports_clinicaldata` (
  `id` bigint(20) NOT NULL,
  `weight` double DEFAULT NULL,
  `height` double DEFAULT NULL,
  `bmi` double DEFAULT NULL,
  `blood_pressure_sys` int(11) DEFAULT NULL,
  `blood_pressure_dia` int(11) DEFAULT NULL,
  `heart_rate` int(11) DEFAULT NULL,
  `temperature` double DEFAULT NULL,
  `respiratory_rate` int(11) DEFAULT NULL,
  `spo2` int(11) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `patient_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reports_patient`
--

CREATE TABLE `reports_patient` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(20) NOT NULL,
  `blood_group` varchar(10) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `address` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tracker_dailylog`
--

CREATE TABLE `tracker_dailylog` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `water` double NOT NULL,
  `smoked` tinyint(1) NOT NULL,
  `steps` int(11) NOT NULL,
  `sleep` double NOT NULL,
  `calories` int(11) NOT NULL,
  `score` int(11) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  `diastolic` int(11) NOT NULL,
  `systolic` int(11) NOT NULL,
  `weight` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tracker_dailylog`
--

INSERT INTO `tracker_dailylog` (`id`, `date`, `water`, `smoked`, `steps`, `sleep`, `calories`, `score`, `timestamp`, `user_id`, `diastolic`, `systolic`, `weight`) VALUES
(5, '2026-03-26', 1, 1, 1000, 8.5, 1000, 40, '2026-03-26 10:16:24.393087', 8, 80, 120, 30),
(6, '2026-03-27', 2, 1, 1000, 8.5, 2000, 40, '2026-03-27 06:28:01.048918', 8, 90, 130, 90);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `assessments_healthassessment`
--
ALTER TABLE `assessments_healthassessment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `assessments_healthassessment_user_id_b4b529f8_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `reports_clinicaldata`
--
ALTER TABLE `reports_clinicaldata`
  ADD PRIMARY KEY (`id`),
  ADD KEY `reports_clinicaldata_patient_id_b88fc7ac_fk_reports_patient_id` (`patient_id`);

--
-- Indexes for table `reports_patient`
--
ALTER TABLE `reports_patient`
  ADD PRIMARY KEY (`id`),
  ADD KEY `reports_patient_user_id_d8374d9a_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `tracker_dailylog`
--
ALTER TABLE `tracker_dailylog`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tracker_dailylog_user_id_date_7e3b10b9_uniq` (`user_id`,`date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `assessments_healthassessment`
--
ALTER TABLE `assessments_healthassessment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `reports_clinicaldata`
--
ALTER TABLE `reports_clinicaldata`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `reports_patient`
--
ALTER TABLE `reports_patient`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tracker_dailylog`
--
ALTER TABLE `tracker_dailylog`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD CONSTRAINT `accounts_profile_user_id_49a85d32_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `assessments_healthassessment`
--
ALTER TABLE `assessments_healthassessment`
  ADD CONSTRAINT `assessments_healthassessment_user_id_b4b529f8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `reports_clinicaldata`
--
ALTER TABLE `reports_clinicaldata`
  ADD CONSTRAINT `reports_clinicaldata_patient_id_b88fc7ac_fk_reports_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `reports_patient` (`id`);

--
-- Constraints for table `reports_patient`
--
ALTER TABLE `reports_patient`
  ADD CONSTRAINT `reports_patient_user_id_d8374d9a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tracker_dailylog`
--
ALTER TABLE `tracker_dailylog`
  ADD CONSTRAINT `tracker_dailylog_user_id_3d78e588_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
