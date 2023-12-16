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
          }
        }
      ],
      yAxis: [
        {
          type: 'value'
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
  background-color: #fff;
  border-radius: 1rem;
  border: 4px solid #c8c8c8;
}
</style>
