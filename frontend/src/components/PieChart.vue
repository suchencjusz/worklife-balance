<template>
  <div class="container">
    <h2>Most popular <span @click="showModal = !showModal">show all</span></h2>
    <div class="pie-chart">
      <div ref="chart" class="chart-container"></div>
    </div>
  </div>

  <div class="modal-outside" v-show="showModal" @click="showModal = false">
    <div class="modal-inside">
      <ul>
        <li v-for="(data, idx) in charData.sort((a: any, b: any) => b.value - a.value)" :key="idx">
          {{ data.name }}: {{ Math.round(data.value / 1000) }}min
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as echarts from 'echarts'
import { ref } from 'vue'

const showModal = ref(false)

const chart = ref<HTMLElement | null>(null)
const API_URL = 'http://127.0.0.1:8080/api/activities/sum_visited_domains/1'

const charData = ref([])

fetch(API_URL)
  .then((response) => response.json())
  .then((data) => {
    charData.value = data.activities.map((item: any) => {
      return {
        name: item.name,
        value: item.value
      }
    })

    const option = {
      tooltip: {
        trigger: 'item',
        valueFormatter: (value: number) => (Math.round(value / 600) / 100).toFixed(1) + 'h'
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
          data: charData.value.slice(0, 6).sort((a: any, b: any) => b.value - a.value)
        }
      ]
    }
    var myChart = echarts.init(chart.value!)
    option && myChart.setOption(option)
  })
</script>

<style scoped>
.container {
  flex: 2;
  height: 100%;
  min-height: 40rem;
}

h2 span {
  font-size: 1rem;
  margin-top: 5px;
  cursor: pointer;
}
h2 {
  display: flex;
  align-items: center;
  justify-content: space-between;
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

.modal-outside {
  position: fixed;
  width: 100vw;
  height: 100vh;
  left: 0;
  top: 0;
  background-color: rgba(0, 0, 0, 0.1);
  z-index: 10;
}

.modal-inside {
  position: absolute;
  width: 60vw;
  height: 80vh;
  left: 20vw;
  top: 10vh;
  background-color: #fff;
  z-index: 1000;
  border: 4px solid #c8c8c8;
  border-radius: 5px;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
</style>
