import request from '@/utils/request'

export function getList() {
  return request({
    url: '/cmdb/type_list',
    method: 'get'
  })
}
export function addType(data) {
  return request({
    url: '/cmdb/add_type',
    method: 'put',
    data: data
  })
}
export function editType(data) {
  return request({
    url: '/cmdb/edit_type',
    method: 'post',
    data: data
  })
}
