<template>
  <div class="app-container">
    <div>
      <el-button type="primary" @click="addDialog">新增菜单</el-button>
      <el-button type="primary" @click="editDialog">修改菜单</el-button>
    </div>
    <el-tree
      :data="menu_lists"
      show-checkbox
      default-expand-all
      node-key="menu_id"
      ref="tree"
      check-strictly
      highlight-current
      :props="defaultProps"
      @check-change="handleCheckChange"
    >
    </el-tree>
    <el-dialog :visible.sync="dialogVisible" :title="dialogTitle">
      <el-form ref="menuForm" :model="selectMenu" :rules="menuRule">
        <el-form-item label="父菜单" prop="parent_id">
          <treeselect
            v-model="selectMenu.parent_id"
            :options="menu_lists"
            :normalizer="normalizer"
            placeholder="请选择上级菜单,不选择即为根菜单"
          ></treeselect>
        </el-form-item>
        <el-form-item label="菜单名" prop="menu_name">
          <el-input v-model="selectMenu.menu_name"></el-input>
        </el-form-item>
        <el-form-item label="前端标识" prop="menu_flag">
          <el-input v-model="selectMenu.menu_flag"></el-input>
        </el-form-item>
        <el-form-item align="right">
          <el-button @click="resetForm('menuForm')">取 消</el-button>
          <el-button type="primary" @click="addMenu('menuForm')">确 定</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import { getMenuLists, addMenu, editMenu, getMenuInfo } from '@/api/menu'
import Treeselect from '@riophae/vue-treeselect'
// import the styles
import '@riophae/vue-treeselect/dist/vue-treeselect.css'
export default {
  components: { Treeselect },
  data() {
    return {
      menu_lists: [],
      defaultProps: {
        children: 'children',
        label: 'menu_name'
      },
      dialogVisible: false,
      selectMenu: {
        parent_id: null,
        menu_name: '',
        menu_flag: ''
      },
      checkedId: '',
      dialogTitle: '新增菜单',
      editFlag: false,
      menuRule: {
        menu_name: [
          { required: true, message: '请输入菜单名', trigger: 'blur' },
          { min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur' }
        ],
        menu_flag: [
          { required: true, message: '请输入前端标识', trigger: 'blur' },
          { min: 4, max: 20, message: '长度在 4 到 20 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  created() {
    this.showMenus()
  },
  methods: {
    normalizer(node) {
      return {
        id: node.menu_id,
        label: node.menu_name
      }
    },
    showMenus() {
      getMenuLists().then(response => {
        this.menu_lists = response.menus
      })
    },
    handleCheckChange(data, checked, node) {
      if (checked) {
        this.checkedId = data.menu_id
        this.$refs.tree.setCheckedKeys([data.menu_id])
      }
    },
    addMenu(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          if (this.editFlag) {
            editMenu(this.selectMenu).then(response => {
              this.$message({
                message: response.message,
                type: 'success'
              })
              this.dialogVisible = false
              this.showMenus()
            })
          } else {
            addMenu(this.selectMenu).then(response => {
              this.$message({
                message: response.message,
                type: 'success'
              })
              this.dialogVisible = false
              this.showMenus()
            })
          }
        } else {
          return false
        }
      })
    },
    resetForm(formName) {
      this.dialogVisible = false
      this.$refs[formName].resetFields()
      this.checkedId = ''
    },
    addDialog() {
      this.dialogVisible = true
      this.editFlag = false
      this.selectMenu = {
        parent_id: null,
        menu_name: '',
        menu_flag: ''
      }
    },
    editDialog() {
      if (!this.checkedId) {
        this.$alert('请选择要修改的菜单', '选择菜单', {
          confirmButtonText: '确定'
        })
      } else {
        this.dialogTitle = '修改菜单'
        this.dialogVisible = true
        this.editFlag = true
        const params = { 'menu_id': this.checkedId }
        getMenuInfo(params).then(response => {
          this.selectMenu = {
            menu_id: response.menu_id,
            parent_id: response.parent_id,
            menu_name: response.menu_name,
            menu_flag: response.menu_flag
          }
        })

      }
    }
  }
}

</script>
