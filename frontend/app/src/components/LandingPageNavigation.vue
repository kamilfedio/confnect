<template>
  <nav class="nav">
    <ul class="nav__list">
      <li class="nav__item">
        <button class="nav__btn">features</button>
      </li>
      <li class="nav__item">
        <button class="nav__btn">about</button>
      </li>
      <li class="nav__item">
        <button class="nav__btn">contact</button>
      </li>
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
  &__btn {
    border: none;
    font-size: 1.6em;
    font-family: 'Questrial';
  }
}
</style>
