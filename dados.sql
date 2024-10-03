-- Usar o banco de dados
USE banco_de_dados;

-- Inserir três registros de usuários
INSERT INTO usuarios (uid, gid, grupos) VALUES 
(1001, 1001, '1001(maria),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),135(lxd),136(sambashare),999(docker)'),
(1002, 1002, '1002(joao),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),135(lxd),136(sambashare),999(docker)'),
(1003, 1003, '1003(ana),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),135(lxd),136(sambashare),999(docker)');
