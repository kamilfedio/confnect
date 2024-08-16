<template>
  <header>
    <div class="header">
      <div class="header__brand">Confnect</div>
      <div class="header__nav">
        <LandingPageNavigationVue />
      </div>
      <div class="header__login">
        <button class="header__btn">login</button>
      </div>
    </div>
  </header>
  <main>
    <section class="introduction">
      <p class="introduction__slogan">
        Are you bored with your usual presentations? Or maybe you want to clear up the mess of a
        rain of questions? We have something for you!
      </p>
      <div class="introduction__icon"></div>
      <div class="introduction__logo">
        <img src="../img/transparentBgc_logo.png" alt="brand logo" class="introduction__img" />
      </div>
      <p class="introduction__text">Your assistant in presentations</p>
      <button class="introduction__btn">Get started</button>
    </section>
  </main>
</template>

<script setup lang="ts">
import LandingPageNavigationVue from '../components/LandingPageNavigation.vue'
</script>

<style lang="scss">
header {
  height: 10vh;
}

.header {
  display: flex;
  align-items: flex-end;
  width: 100%;
  height: 50px;
  padding: 70px 0 50px 0;

  &__brand {
    font-size: 2.4em;
    padding: 0 100px 0 10px;
  }

  &__nav {
    flex-grow: 2;
    font-size: 1.8em;
  }

  &__login {
    padding: 0 10px;
  }
  &__btn {
    font-size: 1.3em;
    width: 87px;
    height: 30px;
    color: $mainDarkBlue;
    border: 1px solid $mainBlack;
    border-radius: 20px;
  }
}

main {
  .introduction {
    width: 60%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    &__slogan {
      font-size: 2.4em;
      text-align: center;
      margin-top: 150px;
      letter-spacing: 1px;
    }
    &__logo {
      margin: 0 auto;
      margin-top: 80px;
    }
    &__text {
      text-align: center;
      font-size: 2em;
      margin-top: 20px;
    }
    &__btn {
      font-size: 1.6em;
      width: 195px;
      height: 45px;
      color: $mainDarkBlue;
      border: 2px solid $mainDarkBlue;
      border-radius: 20px;
      margin: 0 auto;
      margin-top: 40px;
    }
  }
}
</style>
