import request from '@/utils/request'

export function getPerms(params) {
  return request({
    url: '/perm/perm_lists',
    method: 'get',
    params: params
  })
}
export function addPerm(data) {
  return request({
    url: '/perm/add_perm',
    method: 'put',
    data: data
  })
}
export function editPerm(data) {
  return request({
    url: `/perm/edit_perm/${data.perm_id}`,
    method: 'post',
    data: data
  })
}
