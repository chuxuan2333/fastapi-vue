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
      <el-table-column v-for="item in items" :key="item.item_id" :label="item.item_label">
        <template slot-scope="scope">{{ scope.row.cmdb_record_detail[item.item_name] }}</template>
      </el-table-column>
      <el-table-column label="操作" width="100" align="center">
        <template slot-scope="scope">
          <el-button type="primary" icon="el-icon-edit" circle @click="editDialog(scope.row)" />
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :title="title" :visible.sync="dialogVisible">
      <el-form :model="newInstance">
        <template v-for="item in items">
          <el-form-item :key="item.item_id" :label="item.item_label" :prop="item.item_name">
            <el-input v-model="newInstance[item.item_name]" autocomplete="off" />
          </el-form-item>
        </template>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitInstance">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { getInstance, addNewRecord, editOldRecord } from '@/api/cmdb'
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
      row = JSON.parse(JSON.stringify(row))
      this.dialogVisible = true
      this.title = '修改实例'
      this.addFlag = false
      const editInstance = Object.assign(row.cmdb_record_detail, { cmdb_type_id: this.typeID, cmdb_record_id: row.cmdb_record_id })
      this.newInstance = editInstance
    },
    addDialog() {
      this.dialogVisible = true
      this.title = '新增实例'
      this.newInstance = { cmdb_type_id: this.typeID }
      this.addFlag = true
    },
    addRecord() {
      addNewRecord(this.newInstance).then(response => {
        this.getAllInstance()
        this.dialogVisible = false
        this.$message({
          message: response.message,
          type: 'success'
        })
      })
    },
    editRecord() {
      editOldRecord(this.newInstance).then(response => {
        this.getAllInstance()
        this.dialogVisible = false
        this.$message({
          message: response.message,
          type: 'success'
        })
      })
    },
    submitInstance() {
      if (this.addFlag) {
        this.addRecord()
      } else {
        this.editRecord()
      }
    }
  }
}
</script>
