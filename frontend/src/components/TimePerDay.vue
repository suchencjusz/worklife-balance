<template>
  <div>
    <h2>Time per day</h2>
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
      data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      axisLine: {
        lineStyle: {
          color: '#000'
        }
      }
    },
    yAxis: {
      type: 'value',
      name: 'Hours',
      splitLine: {
        lineStyle: {
          color: '#bbb'
        }
      },
      nameTextStyle: {
        color: '#000',
        fontSize: 16
      },
      axisLabel: {
        formatter: '{value}h'
      },
      axisLine: {
        lineStyle: {
          color: '#000'
        }
      }
    },
    legend: {
      textStyle: {
        color: '#000',
        fontSize: 16
      },
      data: ['Learning', 'Entertaiment', 'Other']
    },
    tooltip: {
      trigger: 'axis',
      valueFormatter: (value: string) => value + 'h'
    },
    series: [
      {
        name: 'Learning',
        data: [1, 2, 1.5, 1.3, 5.3, 1.1, 1.8],
        type: 'line',
        smooth: true
      },
      {
        name: 'Entertaiment',
        data: [3.4, 5.3, 1.1, 1.4, 0, 1.1, 4.1],
        type: 'line',
        smooth: true
      },
      {
        name: 'Other',
        data: [0.3, 0.2, 0.1, 0.5, 1.1, 1.5, 1.2],
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
  padding: 1rem;
  background: rgba(255, 255, 255, 0.49);
  border-radius: 16px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(8.7px);
  -webkit-backdrop-filter: blur(8.7px);
  border: 1px solid rgba(255, 255, 255, 1);
}
</style>
