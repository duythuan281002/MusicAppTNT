-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 18, 2024 lúc 09:07 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `appmusic`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `baihat`
--

CREATE TABLE `baihat` (
  `id` int(11) NOT NULL,
  `tenBH` varchar(100) NOT NULL,
  `loaiNhac` varchar(100) NOT NULL,
  `hinhAnh` varchar(100) NOT NULL,
  `linkBH` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `baihat`
--

INSERT INTO `baihat` (`id`, `tenBH`, `loaiNhac`, `hinhAnh`, `linkBH`) VALUES
(15, 'Bài ca tuổi trẻ', 'Rap', 'BaiCaTuoiTre.jpg', 'BaiCaTuoiTre-DaLABLinhCaoMelG-4452195.mp3'),
(16, 'Bạn tình ơi', 'Rap', 'BanTinhOi.jpg', 'BanTinhOi-YuniBooGoctoiMixer-6137656.mp3'),
(17, 'Chỉ một đêm nữa thôi', 'Rap', 'Chimotdemnuathoi.jpg', 'ChiMotDemNuaThoi.mp3'),
(18, 'Luôn yêu đời', 'Rap', 'luonyeudoi.jpg', 'LuonYeuDoi-Den-8692742.mp3'),
(19, 'Mình cưới nhau đi', 'Rap', 'minhcuoinhaudi.jpg', 'MinhCuoiNhauDi-HuynhJamesPjnboys-5382380.mp3'),
(22, 'Quăng tao cái boong', 'Rap', 'quangtaocaiboong.jpg', 'QuangTaoCaiBong.mp3'),
(23, 'Sao cũng được', 'Rap', 'saocungduoc.jpg', 'SaoCungDuocGuitarVersion-Binz-5411337.mp3'),
(24, 'Tối nay ta đi đâu nhờ', 'Rap', 'toinaytađiaunho.jpg', 'ToiNayTaDiDauNho.mp3'),
(25, 'Chạy ngay đi', 'Trẻ', 'chayngaydi.webp', 'ChayNgayDi-SonTungMTP-5468704.mp3'),
(26, 'Chúng ta không thuộc về nhau', 'Trẻ', 'chungtakhongthuocvenhau.jpg', 'ChungTaKhongThuocVeNhau-SonTungMTP-4528181.mp3'),
(27, 'Đợi đến tháng 13', 'Trẻ', 'doidenthang13.jpg', 'DoiDenThang13-VuThinh-14132282.mp3'),
(29, 'Hãy trao cho anh', 'Trẻ', 'haytraochoanh.jpg', 'HayTraoChoAnh-SonTungMTPSnoopDogg-6010660.mp3'),
(30, 'Hoa nở bên đường', 'Trẻ', 'hoanobenduong.jpg', 'HoaNoBenDuong-QuangDangTranACV-14190618.mp3'),
(36, 'Từng là', 'Trẻ', 'tungla.jpg', 'TungLa-VuCatTuong-13962415.mp3'),
(37, 'Thành phố mưa bay', 'Nhạc Xưa', 'thanhphomuabay.jpg', 'ThanhPhoMuaBay-DanNguyen_3zg8x.mp3'),
(38, 'Em về kẻo trời mưa', 'Nhạc Xưa', 'emvekeotroimua.jpg', 'EmVeKeoTroiMua-PhiNhung-2267264.mp3'),
(39, 'Nhật ký đời tôi', 'Nhạc Xưa', 'nhatkydoitoi.jpg', 'NhatKyDoiToi-GiangTien-2753840.mp3'),
(40, 'Nếu chúng mình cách trở', 'Nhạc Xưa', 'neuchungminhcachtro.jpg', 'NeuChungMinhCachTro-GiangTienMaiQuocHuy-2753844.mp3'),
(41, 'Đắp mộ cuộc tình', 'Nhạc Xưa', 'dapmocuoctinh.jpg', 'DapMoCuocTinh-HoVietTrung-4404818.mp3'),
(42, 'Sao em nỡ vô tình', 'Nhạc Xưa', 'saoemnovotinh.jpg', 'SaoEmNoVoTinh-HuynhNguyenCongBang-2644546.mp3'),
(43, 'Cát bụi cuộc đời', 'Nhạc Xưa', 'catbuicuocdoi.jpg', 'CatBuiCuocDoi-HuynhNguyenCongBang-3658039.mp3'),
(44, 'Go hard', 'Nước Ngoài', 'gohard.png', 'GoHard-TWICE-6759609.mp3'),
(45, 'Fancy', 'Nước Ngoài', 'fancy.png', 'Fancy-TWICE-5946557.mp3'),
(46, 'Dance thenightaway', 'Nước Ngoài', 'dance.webp', 'DanceTheNightAway-TWICE-5523060.mp3'),
(47, 'What is love', 'Nước Ngoài', 'islove.jpg', 'WhatIsLove-TWICE-5435161.mp3'),
(48, 'Moonlightsunrise', 'Nước Ngoài', 'mon1.jpg', 'MoonlightSunrise-TWICE-8572950.mp3');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `baihatyeuthich`
--

CREATE TABLE `baihatyeuthich` (
  `id_yeuthich` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_baihat` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `baihatyeuthich`
--

INSERT INTO `baihatyeuthich` (`id_yeuthich`, `id_user`, `id_baihat`) VALUES
(1, 1, 15),
(2, 1, 22),
(3, 1, 26),
(30, 11, 23),
(31, 11, 19),
(32, 8, 25),
(33, 8, 27),
(34, 8, 30),
(35, 8, 29),
(36, 13, 26),
(37, 13, 23),
(38, 13, 22),
(39, 13, 18),
(40, 13, 19),
(41, 8, 40),
(42, 8, 46),
(43, 8, 26);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, 'ndt2810', '123'),
(4, 'sgu1', '1'),
(5, 'sgu2', '22'),
(6, 'sgu3', '123'),
(8, '123', '123'),
(9, 'thu0711', '0711'),
(11, 'thu07111', '11'),
(12, 'thuan1', '33'),
(13, 'thun0306', '03'),
(14, 'nam01', '01'),
(15, '1234', '123');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `baihat`
--
ALTER TABLE `baihat`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `baihatyeuthich`
--
ALTER TABLE `baihatyeuthich`
  ADD PRIMARY KEY (`id_yeuthich`),
  ADD KEY `id_user_yt` (`id_user`),
  ADD KEY `id_baihat_yt` (`id_baihat`);

--
-- Chỉ mục cho bảng `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `baihat`
--
ALTER TABLE `baihat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT cho bảng `baihatyeuthich`
--
ALTER TABLE `baihatyeuthich`
  MODIFY `id_yeuthich` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT cho bảng `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `baihatyeuthich`
--
ALTER TABLE `baihatyeuthich`
  ADD CONSTRAINT `id_baihat_yt` FOREIGN KEY (`id_baihat`) REFERENCES `baihat` (`id`),
  ADD CONSTRAINT `id_user_yt` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
