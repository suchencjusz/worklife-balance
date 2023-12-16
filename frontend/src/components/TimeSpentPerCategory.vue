<template>
  <div class="container">
    <h2>Time spent per category</h2>
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
          { value: 1048, name: 'Entertaiment' },
          { value: 735, name: 'Learning' },
          { value: 580, name: 'Other' }
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
  /* From https://css.glass */
  background: rgba(255, 255, 255, 0.49);
  border-radius: 16px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(8.7px);
  -webkit-backdrop-filter: blur(8.7px);
  border: 1px solid rgba(255, 255, 255, 1);
}
</style>
