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
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346300131607187456, '新增用户', '/users/create_user', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346361517599232000, '修改用户', '/users/update_user', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346370620681752576, '权限列表', '/perm/perm_lists', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346381317268443136, '获取用户信息', '/users/get_user_info', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346382793323712512, '用户列表', '/users/all_users', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346383796026609664, '操作记录列表', '/record/all_records', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346386299602472960, '角色列表', '/role/list', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346386539940286464, '新增角色', '/role/add_role', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346386666427912192, '角色成员修改', '/role/edit_users', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346386778659098624, '角色权限修改', '/role/edit_perms', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346386877837611008, '角色下所有成员', '/role/user_lists', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1346387063926296576, '角色下所有权限', '/role/perm_lists', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1348157449349238784, '菜单列表', '/menu/menu_lists', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1348169237436436480, '新增权限', '/perm/add_perm', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1348169977965973504, '新建菜单', '/menu/add_menu', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1348230996784451584, '修改菜单', '/menu/edit_menu', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1348231036550647808, '查询菜单', '/menu/get_menu_info', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1348244866995458048, '角色所有菜单', '/role/menu_lists', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1348246460768063488, '角色菜单修改', '/role/edit_menus', NOW(), NOW());


INSERT INTO `role`(`role_id`, `role_name`, `role_desc`, `creat_time`, `update_time`) VALUES (1346283931393200128, '管理员', '系统管理员', NOW(), NOW());
INSERT INTO `role_user`(`id`, `role_id`, `user_id`) VALUES (1346283973071998976, 1346283931393200128, 1334394783375953920);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490363072512, 1346283931393200128, 1346300131607187456);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490379849728, 1346283931393200128, 1346361517599232000);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490388238336, 1346283931393200128, 1346370620681752576);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490405015552, 1346283931393200128, 1346381317268443136);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490413404160, 1346283931393200128, 1346382793323712512);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490425987072, 1346283931393200128, 1346383796026609664);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490434375680, 1346283931393200128, 1346386299602472960);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490442764288, 1346283931393200128, 1346386539940286464);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490451152896, 1346283931393200128, 1346386666427912192);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490467930112, 1346283931393200128, 1346386778659098624);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490476318720, 1346283931393200128, 1346386877837611008);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490488901632, 1346283931393200128, 1346387063926296576);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490497290240, 1346283931393200128, 1348157449349238784);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490509873152, 1346283931393200128, 1348169237436436480);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490518261760, 1346283931393200128, 1348169977965973504);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490526650368, 1346283931393200128, 1348230996784451584);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490539233280, 1346283931393200128, 1348231036550647808);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490547621888, 1346283931393200128, 1348244866995458048);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348246490560204800, 1346283931393200128, 1348246460768063488);

INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348170310200987648, '系统管理', 'system-manage', NOW(), NOW(), 0);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348170732772921344, '用户管理', 'user-manage', NOW(), NOW(), 1348170310200987648);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348223628373790720, '角色管理', 'role-manage', NOW(), NOW(), 1348170310200987648);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348224370950148096, '权限管理', 'perm-manage', NOW(), NOW(), 1348170310200987648);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348224662114537472, '菜单管理', 'menu-manage', NOW(), NOW(), 1348170310200987648);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348225668672000000, '操作记录', 'record-manage', NOW(), NOW(), 1348170310200987648);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348234823931662336, '新增用户', 'user-add', NOW(), NOW(), 1348170732772921344);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348235042819805184, '修改角色', 'role-edit', NOW(), NOW(), 1348223628373790720);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514846101504, 1346283931393200128, 1348170310200987648);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514858684416, 1346283931393200128, 1348170732772921344);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514871267328, 1346283931393200128, 1348223628373790720);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514883850240, 1346283931393200128, 1348224662114537472);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514896433152, 1346283931393200128, 1348225668672000000);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514904821760, 1346283931393200128, 1348234823931662336);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514913210368, 1346283931393200128, 1348235042819805184);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514925793280, 1346283931393200128, 1348224370950148096);



