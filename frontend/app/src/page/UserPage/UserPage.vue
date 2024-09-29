<template>
  <div class="wrapper">
    <header>
      <div class="topPanel">
        <img src="../../img/transparentBgc_logo.png" alt="brandLogo" class="topPanel__logo" />
        <div class="topPanel__profile profile">
          <div class="profile__name">
            <p class="profile__firstName">{{ userStore.user.first_name }}</p>
            <p class="profile__surName">{{ userStore.user.last_name }}</p>
          </div>
          <div class="profile__img"></div>
        </div>
      </div>
    </header>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script src="./UserPage.vue.ts"></script>
<style src="./UserPage.scss" scoped></style>
