<template>
  <div class="app-container">
    <div>
      <el-button type="primary" @click="dialogVisible=true">新增模型</el-button>
    </div>
    <ul class="model-list clearfix">
      <li v-for="type in types" :key="type.type_name" class="model-item bgc-white">
        <div class="info-model" @click="typeEdit(type.type_id)">
          <div class="icon-box" align="center">
            <svg-icon :icon-class="type.type_icon" class-name="icon" />
          </div>
          <div class="model-details">
            <p class="model-name" :title="type.type_label">{{ type.type_label }}</p>
            <p class="model-id" :title="type.type_name">{{ type.type_name }}</p>
          </div>
        </div>
      </li>
    </ul>
    <el-dialog :visible.sync="dialogVisible" :title="dialogTitle">
      <el-form ref="typeForm" :model="newType" :rules="addRule">
        <el-form-item label="类型标识" prop="type_label">
          <el-input v-model="newType.type_label" autocomplete="off" />
        </el-form-item>
        <el-form-item label="类型名" prop="type_name">
          <el-input v-model="newType.type_name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="类型图标" prop="type_icon">
          <el-input v-model="newType.type_icon" autocomplete="off" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addType">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { getList, addType } from '@/api/cmdb'
export default {
  data() {
    return {
      types: [],
      dialogVisible: false,
      dialogTitle: '新增类型',
      newType: {
        type_label: null,
        type_name: null,
        type_icon: null
      },
      addRule: {
        type_label: [
          { required: true, message: '请输入类型标识', trigger: 'blur' },
          { min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur' }
        ],
        type_name: [
          { required: true, message: '请输入类型名', trigger: 'blur' },
          { min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur' }
        ],
        type_icon: [
          { required: true, message: '请输入类型图标', trigger: 'blur' },
          { min: 2, max: 20, message: '长度在 2 到 20 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  created() {
    this.getCMDBList()
  },
  methods: {
    getCMDBList() {
      getList().then(response => {
        this.types = response.types
      })
    },
    addType() {
      addType(this.newType).then(response => {
        this.dialogVisible = false
        this.getCMDBList()
        this.newType = {
          type_label: null,
          type_name: null,
          type_icon: null
        }
        this.$message({
          message: response.message,
          type: 'success'
        }
        )
      })
    },
    typeEdit(typeId) {
      this.$router.push(`/cmdb/edit_type/${typeId}`)
    }
  }
}
</script>

<style lang="scss" scoped>
.clearfix {
  zoom: 1;
  &:before,
  &:after {
      content: "";
      display: table;
      clear: both;
  }
}
.bgc-white {
    background-color: #fff;
}
.model-list {
    padding-left: 12px;
    overflow: hidden;
    transition: height .2s;
    .model-item {
        display: flex;
        position: relative;
        float: left;
        margin: 10px 10px 0 0;
        width: calc((100% - 10px * 4) / 5);
        height: 70px;
        border: 1px solid #dde4eb;
        border-radius: 4px;
        background-color: #ffffff;
        cursor: pointer;
        &:nth-child(5n) {
            margin-right: 0;
        }
        &.ispaused {
            background: #fcfdfe;
            border-color: #dde4eb;
            .icon-box {
                color: #96c2f7;
            }
            .model-name {
                color: #bfc7d2;
            }
        }
        &.ispre {
            .icon-box {
                color: #798aad;
            }
        }
        &:hover {
            border-color: #dde4eb;
            .info-instance {
                display: block;
            }
        }
        .icon-box {
            float: left;
            width: 66px;
            height: 68px;
            font-size: 32px;
            color: #2b2f3a;
            .icon {
                height: 68px;
            }
        }
        .model-details {
            padding: 0 4px 0 0;
            overflow: hidden;
        }
        .model-name {
            margin-top: 16px;
            line-height: 14px;
            font-size: 14px;
        }
        .model-id {
            line-height: 14px;
            font-size: 12px;
            color: #bfc7d2;
        }
        .info-model {
            flex: 1;
            width: 0;
            border-radius: 4px 0 0 4px;
            &:hover {
                background-color: #f0faff;
              p {
                        color: #3a84ff;
                    }
            }
            &.radius {
                border-radius: 4px;
            }
        }
        .info-instance {
            display: none;
            width: 70px;
            padding: 0 8px 0 6px;
            text-align: center;
            color: #c3cdd7;
            border-radius: 0 4px 4px 0;
            &:hover {
                background-color: #f0f5ff;
                p {
                    color: #3a84ff;
                }
            }
            p {
                font-size: 16px;
                padding-top: 2px;
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }
        }
    }
}
</style>
