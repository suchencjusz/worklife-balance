<template>
  <main>
    <div class="small-widgets">
      <TimeSpentPerCategory />
      <RawStatistics />
      <PieChart />
    </div>
    <timePerDay />
  </main>
</template>

<script setup lang="ts">
import PieChart from '@/components/PieChart.vue'
import timePerDay from '@/components/TimePerDay.vue'
import RawStatistics from '@/components/RawStatistics.vue'
import TimeSpentPerCategory from '@/components/TimeSpentPerCategory.vue'
</script>

<style scoped>
main {
  padding: 2rem;
}

.small-widgets {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 2rem;
  width: 100%;
}
</style>
