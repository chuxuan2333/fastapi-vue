import request from '@/utils/request'

export function getMenuLists() {
  return request({
    url: '/menu/menu_lists',
    method: 'get'
  })
}

export function addMenu(data) {
  return request({
    url: '/menu/add_menu',
    method: 'put',
    data: data
  })
}

export function editMenu(data) {
  return request({
    url: '/menu/edit_menu',
    method: 'post',
    data: data
  })
}
export function getMenuInfo(menu_id) {
  return request({
    url: '/menu/get_menu_info',
    params: menu_id
  })
}
