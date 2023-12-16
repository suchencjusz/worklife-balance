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
    const charData = data.activities.slice(0, 7).map((item: any) => {
      return {
        name: item.name,
        value: item.value
      }
    })

    console.log(charData)

    const option = {
      tooltip: {
        trigger: 'item'
        // valueFormatter: (value: number) => Math.round(value / 1000 / 36) / 100 + 'h'
      },
      itemStyle: {
        borderColor: '#fff',
        borderWidth: 1
      },
      legend: {
        top: '5%',
        left: 'center',
        textStyle: {
          color: '#000'
        }
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
  /* From https://css.glass */
  background: rgba(255, 255, 255, 0.49);
  border-radius: 16px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(8.7px);
  -webkit-backdrop-filter: blur(8.7px);
  border: 1px solid rgba(255, 255, 255, 1);
}
</style>
