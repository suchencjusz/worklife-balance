<template>
  <div class="container">
    <h2>Most popular</h2>
    <div class="pie-chart">
      <div ref="chart" class="chart-container"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as echarts from 'echarts'
import { ref, onMounted } from 'vue'

const chart = ref<HTMLElement | null>(null)

onMounted(() => {
  const myChart = echarts.init(chart.value)
  var option

  option = {
    tooltip: {
      trigger: 'item'
    },
    legend: {
      top: '5%',
      left: 'center'
    },
    series: [
      {
        name: 'Access From',
        type: 'pie',
        radius: ['40%', '70%'],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 10,
          borderColor: '#fff',
          borderWidth: 2
        },
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 40,
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
        data: [
          { value: 1048, name: 'Search Engine' },
          { value: 735, name: 'Direct' },
          { value: 580, name: 'Email' },
          { value: 484, name: 'Union Ads' },
          { value: 300, name: 'Video Ads' }
        ]
      }
    ]
  }
  option && myChart.setOption(option)
})
</script>

<style scoped>
.container {
  flex: 1;
  height: 100%;
  min-height: 40rem;
}

.chart-container {
  min-height: 40rem;
  width: 100%;
  background-color: #fff;
  border-radius: 1rem;
  border: 4px solid #c8c8c8;
}
</style>
