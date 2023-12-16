<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Kanit:wght@200;500&display=swap');

body {
  font-family: 'Kanit', sans-serif;
  margin: 0;
  padding: 0;
  background-color: #abd8e9;
}

#app {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
h2 {
  font-weight: normal;
}
</style>
