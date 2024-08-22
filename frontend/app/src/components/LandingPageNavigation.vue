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

<script>
export default {
  name: 'LandingPageNavigation',
  props: ['onScrollToFeatures', 'onScrollToAbout', 'onScrollToContact']
}
</script>

<style scoped lang="scss">
.nav {
  padding-left: 10px;
  &__list {
    list-style: none;
    display: flex;
  }
  &__item {
    padding: 0 10px;
  }
  &__btn {
    border: none;
    font-size: 1.6em;
    font-family: 'Questrial';
    cursor: pointer;
  }
}
</style>
