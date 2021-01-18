<template>
  <div class="app-container">
    <div>
      <el-button type="primary" @click="addDialog">新增实例</el-button>
    </div>
    <el-table
      v-loading="listLoading"
      element-loading-text="拼命加载中"
      element-loading-spinner="el-icon-loading"
      :data="instances"
      border
      highlight-current-row
    >
      <el-table-column v-for="item in items" :key="item.item_id" :label="item.item_label" :property="item.item_name" />
      <el-table-column label="操作" width="100" align="center">
        <template slot-scope="scope">
          <el-button type="primary" icon="el-icon-edit" circle @click="editDialog(scope.row)" />
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :title="title" :visible.sync="dialogVisible">
      <el-form :model="newInstance">
        <el-form-item v-for="item in items" :key="item.item_id" :label="item.item_label" :prop="item.item_name">
          <el-input v-model="newInstance[item.item_name]" autocomplete="off" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitInstance">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { getInstance } from '@/api/cmdb'
export default {
  data() {
    return {
      listLoading: true,
      dialogVisible: false,
      title: '新增实例',
      instances: [],
      items: [],
      typeID: this.$route.params.id,
      newInstance: { cmdb_type_id: this.$route.params.id },
      addFlag: true
    }
  },
  created() {
    this.getAllInstance()
  },
  methods: {
    getAllInstance() {
      getInstance({ 'type_id': this.typeID }).then(response => {
        this.instances = response.instances
        this.items = response.items
      })
      this.listLoading = false
    },
    editDialog(row) {
      this.dialogVisible = true
      this.title = '修改实例'
      this.addFlag = false
      console.log(row)
    },
    addDialog() {
      this.dialogVisible = true
      this.title = '新增实例'
      this.newInstance = { cmdb_type_id: this.typeID }
      this.addFlag = true
    },
    submitInstance() {
      console.log(this.newInstance)
    }
  }
}
</script>
