<template>
  <div class="container">
    <h2>Raw Statistics</h2>
    <div class="statistics">
      <ul>
        <li>
          <h3>opend cards</h3>
          <p>951</p>
        </li>
        <li>
          <h3>average time per card</h3>
          <p>4.42s</p>
        </li>
        <li>
          <h3>total time spent</h3>
          <p>13.54h</p>
        </li>
        <li>
          <h3>fastest closed tab</h3>
          <p>0.932s</p>
        </li>
        <li>
          <h3>longest opened tab</h3>
          <p>53.2min</p>
        </li>
        <li>
          <h3>most visited domain</h3>
          <p>youtube.com</p>
        </li>
        <li>
          <h3>longest session</h3>
          <p>6.5h</p>
        </li>
        <li>
          <h3>drinks drinked</h3>
          <p>23</p>
        </li>
        <li>
          <h3>average session</h3>
          <p>103.2min</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.container {
  flex: 2;
  height: 40rem;
}

.statistics {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

ul {
  padding: 0;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  height: 100%;
}

h3 {
  margin-top: -3px;
  font-size: 1.2rem;
  font-weight: normal;
  margin-bottom: 0.5rem;
}

li p {
  position: absolute;
  top: 50%;
  left: 50%;
  font-size: 1.1rem;
  transform: translate(-50%, -50%);
}

li {
  flex: 1;
  position: relative;
  list-style: none;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.49);
  border-radius: 5px;
  text-align: center;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(8.7px);
  -webkit-backdrop-filter: blur(8.7px);
  border: 1px solid rgba(255, 255, 255, 1);
}
</style>
