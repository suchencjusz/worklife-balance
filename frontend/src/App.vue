<script setup lang="ts">
import { RouterView } from 'vue-router'
import TheNavBar from './components/TheNavBar.vue'
</script>

<template>
  <TheNavBar />
  <RouterView />
</template>

<style scoped></style>

<style>
body {
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif;
  background-color: #d4ebf2;
}

#app {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>
