<template>
  <div>
    <h1>Time per day</h1>
    <div ref="chart" class="chart-container"></div>
  </div>
</template>

<script setup lang="ts">
import * as echarts from 'echarts'
import { ref, onMounted } from 'vue'

const chart = ref<HTMLElement | null>(null)

onMounted(() => {
  var myChart = echarts.init(chart.value)
  var option

  option = {
    xAxis: {
      type: 'category',
      data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
      type: 'value'
    },
    legend: {
      data: ['Learning', 'Entertaiment', 'Other']
    },
    tooltip: {
      trigger: 'axis'
    },
    series: [
      {
        name: 'Learning',
        data: [820, 932, 901, 934, 1290, 1330, 1320],
        type: 'line',
        smooth: true
      },
      {
        name: 'Entertaiment',
        data: [153, 1232, 11, 234, 190, 130, 1320],
        type: 'line',
        smooth: true
      },
      {
        name: 'Other',
        data: [123, 123, 123, 123, 123, 123, 123],
        type: 'line',
        smooth: true
      }
    ]
  }

  option && myChart.setOption(option)
})
</script>

<style scoped>
.chart-container {
  height: 500px;
  background-color: #fff;
  border-radius: 1rem;
  border: 4px solid #c8c8c8;
}
</style>
