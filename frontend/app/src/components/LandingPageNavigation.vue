<template>
  <nav class="nav">
    <ul class="nav__list">
      <li class="nav__item">
        <button class="nav__btn" @click="props.onScrollToFeatures()">features</button>
      </li>
      <li class="nav__item">
        <button class="nav__btn" @click="props.onScrollToAbout">about</button>
      </li>
      <li class="nav__item">
        <button class="nav__btn" @click="props.onScrollToContact">contact</button>
      </li>
    </ul>
  </nav>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  onScrollToFeatures: {
    type: Function,
    required: false
  },
  onScrollToAbout: {
    type: Function,
    required: false
  },
  onScrollToContact: {
    type: Function,
    required: false
  }
})
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
