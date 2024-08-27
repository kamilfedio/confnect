<script setup lang="ts">
import LandingPage from './page/LandingPage/LandingPage.vue'
import FooterComponent from './components/FooterComponent/FooterComponent.vue'
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

.wrapper {
  width: 100vw;
  max-width: 1200px;
  margin: 0 auto;
  overflow: hidden;
}
</style>
