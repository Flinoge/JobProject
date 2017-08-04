<template>
  <div class="ideaWeb">
    <canvas id="ideaWeb"></canvas>
  </div>
</template>

<script>
import fabric from 'fabric'
import axios from 'axios'

export default {
  data () {
    return {
    }
  },
  computed: {
  },
  methods: {
    handleResize () {
//      let scale = window.innerHeight / this.ideaWeb.height
      this.ideaWeb.setWidth(window.innerWidth)
      this.ideaWeb.setHeight(window.innerHeight)
//      for (let i = 0; i < this.nodes.length; i++) {
//        this.nodes[i].scaleX = scale
//        this.nodes[i].scaleY = scale
//      }
//      console.log(this.nodes[0])
    }
  },
  mounted () {
    axios({
      method: 'get',
      url: 'http://localhost:8000/ideas'
    }).then(response => {
      console.log(response)
    }).catch(error => {
      console.log(error)
    })
    window.addEventListener('resize', this.handleResize)
    this.ideaWeb = new fabric.fabric.Canvas('ideaWeb')
    this.ideaWeb.selection = false
    this.ideaWeb.setWidth(window.innerWidth)
    this.ideaWeb.setHeight(window.innerHeight)
    this.nodes = new Array(10)
    for (let i = 0; i < this.nodes.length; i++) {
      this.nodes[i] = new fabric.fabric.Circle({
        left: 0,
        top: 0,
        radius: window.innerHeight / 15
      })
      this.ideaWeb.add(this.nodes[i])
    }
//    console.log(this.nodes[0])
  }
}
</script>

<style>
  body {
    width: 100%;
    height: 100%;
  }
  .ideaWeb {
    height: 100%;
    width: 100%;
  }
  #ideaWeb {
    height: 100%;
    width: 100%;
  }
  .canvas-container {
    height: 100% !important;
    width: 100% !important;
  }
</style>
