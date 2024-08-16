<template>
  <nav class="nav">
    <ul class="nav__list">
      <li class="nav__item">features</li>
      <li class="nav__item">about</li>
      <li class="nav__item">contact</li>
    </ul>
  </nav>
</template>

<style lang="scss">
.nav {
  padding-left: 10px;
  &__list {
    list-style: none;
    display: flex;
  }
  &__item {
    padding: 0 10px;
  }
}
</style>
