import request from '@/utils/request'
export function getRoles() {
  return request({
    url: '/role/list',
    method: 'get'
  })
}
export function roleAdd(data) {
  return request({
    url: '/role/add_role',
    method: 'put',
    data: data
  })
}
export function getUsers(data) {
  return request({
    url: '/role/user_lists',
    params: data
  })
}
export function getMenus(data) {
  return request({
    url: '/role/user_lists',
    params: data
  })
}
export function getPerms(data) {
  return request({
    url: '/role/perm_lists',
    params: data
  })
}
export function submitUsers(data) {
  return request({
    url: '/role/edit_users',
    method: 'post',
    data: data
  })
}
export function submitPerms(data) {
  return request({
    url: '/role/edit_perms',
    method: 'post',
    data: data
  })
}
