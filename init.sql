INSERT INTO users ( `user_id`, `username`, `nick_name`, `email`, `hashed_password`, `is_active`, `creat_time` )
VALUES
	(
		1334394783375953920,
		'admin',
		'超级管理员',
		'admin@xxx.com',
		'$2b$12$7oOsvkOPSoDz/ipaIXWP0.1lWUhvAYe1ZhIKfmd5MNiVUFD9JRrnu',
	1,
	NOW());
INSERT INTO `permission` VALUES (1346300131607187456, '新增用户', '/users/create_user', NOW(), NOW());
INSERT INTO `permission` VALUES (1346361517599232000, '修改用户', '/users/update_user', NOW(), NOW());
INSERT INTO `permission` VALUES (1346370620681752576, '权限列表', '/perm/perm_lists', NOW(), NOW());
INSERT INTO `permission` VALUES (1346381317268443136, '获取用户信息', '/users/get_user_info', NOW(), NOW());
INSERT INTO `permission` VALUES (1346382793323712512, '用户列表', '/users/all_users', NOW(), NOW());
INSERT INTO `permission` VALUES (1346383796026609664, '操作记录列表', '/record/all_records', NOW(), NOW());
INSERT INTO `permission` VALUES (1346386299602472960, '角色列表', '/role/list', NOW(), NOW());
INSERT INTO `permission` VALUES (1346386539940286464, '新增角色', '/role/add_role', NOW(), NOW());
INSERT INTO `permission` VALUES (1346386666427912192, '角色成员修改', '/role/edit_users', NOW(), NOW());
INSERT INTO `permission` VALUES (1346386778659098624, '角色权限修改', '/role/edit_perms', NOW(), NOW());
INSERT INTO `permission` VALUES (1346386877837611008, '角色下所有成员', '/role/user_lists', NOW(), NOW());
INSERT INTO `permission` VALUES (1346387063926296576, '角色下所有权限', '/role/perm_lists', NOW(), NOW());
INSERT INTO `fast`.`role`(`role_id`, `role_name`, `role_desc`, `creat_time`, `update_time`) VALUES (1346283931393200128, '管理员', '系统管理员', NOW(), NOW());
INSERT INTO `fast`.`role_user`(`id`, `role_id`, `user_id`) VALUES (1346283973071998976, 1346283931393200128, 1334394783375953920);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149483474944, 1346283931393200128, 1346300131607187456);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149525417984, 1346283931393200128, 1346361517599232000);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149554778112, 1346283931393200128, 1346370620681752576);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149592526848, 1346283931393200128, 1346381317268443136);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149621886976, 1346283931393200128, 1346382793323712512);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149655441408, 1346283931393200128, 1346383796026609664);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149693190144, 1346283931393200128, 1346386299602472960);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149730938880, 1346283931393200128, 1346386539940286464);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149768687616, 1346283931393200128, 1346386666427912192);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149802242048, 1346283931393200128, 1346386778659098624);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149831602176, 1346283931393200128, 1346386877837611008);
INSERT INTO `fast`.`role_perm`(`id`, `role_id`, `perm_id`) VALUES (1346388149860962304, 1346283931393200128, 1346387063926296576);

