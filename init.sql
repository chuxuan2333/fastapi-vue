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
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1348437874474881024, '修改权限', '/perm/edit_perm', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1349277847168094208, 'cmdb类型列表', '/cmdb/type_list', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1349277962737946624, '新增cmdb类型', '/cmdb/add_type', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1349278125342724096, '修改cmdb类型', '/cmdb/edit_type', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1350988831695966208, '获取类型所有的属性', '/cmdb/get_type_items', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1351015107055980544, 'cmdb type新增属性', '/cmdb/add_type_item', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1351047267733344256, 'cmdb type修改属性', '/cmdb/edit_type_item', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1351055889213296640, 'cmdb获取类型属性详情', '/cmdb/item_info', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1351068663289090048, '获取CMDB类型详情', '/cmdb/type_info', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1351092141601984512, '模型下实例列表', '/cmdb/instance_lists', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1351171013605462016, 'cmdb新增记录', '/cmdb/add_record', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1351171107306213376, 'cmdb修改记录', '/cmdb/edit_record', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1351344606725410816, 'cmdb删除记录', '/cmdb/delete_record', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1356504832885788672, '获取cmdb记录详情', '/cmdb/record_details', NOW(), NOW());
INSERT INTO `permission`(`perm_id`, `perm_name`, `perm_interface`, `creat_time`, `update_time`) VALUES (1356872129366331392, 'cmdb导入数据', '/cmdb/import_record', NOW(), NOW());

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
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1348438011699924992, 1346283931393200128, 1348437874474881024);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1349278168187539456, 1346283931393200128, 1349277847168094208);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1349278168216899584, 1346283931393200128, 1349277962737946624);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1349278168246259712, 1346283931393200128, 1349278125342724096);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1351016286783672320, 1346283931393200128, 1350988831695966208);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1351016286813032448, 1346283931393200128, 1351015107055980544);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1351047303007440896, 1346283931393200128, 1351047267733344256);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1351068698546409472, 1346283931393200128, 1351055889213296640);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1351068698575769600, 1346283931393200128, 1351068663289090048);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1351092183565996032, 1346283931393200128, 1351092141601984512);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1351171668248236032, 1346283931393200128, 1351171013605462016);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1351171668256624640, 1346283931393200128, 1351171107306213376);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1351344650434252800, 1346283931393200128, 1351344606725410816);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1356504870244454400, 1346283931393200128, 1356504832885788672);
INSERT INTO `role_perm`(`id`, `role_id`, `perm_id`) VALUES (1356872164191637504, 1346283931393200128, 1356872129366331392);

INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348170310200987648, '系统管理', 'system-manage', NOW(), NOW(), 0);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348170732772921344, '用户管理', 'user-manage', NOW(), NOW(), 1348170310200987648);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348223628373790720, '角色管理', 'role-manage', NOW(), NOW(), 1348170310200987648);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348224370950148096, '权限管理', 'perm-manage', NOW(), NOW(), 1348170310200987648);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348224662114537472, '菜单管理', 'menu-manage', NOW(), NOW(), 1348170310200987648);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348225668672000000, '操作记录', 'record-manage', NOW(), NOW(), 1348170310200987648);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348234823931662336, '新增用户', 'user-add', NOW(), NOW(), 1348170732772921344);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `creat_time`, `update_time`, `parent_id`) VALUES (1348235042819805184, '修改角色', 'role-edit', NOW(), NOW(), 1348223628373790720);
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `parent_id`, `creat_time`, `update_time`) VALUES (1349233447075450880, '资源管理', 'cmdb-manage', 0, NOW(), NOW());
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `parent_id`, `creat_time`, `update_time`) VALUES (1349233912022437888, '模型', 'cmdb-model', 1349233447075450880, NOW(), NOW());
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `parent_id`, `creat_time`, `update_time`) VALUES (1349347469275828224, '修改类型', 'cmdb-type-edit', 1349233447075450880, NOW(), NOW());
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `parent_id`, `creat_time`, `update_time`) VALUES (1350980086203027456, '实例', 'cmdb-instance', 1349233447075450880, NOW(), NOW());
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `parent_id`, `creat_time`, `update_time`) VALUES (1350982403165917184, '所有实例', 'cmdb-all-instance', 1349233447075450880, NOW(), NOW());
INSERT INTO `menu`(`menu_id`, `menu_name`, `menu_flag`, `parent_id`, `creat_time`, `update_time`) VALUES (1351891602716626944, '网页终端', 'cmdb-web-ssh', 1349233447075450880, NOW(), NOW());


INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514846101504, 1346283931393200128, 1348170310200987648);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514858684416, 1346283931393200128, 1348170732772921344);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514871267328, 1346283931393200128, 1348223628373790720);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514883850240, 1346283931393200128, 1348224662114537472);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514896433152, 1346283931393200128, 1348225668672000000);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514904821760, 1346283931393200128, 1348234823931662336);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514913210368, 1346283931393200128, 1348235042819805184);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1348256514925793280, 1346283931393200128, 1348224370950148096);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1349233969132081152, 1346283931393200128, 1349233447075450880);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1349233969161441280, 1346283931393200128, 1349233912022437888);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1349347506827431936, 1346283931393200128, 1349347469275828224);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1350980142771605504, 1346283931393200128, 1350980086203027456);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1350982443661922304, 1346283931393200128, 1350982403165917184);
INSERT INTO `role_menu`(`id`, `role_id`, `menu_id`) VALUES (1351891689106706432, 1346283931393200128, 1351891602716626944);


INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349282902902444032, 'mysql', 'cc-mysql', 'MySQL', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349283493586276352, 'kafka', 'cc-kafka', 'Kafka', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349284648261390336, 'rabbitmq', 'cc-rabbitmq', 'RabbitMQ', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349285013341999104, 'rocketmq', 'cc-rocketmq', 'RocketMQ', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349285318741856256, 'ups', 'cc-ups', 'UPS', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349286101822607360, 'kubernetes', 'cc-kubernetes', 'K8s', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349286546645323776, 'mongodb', 'cc-mongodb', 'MongoDB', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349287073940639744, 'oracle', 'cc-oracle', 'Oracle', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349287428598403072, 'redis', 'cc-redis', 'Redis', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349287493794664448, 'nginx', 'cc-nginx', 'Nginx', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349287571687084032, 'printer', 'cc-printer', '打印机', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349287747642331136, 'win-server', 'cc-win7', 'windows服务器', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349287994342903808, 'router', 'cc-router', '路由器', NOW(), NOW());
INSERT INTO `cmdb_type`(`cmdb_type_id`, `cmdb_type_name`, `cmdb_type_icon`, `cmdb_type_label`, `creat_time`, `update_time`) VALUES (1349534453021675520, 'linux', 'cc-linux', '主机', NOW(), NOW());


