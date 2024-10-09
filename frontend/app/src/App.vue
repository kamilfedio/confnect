<script setup lang="ts"></script>

<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style lang="scss">
html {
  font-family: 'Questrial';
  font-size: 10px;
  background-color: $mainBgc;
  @media (max-width: 960px) {
    font-size: 8px;
  }
  @media (max-width: 430px) {
    font-size: 7px;
  }
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>
