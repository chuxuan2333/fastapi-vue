<template>
  <div class="app-container">
    <div id="xterm" class="xterm" />
  </div>
</template>
<script>
import 'xterm/css/xterm.css'
import { Terminal } from 'xterm'
import { FitAddon } from 'xterm-addon-fit'
import { AttachAddon } from 'xterm-addon-attach'

export default {
  name: 'Xterm',
  props: {
    socketURI: {
      type: String,
      default: 'ws://localhost:8999/api/cmdb/web_terminal'
    }
  },
  mounted() {
    this.initSocket()
  },
  beforeDestroy() {
    this.socket.close()
    this.term.dispose()
  },
  methods: {
    initTerm() {
      const term = new Terminal({
        rendererType: 'canvas', // 渲染类型
        convertEol: true, // 启用时，光标将设置为下一行的开头
        scrollback: 10, // 终端中的回滚量
        disableStdin: false, // 是否应禁用输入。
        cursorBlink: true, // 光标闪烁
        theme: {
          foreground: 'yellow', // 字体
          background: '#111111', // 背景色
          cursor: 'help' // 设置光标
        }
      })
      const attachAddon = new AttachAddon(this.socket)
      const fitAddon = new FitAddon()
      term.loadAddon(attachAddon)
      term.loadAddon(fitAddon)
      term.open(document.getElementById('xterm'))
      fitAddon.fit()
      term.focus()
      this.term = term
    },
    initSocket() {
      this.socket = new WebSocket(this.socketURI + '?username=root&password=root123&port=22&ip=10.34.9.123')
      this.socketOnClose()
      this.socketOnOpen()
      this.socketOnError()
    },
    socketOnOpen() {
      this.socket.onopen = () => {
        // 链接成功后
        this.initTerm()
      }
    },
    socketOnClose() {
      this.socket.onclose = () => {
        console.log('close socket')
      }
    },
    socketOnError() {
      this.socket.onerror = () => {
        // console.log('socket 链接失败')
      }
    }
  }
}
</script>
