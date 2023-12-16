<template>
  <div class="container">
    <h2>Times visited</h2>
    <div class="pie-chart">
      <div ref="chart" class="chart-container"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as echarts from 'echarts'
import { ref, onMounted } from 'vue'

const API_URL = 'http://127.0.0.1:8080/api/activities/most_visited_domains/1'

const chart = ref<HTMLElement | null>(null)

fetch(API_URL)
  .then((response) => response.json())
  .then((data) => {
    const charData = data.activities.map((activity: any) => {
      return {
        name: activity.name,
        value: activity.value
      }
    })

    charData.sort((a: any, b: any) => b.value - a.value)

    const option = {
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        }
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
      },
      xAxis: [
        {
          type: 'category',
          data: charData.map((activity: any) => activity.name),
          axisTick: {
            alignWithLabel: true
          },
          textStyle: {
            color: '#000'
          }
        }
      ],
      yAxis: [
        {
          type: 'value',
          textStyle: {
            color: '#000',
            fontSize: 16
          }
        }
      ],
      series: [
        {
          name: 'Direct',
          type: 'bar',
          barWidth: '60%',
          data: charData.map((activity: any) => activity.value)
        }
      ]
    }

    const myChart = echarts.init(chart.value!)
    myChart.setOption(option)
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
