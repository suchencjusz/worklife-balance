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
import { ref } from 'vue'

const chart = ref<HTMLElement | null>(null)
const API_URL = 'http://127.0.0.1:8080/api/activities/sum_visited_domains/1'

fetch(API_URL)
  .then((response) => response.json())
  .then((data) => {
    const charData = data.activities.map((activity: any) => {
      return {
        name: activity.name,
        value: Math.round(activity.value / 1000)
      }
    })

    console.log(charData)

    const option = {
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
          data: charData
        }
      ]
    }
    var myChart = echarts.init(chart.value!)
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
