<script setup lang="ts">
import LandingPage from './page/LandingPage.vue'
import FooterComponent from './components/FooterComponent.vue'
</script>

<template>
  <div class="wrapper">
    <LandingPage />
  </div>
  <FooterComponent />
</template>

<style lang="scss">
html {
  font-family: 'Questrial';
  font-size: 10px;
  background-color: $mainBgc;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.wrapper {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}
</style>
