<template>
  <nav class="nav">
    <ul class="nav__list">
      <li class="nav__item">
        <button class="nav__btn" @click="onScrollToFeatures">features</button>
      </li>
      <li class="nav__item">
        <button class="nav__btn" @click="onScrollToAbout">about</button>
      </li>
      <li class="nav__item">
        <button class="nav__btn" @click="onScrollToContact">contact</button>
      </li>
    </ul>
  </nav>
</template>

<script src="./LandingPageNavigation.vue.ts"></script>
<style src="./LandingPageNavigation.scss" scoped></style>
