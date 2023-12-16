<template>
  <header>
    <nav>
      <div class="logo">
        <img src="@/assets/logo.webp" alt="logo" />
        track your life
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
        <div class="arrow" />
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

.arrow {
  position: absolute;
  width: 0;
  right: 3.75rem;
  height: 0;
  border-top: 0.5rem solid #c8c8c8;
  border-left: 0.5rem solid transparent;
  border-right: 0.5rem solid transparent;
}
.logo {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-top: 3px;
  color: black;
}

.logo img {
  width: 3rem;
  height: 3rem;
  object-fit: cover;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
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
