<template>
  <header>
    <nav>
      <div class="logo">
        <img src="@/assets/logo.png" alt="logo" />
      </div>
      <div class="links">
        <ul>
          <li>
            <router-link to="/">Dashboard</router-link>
          </li>
          <li>
            <router-link to="/about">Settings</router-link>
          </li>
        </ul>
        <div class="avatar">
          <img src="https://avatars.githubusercontent.com/u/10047099?v=4" alt="avatar" />
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts"></script>

<style scoped>
.links {
  display: flex;
  align-items: center;
  gap: 3rem;
}
.logo {
  width: 3rem;
}

.logo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

ul {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
  gap: 1rem;
}

header {
  background-color: #fff;
  color: #fff;
  padding: 0.5rem;
  border-bottom: 2px solid #c8c8c8;
}

li {
  font-size: 1rem;
  border: 3px solid #c8c8c8;
  padding: 0.5rem;
  border-radius: 0.5rem;
}

li a {
  color: #000;
  text-decoration: none;
}

.avatar {
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid #c8c8c8;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
