<template>
  <div class="container">
    <h2>Raw Statistics</h2>
    <div class="statistics">
      <ul>
        <li>opend cards: 951</li>
        <li>average time per card: 4.42s</li>
        <li>total time spent: 13.54h</li>
        <li>fastest closed tab: 0.932s</li>
        <li>longest opened tab: 53.2min</li>
        <li>most visited domain: youtube.com</li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.container {
  flex: 1;
}
.statistics {
  height: 40rem;

  background: rgba(255, 255, 255, 0.49);
  border-radius: 16px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(8.7px);
  -webkit-backdrop-filter: blur(8.7px);
  border: 1px solid rgba(255, 255, 255, 1);
}
</style>
